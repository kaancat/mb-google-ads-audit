# mb-google-ads-audit

Google Ads account audit plugin for Claude Code. Comprehensive diagnostic analysis with actionable recommendations.

## Status: Implementation Complete - Ready for Testing

Deep research phase completed. Architecture designed and documented. All components implemented including phase prompts, hooks, schemas, and command entry point.

### Implementation Progress
- [x] SKILL.md main skill definition
- [x] hooks.json with phase gate validation
- [x] validate-phase-gate.py (PreToolUse hook)
- [x] validate-completion.py (Stop hook)
- [x] JSON schemas for all output artifacts
- [x] All 8 phase prompt files (phases 0-7)
- [x] Presentation template (audit_presentation.html)
- [x] Plugin manifest (.claude-plugin/plugin.json)
- [x] Command entry point (commands/google-ads-audit.md)
- [x] Automated test suite (scripts/test_plugin.py - 55 tests passing)

### Research Documents (in `/research/`)

| Document | Description |
|----------|-------------|
| **PPC_SPECIALIST_AUDIT_FRAMEWORK.md** | Comprehensive synthesis of how PPC specialists approach audits - mindset, methodology, decision frameworks |
| **AUDIT_CHECKLIST.md** | Practical checklist for conducting audits, organized by phase |
| **PLUGIN_ARCHITECTURE.md** | Detailed plugin architecture with phase workflows, decision trees, schemas |

---

## Vision

A comprehensive Google Ads audit system that produces diagnostic reports with severity-ranked findings and prioritized action plans. Similar workflow to `mb-keyword-analysis` but focused on analyzing existing accounts rather than building new campaigns.

**Primary Deliverable:** Diagnostic report + action plan, beautifully presented (like `presentation.html` in keyword plugin).

**Key Constraint:** Typically only Google Ads access available (not GA4), so the audit must work with Ads data alone.

---

## Research Summary

### Sources Consulted

