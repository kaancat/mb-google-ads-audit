# mb-google-ads-audit

A comprehensive Google Ads account audit plugin for [Claude Code](https://claude.ai/code). Performs diagnostic analysis with severity-ranked findings and prioritized action plans.

**Repository:** https://github.com/kaancat/mb-google-ads-audit
**Marketplace:** https://github.com/kaancat/mb-marketplace
**Version:** 1.0.2

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [The 8-Phase Workflow](#the-8-phase-workflow)
- [Plugin Architecture](#plugin-architecture)
- [File Structure](#file-structure)
- [How Claude Code Plugins Work](#how-claude-code-plugins-work)
- [Audit Methodology (from RAG)](#audit-methodology-from-rag)
- [Configuration](#configuration)
- [Development](#development)
- [Related Projects](#related-projects)

---

## Installation

### From Marketplace

```bash
/plugin install mb-google-ads-audit@mb-plugins
```

### Local Development

```bash
claude --plugin-dir /path/to/mb-google-ads-audit
```

### Prerequisites

1. **Google Ads API credentials** in `~/.mondaybrew/.env`:
   ```env
   GOOGLE_ADS_DEVELOPER_TOKEN=xxx
   GOOGLE_ADS_CLIENT_ID=xxx
   GOOGLE_ADS_CLIENT_SECRET=xxx
   GOOGLE_ADS_REFRESH_TOKEN=xxx
   GOOGLE_ADS_LOGIN_CUSTOMER_ID=xxx
   ```

2. **Python 3.9+** with dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Quick Start

### Option 1: By Account Name
```
/google-ads-audit
> "Audit the NMD Law account"
```
The plugin will list accessible accounts, match by name, and confirm before proceeding.

### Option 2: By Customer ID
```
/google-ads-audit
> "Customer ID: 123-456-7890, Website: https://example.com"
```

### List Available Accounts
```bash
python3 scripts/list_accounts.py
python3 scripts/list_accounts.py --search "NMD"
python3 scripts/list_accounts.py --format json
```

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     AUDIT WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. USER INVOKES                                                │
│     /google-ads-audit                                           │
│           │                                                     │
│           ▼                                                     │
│  2. DATA FETCHING                                               │
│     scripts/audit_account.py --customer-id [ID]                 │
│     → output/audit_[ID]_[DATE].json                             │
│           │                                                     │
│           ▼                                                     │
│  3. PHASE 0: DISCOVERY (GATE)                                   │
│     - Scrape website                                            │
│     - 11 discovery questions                                    │
│     → audits/{client}/discovery_brief.md                        │
│           │                                                     │
│           ▼                                                     │
│  4. PHASES 1-5: ANALYSIS                                        │
│     Each phase analyzes the JSON data                           │
│     → tracking_audit.md, structure_analysis.md, etc.            │
│           │                                                     │
│           ▼                                                     │
│  5. PHASE 6: SYNTHESIS                                          │
│     - Aggregate findings                                        │
│     - Apply severity scores                                     │
│     - Quantify DKK impact                                       │
│     → recommendations.json                                      │
│           │                                                     │
│           ▼                                                     │
│  6. PHASE 7: PRESENTATION                                       │
│     - Generate client-ready HTML report                         │
│     → audit_presentation.html                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The 8-Phase Workflow

### Phase 0: Discovery (GATE)
**File:** `skills/google-ads-audit/phases/phase-0-discovery.md`
**Output:** `discovery_brief.md`

The mandatory starting point. Cannot proceed without completing discovery.

- **Website Analysis**: Understand business, services, conversion paths
- **11 Discovery Questions**: Establish context for interpretation
- **Derive Targets**: Extract target CPA/ROAS from account or interview

**Why it matters:** Context shapes interpretation. A "high CPA" is only bad if it exceeds the client's targets.

### Phase 1: Conversion & Tracking
**File:** `skills/google-ads-audit/phases/phase-1-tracking.md`
**Output:** `tracking_audit.md`

Validates data trustworthiness before analyzing performance.

- Conversion actions review
- Attribution model assessment (data-driven preferred)
- Time lag analysis
- Enhanced conversions check
- Trust level determination

**Key question:** "Is the data even trustworthy?"

### Phase 2: Account Structure
**File:** `skills/google-ads-audit/phases/phase-2-structure.md`
**Output:** `structure_analysis.md`

Reviews how the account is organized.

- Campaign hierarchy and naming conventions
- Ad group organization (SKAG vs thematic)
- Network settings (Search vs Display mixing)
- Geographic targeting review

### Phase 3: Campaign Performance
**File:** `skills/google-ads-audit/phases/phase-3-performance.md`
**Output:** `performance_analysis.json`

Analyzes campaign-level metrics and competition.

- Performance across 30/90/180 day windows
- Budget utilization (limited by budget?)
- Bid strategy effectiveness vs targets
- Campaign tiering (Stars/Workhorses/Question Marks/Dogs)
- Auction Insights competitor analysis

### Phase 4: Keywords & Search Terms (TENTPOLE)
**File:** `skills/google-ads-audit/phases/phase-4-keywords.md`
**Output:** `keyword_audit.json`

One of the three tentpoles - where wasted spend lives.

- Quality Score distribution (spend-weighted)
- Search terms wasted spend analysis
- Negative keyword gap identification
- N-gram analysis for patterns
- Converting term identification

### Phase 5: Ad Copy & Assets
**File:** `skills/google-ads-audit/phases/phase-5-ads.md`
**Output:** `ad_copy_audit.json`

Reviews creative quality and coverage.

- RSA strength distribution
- Headline/description coverage (need 10+/3+ for flexibility)
- Asset performance (sitelinks, callouts, snippets)
- Landing page alignment
- Quick win identification

### Phase 6: Synthesis
**File:** `skills/google-ads-audit/phases/phase-6-synthesis.md`
**Output:** `recommendations.json`

Aggregates all findings into actionable recommendations.

- Validate findings against `$WORKING_WELL` (exclude intentional items)
- Apply severity scoring (Critical/High/Medium/Low)
- Quantify DKK impact for all findings
- Create prioritized action plan (P0/P1/P2)
- Extract quick wins

### Phase 7: Presentation
**File:** `skills/google-ads-audit/phases/phase-7-presentation.md`
**Output:** `audit_presentation.html`

Generates the client-ready deliverable.

- Executive summary with critical finding headline
- Key metrics snapshot
- Findings organized by severity
- Priority action plan
- Quick wins checklist
- Technical appendices

---

## Plugin Architecture

### Severity Scoring System

| Level | Criteria | Example |
|-------|----------|---------|
| **CRITICAL** | Blocking optimization, ≥50% budget waste | No conversion tracking |
| **HIGH** | Significant impact, 20-50% waste | Poor QS keywords consuming 20%+ budget |
| **MEDIUM** | Improvement opportunity | Missing ad extensions |
| **LOW** | Best practice, nice to have | Ad copy could be stronger |

### Finding Categories (17 Canonical)

**Tracking (Phase 1):**
- `TRACKING_CONVERSION` - Conversion action issues
- `TRACKING_ATTRIBUTION` - Attribution model issues
- `TRACKING_ENHANCED` - Enhanced conversions
- `TRACKING_DATA_QUALITY` - Data reliability

**Structure (Phase 2):**
- `STRUCTURE_CAMPAIGN` - Campaign organization
- `STRUCTURE_AD_GROUP` - Ad group organization
- `STRUCTURE_NETWORK` - Network settings
- `STRUCTURE_TARGETING` - Geographic/demographic targeting

**Performance (Phase 3):**
- `PERFORMANCE_BUDGET` - Budget utilization
- `PERFORMANCE_BIDDING` - Bid strategy issues
- `PERFORMANCE_COMPETITION` - Competitive position

**Keywords (Phase 4):**
- `KEYWORD_QUALITY_SCORE` - QS issues
- `KEYWORD_WASTED_SPEND` - Search term waste
- `KEYWORD_NEGATIVE` - Missing negatives
- `KEYWORD_MATCH_TYPE` - Match type issues

**Ads (Phase 5):**
- `ADS_RSA` - RSA strength/coverage
- `ADS_ASSETS` - Extension utilization
- `ADS_LANDING_PAGE` - Landing page issues

### Variable Storage Pattern

Cross-phase data is stored as variables (e.g., `$TARGET_CPA`, `$BRAND_STRATEGY`) that subsequent phases reference for context-aware analysis.

### Phase Gating

Hooks enforce sequential execution:
- `validate-phase-gate.py` - Blocks writing Phase N output without Phase N-1 complete
- `validate-completion.py` - Ensures all phases complete before finishing

---

## File Structure

```
mb-google-ads-audit/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest (required)
│
├── commands/
│   └── google-ads-audit.md      # Entry point: /google-ads-audit
│
├── skills/
│   └── google-ads-audit/
│       ├── SKILL.md             # Main skill definition
│       ├── phases/              # 8 phase prompt files
│       │   ├── phase-0-discovery.md
│       │   ├── phase-1-tracking.md
│       │   ├── phase-2-structure.md
│       │   ├── phase-3-performance.md
│       │   ├── phase-4-keywords.md
│       │   ├── phase-5-ads.md
│       │   ├── phase-6-synthesis.md
│       │   └── phase-7-presentation.md
│       ├── decision-trees/
│       │   └── severity-scoring.md
│       └── templates/
│           ├── discovery_brief.md
│           └── audit_presentation.html
│
├── hooks/
│   ├── hooks.json               # Hook configuration
│   ├── validate-phase-gate.py   # PreToolUse: enforce phase order
│   └── validate-completion.py   # Stop: ensure completion
│
├── schemas/
│   ├── performance_analysis.schema.json
│   ├── keyword_audit.schema.json
│   ├── ad_copy_audit.schema.json
│   └── recommendations.schema.json
│
├── backend/
│   └── services/
│       ├── ads_connector.py     # Google Ads API wrapper (114KB)
│       ├── credentials.py       # Credential loading
│       └── ga4_service.py       # GA4 integration (optional)
│
├── scripts/
│   ├── audit_account.py         # Fetch all audit data
│   ├── list_accounts.py         # List accessible accounts
│   └── test_plugin.py           # Automated test suite
│
├── research/
│   ├── PPC_SPECIALIST_AUDIT_FRAMEWORK.md
│   ├── AUDIT_CHECKLIST.md
│   └── PLUGIN_ARCHITECTURE.md
│
├── CLAUDE.md                    # Context for Claude
├── README.md                    # This file
└── requirements.txt             # Python dependencies
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `.claude-plugin/plugin.json` | Tells Claude Code this is a plugin. Defines name, commands, hooks. |
| `commands/google-ads-audit.md` | The slash command entry point. Loaded when user runs `/google-ads-audit`. |
| `skills/*/SKILL.md` | Detailed workflow instructions. Auto-discovered by Claude Code. |
| `hooks/hooks.json` | Event handlers that run before/after tool calls. |
| `backend/services/ads_connector.py` | 1700+ line Google Ads API wrapper with 25+ methods. |
| `scripts/audit_account.py` | Fetches all audit data into a single JSON file. |

---

## How Claude Code Plugins Work

### Plugin Discovery

Claude Code discovers plugins via:
1. **Marketplace**: Remote repositories registered in a marketplace manifest
2. **Local**: `--plugin-dir` flag for development

### The Manifest (plugin.json)

Located at `.claude-plugin/plugin.json`:

```json
{
  "name": "mb-google-ads-audit",
  "version": "1.0.0",
  "description": "...",
  "author": { "name": "Monday Brew" },
  "commands": "./commands",
  "hooks": "./hooks/hooks.json"
}
```

Key rules:
- All paths must use `./` prefix (relative to plugin root)
- Name must be kebab-case
- Version must be semver (MAJOR.MINOR.PATCH)

### Commands

Files in `commands/` become slash commands. `google-ads-audit.md` → `/google-ads-audit`.

Command files use frontmatter for configuration:
```markdown
---
description: Comprehensive Google Ads account audit
allowed-tools: Bash(*), Read, Write, Edit, WebFetch
---

# Instructions for Claude...
```

### Skills

Skills in `skills/*/SKILL.md` are auto-discovered. They provide detailed instructions that Claude follows when the skill is invoked.

### Hooks

Hooks intercept events:
- `PreToolUse`: Before a tool runs (can block/modify)
- `PostToolUse`: After a tool runs
- `Stop`: When Claude wants to end the conversation

Example from this plugin - blocking Phase 2 write if Phase 1 not complete:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/validate-phase-gate.py"
      }]
    }]
  }
}
```

### Marketplace Distribution

Plugins are distributed via marketplace repositories. The marketplace manifest at `.claude-plugin/marketplace.json`:

```json
{
  "name": "mb-plugins",
  "plugins": [
    {
      "name": "mb-google-ads-audit",
      "source": {
        "source": "url",
        "url": "https://github.com/kaancat/mb-google-ads-audit.git"
      },
      "version": "1.0.0"
    }
  ]
}
```

Users install with: `/plugin install mb-google-ads-audit@mb-plugins`

---

## Audit Methodology (from RAG)

This plugin's methodology comes from the Monday Brew Google Ads knowledge base (RAG), specifically **Section 15: The Google Ads Audit Playbook**.

### The Three Types of Audits

| Type | Focus | Examples |
|------|-------|----------|
| **Quick Wins** | Egregious errors, immediate fixes | No conversion tracking, only 2/15 RSA headlines |
| **Strategic** | Business goals alignment | Campaign structure matches goals, scaling potential |
| **Optimization** | Day-to-day blueprint | Negative keywords, budget adjustments |

**Best audits combine all three.**

### The Three Tentpoles

1. **Business Understanding** - Website analysis, discovery interview
2. **Conversion Tracking** - Is data trustworthy?
3. **Search Term Report** - Where is spend being wasted?

### The 12-Step Process (from Course)

1. Website first (1 hour minimum)
2. Competitors & Google searches
3. Conversion tracking check
4. Search term report analysis
5. Ads review (RSA quality, extensions)
6. Sitelinks, callouts, structured snippets
7. Bid strategies (targets vs actuals)
8. Quality Score analysis
9. Budget analysis (limited by budget?)
10. Landing page URL verification
11. N-gram analysis
12. Best practice checklist

### Quick Wins Checklist

- [ ] Conversion tracking accuracy
- [ ] Attribution settings (last-click = problem)
- [ ] Enhanced conversions enabled?
- [ ] Campaign consolidation (too fragmented?)
- [ ] Negative keywords (added recently?)
- [ ] RSA headlines (need 10-15, not 2)
- [ ] RSA descriptions (need 3-4)
- [ ] Landing page URLs correct?
- [ ] Assets with $300+ clicks, <3 conversions

### Core Principles

1. **Discovery before diagnosis** - Context shapes interpretation
2. **Quantify everything** - Every finding needs estimated DKK impact
3. **Don't "fix" intentional strategies** - Ask first about brand campaigns, geo targeting
4. **Lead with impact** - Executive summary first, details in appendices

---

## Configuration

### Environment Variables

Set in `~/.mondaybrew/.env`:

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Your Google Ads API developer token |
| `GOOGLE_ADS_CLIENT_ID` | OAuth client ID |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth client secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth refresh token |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC account ID (for accessing client accounts) |

### MCP RAG Tools

The plugin uses the `google-ads-rag` MCP server for methodology guidance:

```python
query_knowledge("audit checklist")      # Search audit methodology
get_methodology("audit")                # Get audit-specific guidance
get_example("nmd_law")                  # Case study retrieval
get_deliverable_schema("keyword_audit") # Output format specs
```

---

## Development

### Running Tests

```bash
python3 scripts/test_plugin.py
```

**Current status:** 56 tests passing, 0 failures

### Testing Locally

```bash
claude --plugin-dir /Users/you/path/to/mb-google-ads-audit
```

Then run `/google-ads-audit` to test the workflow.

### Manual Data Fetch

```bash
# Fetch audit data for an account
python3 scripts/audit_account.py --customer-id 1234567890

# Output: output/audit_1234567890_20260112.json
```

### Adding a New Phase

1. Create `skills/google-ads-audit/phases/phase-X-name.md`
2. Follow the template: Purpose, Prerequisites, Steps, Checkpoint, Output
3. Update `commands/google-ads-audit.md` to reference it
4. Add to `hooks/validate-phase-gate.py` if needed
5. Run tests

---

## Related Projects

| Project | Description |
|---------|-------------|
| [mb-keyword-analysis](https://github.com/kaancat/mb-keyword-analysis) | Keyword research plugin (creates new campaigns) |
| [mb-marketplace](https://github.com/kaancat/mb-marketplace) | Plugin registry for Monday Brew plugins |

---

## License

MIT

---

**Built by [Monday Brew](https://mondaybrew.dk)** - Google Ads workflow automation for Claude Code.
