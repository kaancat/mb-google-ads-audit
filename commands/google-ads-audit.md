---
description: Comprehensive Google Ads account audit with diagnostic report and action plan
allowed-tools: Bash(*), Read, Write, Edit, WebFetch, AskUserQuestion, Task, TodoWrite
---

# Google Ads Audit Workflow

You are performing a comprehensive Google Ads account audit. This is a multi-phase workflow that produces a diagnostic report with severity-ranked findings and a prioritized action plan.

## Prerequisites

Before starting, ensure you have:
- Google Ads account access (Customer ID)
- Website URL for the business being audited

## Workflow Phases

Execute phases sequentially. Each phase has detailed instructions in `skills/google-ads-audit/phases/`.

### Phase 0: Discovery (GATE)
**File:** `phase-0-discovery.md`
**Output:** `discovery_brief.md`

1. **Website Analysis** - Understand business, services, conversion paths
2. **Discovery Interview** - 11 questions establishing context
3. **Derive Targets** - Target CPA/ROAS from account or interview

**GATE: Cannot proceed to any other phase without completing discovery.**

### Phase 1: Conversion & Tracking Audit
**File:** `phase-1-tracking.md`
**Output:** `tracking_audit.md`

- Conversion actions review
- Attribution model assessment (Data-driven preferred)
- Time lag analysis
- Enhanced conversions check
- Conversion trust level determination

### Phase 2: Account Structure Analysis
**File:** `phase-2-structure.md`
**Output:** `structure_analysis.md`

- Campaign hierarchy review
- Ad group organization
- Network settings check (Search vs Display)
- Geographic targeting review
- Naming conventions assessment

### Phase 3: Campaign Performance Analysis
**File:** `phase-3-performance.md`
**Output:** `performance_analysis.json`

- Campaign metrics (30/90/180 day windows)
- Budget utilization analysis
- Bid strategy effectiveness vs targets
- Campaign tiering (Stars/Workhorses/Question Marks/Dogs)
- Auction Insights review

### Phase 4: Keyword & Search Term Analysis (TENTPOLE)
**File:** `phase-4-keywords.md`
**Output:** `keyword_audit.json`

- Quality Score distribution (spend-weighted)
- Search terms wasted spend analysis
- Negative keyword gap identification
- N-gram analysis
- Converting term identification

### Phase 5: Ad Copy & Asset Analysis
**File:** `phase-5-ads.md`
**Output:** `ad_copy_audit.json`

- RSA strength distribution
- Headline/description coverage (need 10+/3+ for pinning flexibility)
- Asset performance (sitelinks, callouts, snippets)
- Landing page alignment
- Quick win identification

### Phase 6: Synthesis & Recommendations
**File:** `phase-6-synthesis.md`
**Output:** `recommendations.json`

- Aggregate all findings from Phases 1-5
- Validate against `$WORKING_WELL` (exclude intentional items)
- Apply severity scoring (Critical/High/Medium/Low)
- Quantify DKK impact for all findings
- Create P0/P1/P2 action plan
- Identify quick wins

### Phase 7: Presentation
**File:** `phase-7-presentation.md`
**Output:** `audit_presentation.html`

- Executive summary with critical finding headline
- Key metrics snapshot
- Findings organized by section
- Priority action plan
- Quick wins checklist
- Technical appendices

## Critical Rules

1. **Complete discovery before analysis** - Context shapes interpretation
2. **Quantify everything** - Every finding needs estimated DKK impact
3. **Severity is mandatory** - Critical / High / Medium / Low for every finding
4. **Don't fix intentional strategies** - Validate against `$WORKING_WELL`
5. **Lead with impact** - Executive summary first, details in appendices
6. **Use canonical categories** - 17 finding categories across 5 phases

## Severity Levels

| Level | Criteria |
|-------|----------|
| **CRITICAL** | Blocking optimization, ≥50% budget waste |
| **HIGH** | Significant impact, 20-50% waste, tracking issues |
| **MEDIUM** | Improvement opportunity with measurable impact |
| **LOW** | Best practice, nice to have |

## MCP RAG Tools

Use these to inform your analysis:
- `query_knowledge("audit")` - Search audit methodology
- `get_methodology("audit")` - Get audit-specific guidance
- `get_deliverable_schema("keyword_analysis")` - Schema reference

## Getting Started

### Option A: User knows the Customer ID
Ask for:
1. Google Ads Customer ID (e.g., `123-456-7890`)
2. Website URL
3. Audit period (default: last 90 days)

### Option B: User provides account name
If user provides a name instead of ID:

1. **List accessible accounts:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/list_accounts.py
```

2. **Match by name** - Find the account matching the user's input
3. **Confirm with user** - Show the matched account and ID before proceeding
4. **Continue with the ID**

### Then:
Load and execute `phase-0-discovery.md` to start the discovery process.