1. **Web Research:**
   - [Promodo Google Ads Audit Checklist 2025](https://www.promodo.com/blog/google-ads-audit-checklist)
   - [North Country 7-Figure Account Audit Checklist](https://www.northcountrygrowth.com/blog/steal-our-2025-google-ads-audit-checklist-used-by-7-figure-accounts)
   - [Adalysis PPC Audit Guide](https://adalysis.com/how-to-audit-a-google-ads-account-the-ultimate-ppc-audit-checklist-2021/)
   - [Search Engine Land: Agency-Grade PPC Audits](https://searchengineland.com/agency-grade-ppc-audits-reports-growth-roadmaps-460929)

2. **RAG Knowledge Base (Section 15: The Google Ads Audit Playbook):**
   - 15.1 Different Types of Audits
   - 15.2 Guide to our Google Ads Audit Process
   - 15.3 A Quick Wins Cheat Sheet
   - 15.4 Key Takeaways
   - 15.5 Free Audit

3. **Existing Audit Examples:**
   - `/clients/nmd_law/documentation/nmd_audit_6month_20251201.md` - 524-line comprehensive audit
   - `/output/karim_design_audit.md`
   - `backend/scripts/audit_account.py` - 350+ lines of audit data fetching

---

## Three Types of Audits (from Knowledge Base)

| Type | Focus | Examples |
|------|-------|----------|
| **Quick Wins** | Egregious errors, immediate fixes | No conversion tracking, only 2/15 headlines, search terms eating budget |
| **Strategic** | Business goals alignment, testing framework | SWOT, campaign structure matches goals, scaling potential |
| **Optimization** | Day-to-day blueprint | Negative keywords, budget adjustments, sitelink performance |

**Best audits combine all three.**

---

## The 12-Step Audit Process (from Course)

1. **Website first** - understand the business (spend ~1 hour)
2. Competitors & Google searches
3. Conversion tracking - is it set up?
4. Search term report - wasted spend analysis
5. Ads - RSA quality, extensions
6. Sitelinks, callouts, structured snippets
7. Bid strategies & targets vs actuals
8. Quality Score analysis
9. Budget adjustments - which campaigns limited by budget?
10. Landing page URLs - are they correct?
11. N-gram analysis
12. Best practice checklist

**Three Tentpoles:** Business understanding, Conversion tracking, Search term report

---

## Quick Wins Checklist (from Course)

- [ ] Conversion tracking accuracy
- [ ] Attribution settings (last-click = problem)
- [ ] Enhanced conversion tracking enabled?
- [ ] Campaign consolidation (too fragmented?)
- [ ] Negative keywords (haven't added any in a year?)
- [ ] Ad copy (typos, missing headlines/descriptions)
- [ ] Only 1-2 headlines in RSAs (need 10-15)
- [ ] Only 1 out of 4 descriptions
- [ ] Incorrect audiences/placements
- [ ] Bad budget/bid settings
- [ ] Landing page URLs incorrect
- [ ] Filter: assets with $300+ clicks, <3 conversions

---

## Audit Components (Comprehensive List)

### Foundation Layer (Data Gathering)
1. Account structure analysis (campaigns, ad groups, hierarchy)
2. Conversion tracking setup (actions, attribution, time lag)
3. Campaign performance metrics
4. Keyword performance & Quality Score
5. Search terms & wasted spend
6. Ad copy & RSA strength
7. Asset analysis (sitelinks, callouts, structured snippets, etc.)
8. Landing page alignment
9. Device/geographic/demographic splits
10. Impression share & competition (Auction Insights)
11. Budget allocation & bidding strategy
12. Change history review

### Analysis Layer (Diagnosis)
- Severity matrix (Critical / High / Medium / Low)
- Wasted spend quantification
- Root cause identification
- Benchmark comparison (targets vs actuals)

### Output Layer (Deliverable)
- Executive summary with key findings
- Section-by-section analysis
- Prioritized action plan (P0 immediate → P2 medium-term)
- Quick wins checklist
- Technical appendices

---

## Discovery Questions (Draft - 11 Questions)

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What are your primary business goals? (Leads, Sales, Brand) | Frames entire analysis |
| 2 | Which campaigns/services are most important to you? | Prioritizes analysis depth |
| 3 | What's working well right now? | Don't "fix" what's intentional |
| 4 | What concerns do you have about the account? | Direct issues to investigate |
| 5 | How are conversions tracked? (Forms, calls, purchases, offline?) | Understanding what data represents |
| 6 | What significant changes were made in the last 6 months? | Context for performance shifts |
| 7 | Are there seasonal patterns in your business? | Prevents misdiagnosing normal fluctuations |
| 8 | Brand vs non-brand strategy - any intentional approach? | Don't flag brand as "too expensive" |
| 9 | What's your profit margin or customer lifetime value? | Contextualizes CPA recommendations |
| 10 | Any competitors you're specifically watching? | Auction insights context |
| 11 | What would a successful audit outcome look like for you? | Shapes deliverable focus |

**Note:** Target CPA/ROAS can be inferred from account data (conversion goals, historical performance).

Plus **website scraping** to understand services, landing pages, and conversion paths.

---

## Architecture (Decided: 8-Phase Sequential Workflow)

Based on deep research into PPC specialist methodology, we've selected a sequential phase approach with a mandatory discovery gate. See `/research/PLUGIN_ARCHITECTURE.md` for full details.

```
Phase 0: DISCOVERY (GATE - cannot proceed without)
         ├── Website Analysis
         └── Discovery Interview (11 questions)
         Output: discovery_brief.md

Phase 1: CONVERSION & TRACKING AUDIT
         ├── Conversion Actions Review
         ├── Attribution Model Assessment
         └── Time Lag Analysis
         Output: tracking_audit.md

Phase 2: ACCOUNT STRUCTURE ANALYSIS
         ├── Campaign Hierarchy
         ├── Ad Group Organization
         └── Network/Geo Settings
         Output: structure_analysis.md

Phase 3: CAMPAIGN PERFORMANCE ANALYSIS
         ├── Metrics (30/90/180 day windows)
         ├── Budget Utilization
         ├── Bid Strategy Effectiveness
         └── Auction Insights
         Output: performance_analysis.json

Phase 4: KEYWORD & SEARCH TERM ANALYSIS
         ├── Quality Score Distribution
         ├── Search Terms Wasted Spend
         ├── Negative Keyword Gaps
         └── N-Gram Analysis
         Output: keyword_audit.json

Phase 5: AD COPY & ASSET ANALYSIS
         ├── RSA Strength/Coverage
         ├── Extension Utilization
         └── Landing Page Alignment
         Output: ad_copy_audit.json

Phase 6: SYNTHESIS & RECOMMENDATIONS
         ├── Severity Matrix Generation
         ├── Quick Wins Extraction
         └── Action Plan (P0/P1/P2)
         Output: recommendations.json

Phase 7: PRESENTATION
         └── Client-ready deliverable
         Output: audit_presentation.html
```

**Core Principles:**
- Discovery before diagnosis (context shapes interpretation)
- Three tentpoles: Business understanding, Conversion tracking, Search terms
- All findings require severity rating + DKK impact estimation
- Don't "fix" intentional strategies - ask first

---

## Technical Infrastructure

### Backend Services (Included)

The plugin includes backend services from the Monday Brew ecosystem:

| File | Purpose | Size |
|------|---------|------|
| `backend/services/ads_connector.py` | Full Google Ads API wrapper | 114KB |
| `backend/services/credentials.py` | Centralized credential loading | 1KB |
| `backend/services/ga4_service.py` | GA4 integration (optional) | 22KB |
| `scripts/audit_account.py` | Audit data fetching | 8KB |

### Credential Requirements

Configure in `~/.mondaybrew/.env`:
```env
GOOGLE_ADS_DEVELOPER_TOKEN=xxx
GOOGLE_ADS_CLIENT_ID=xxx
GOOGLE_ADS_CLIENT_SECRET=xxx
GOOGLE_ADS_REFRESH_TOKEN=xxx
GOOGLE_ADS_LOGIN_CUSTOMER_ID=xxx
```

### Data Flow

```
1. Run: python scripts/audit_account.py --customer-id [ID]
2. Output: output/audit_[ID]_[DATE].json
3. Phases 1-5 analyze the JSON data
4. Phase 6 synthesizes findings
5. Phase 7 generates presentation
```

### MCP RAG Available
- `query_knowledge()` - Search audit methodology
- `get_methodology("audit")` - Get audit-specific guidance
- `get_example()` - Case study retrieval
- `get_deliverable_schema()` - Output format specs

### Existing Audit Output Format (from NMD Law example)
- Executive Summary with severity matrix
- Section-by-section analysis (10 sections)
- Tables with metrics, assessments, and recommendations
- Priority action plan (P0/P1/P2)
- Technical appendices (negative keywords, keyword additions)

---

## Next Steps

### Completed (Research Phase)
- [x] Deep research into PPC specialist audit methodology
- [x] Synthesize findings into comprehensive framework
- [x] Document audit checklist by phase
- [x] Design 7-phase plugin architecture
- [x] Define severity scoring system
- [x] Create decision trees for findings interpretation
- [x] Finalize discovery interview questions (11 questions)
- [x] Design data extraction requirements

### Completed (Strengthening Phase)
- [x] Applied `mb-keyword-analysis` patterns to architecture:
  - Variable storage pattern (`$VARIABLE_NAME`)
  - Phase gating with explicit checkpoints ("STOP. Do not proceed.")
  - Canonical finding categories (single source of truth)
  - Schema with embedded guidelines and enums
- [x] Created `skills/google-ads-audit/templates/discovery_brief.md`
- [x] Created `skills/google-ads-audit/decision-trees/severity-scoring.md`
- [x] Updated `AUDIT_CHECKLIST.md` with variable mappings and checkpoints
- [x] Updated `PLUGIN_ARCHITECTURE.md` with comprehensive variable system

### Completed (Presentation Phase)
- [x] Created `skills/google-ads-audit/templates/audit_presentation.html`
  - Monday Brew dark mode styling (extracted from website globals.css)
  - Path-based SVG logo (font-independent)
  - Severity color system (Critical/High/Medium/Low)
  - Responsive design with print styles
  - Handlebars-style placeholders for data injection
  - Self-contained (deploy directly to Vercel)

### Completed (Implementation Phase)
- [x] Create `SKILL.md` main skill definition
- [x] Create `phases/phase-0-discovery.md` prompt file
- [x] Implement `hooks/hooks.json` with phase gate validation
- [x] Create `hooks/validate-phase-gate.py` (PreToolUse hook)
- [x] Create `hooks/validate-completion.py` (Stop hook)
- [x] Create JSON schema files in `schemas/` directory:
  - `performance_analysis.schema.json`
  - `keyword_audit.schema.json`
  - `ad_copy_audit.schema.json`
  - `recommendations.schema.json`

### Remaining (Testing & Refinement)
1. [x] Create all phase prompt files (phases 0-7) ✅
2. [x] Create `.claude-plugin/plugin.json` manifest ✅
3. [x] Create main command file `commands/google-ads-audit.md` ✅
4. [x] Automated test suite (55 tests passing) ✅
5. [ ] Create additional decision tree files (optional - core logic in phase files)
6. [ ] Test with real Google Ads account data
7. [ ] Iterate based on real audit results

---

## Installation (Future)

```bash
/plugin install mb-google-ads-audit@mb-plugins
```

## Usage (Future)

```bash
/google-ads-audit
```

---

## Plugin Structure (per Claude Code Docs)

```
mb-google-ads-audit/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/
│   └── google-ads-audit.md      # Main /google-ads-audit command
├── agents/                       # Subagent definitions (if needed)
├── skills/
│   └── google-ads-audit/
│       ├── SKILL.md             # ✅ Created - Main skill definition
│       ├── phases/
│       │   ├── phase-0-discovery.md     # ✅ Created - Discovery gate
│       │   ├── phase-1-tracking.md      # ✅ Created - Conversion tracking
│       │   ├── phase-2-structure.md     # ✅ Created - Account structure
│       │   ├── phase-3-performance.md   # ✅ Created - Performance analysis
│       │   ├── phase-4-keywords.md      # ✅ Created - Keywords & search terms
│       │   ├── phase-5-ads.md           # ✅ Created - Ad copy & assets
│       │   ├── phase-6-synthesis.md     # ✅ Created - Findings synthesis
│       │   └── phase-7-presentation.md  # ✅ Created - Final deliverable
│       ├── decision-trees/
│       │   └── severity-scoring.md      # ✅ Created - Finding severity logic
│       ├── templates/
│       │   ├── discovery_brief.md       # ✅ Created - Phase 0 output template
│       │   └── audit_presentation.html  # ✅ Created - Client-facing HTML report
│       └── examples/                    # Golden audit examples (TODO)
├── hooks/
│   ├── hooks.json               # ✅ Created - Phase gate validation
│   ├── validate-phase-gate.py   # ✅ Created - PreToolUse hook
│   └── validate-completion.py   # ✅ Created - Stop hook
├── research/
│   ├── PPC_SPECIALIST_AUDIT_FRAMEWORK.md  # ✅ Complete
│   ├── AUDIT_CHECKLIST.md                 # ✅ Strengthened with variables
│   └── PLUGIN_ARCHITECTURE.md             # ✅ Strengthened with patterns
├── scripts/                      # Utility scripts (TODO)
├── schemas/                      # ✅ Created - JSON schemas for outputs
│   ├── performance_analysis.schema.json
│   ├── keyword_audit.schema.json
│   ├── ad_copy_audit.schema.json
│   └── recommendations.schema.json
├── CLAUDE.md                    # Plugin context for Claude
└── README.md                    # This file
```

### Component Purposes

| Directory | Purpose |
|-----------|---------|
| `commands/` | Entry point - the `/google-ads-audit` slash command |
| `skills/` | Workflow logic, decision trees, templates |
| `hooks/` | Phase gate validation (ensure discovery before analysis) |
| `scripts/` | Data extraction, presentation generation |
| `schemas/` | Enforce consistent output formats |

---

## Related

- [mb-keyword-analysis](https://github.com/kaancat/mb-keyword-analysis) - Keyword research plugin
- [Google Ads - Monday Brew](../Projects/Google%20Ads%20-%20mondaybrew) - Backend services and knowledge base
- [mb-marketplace](https://github.com/kaancat/mb-marketplace) - Plugin registry
