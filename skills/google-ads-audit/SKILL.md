---
name: Google Ads Audit Workflow
description: This skill should be used when the user asks to "audit a Google Ads account", "analyze Google Ads performance", "do a Google Ads audit", "review Google Ads setup", or provides a Google Ads customer ID for analysis. Orchestrates the full Monday Brew audit workflow from discovery to final presentation deliverable.
version: 1.0.0
---

# Google Ads Audit Workflow (Professional-Grade)

Complete Google Ads account audit workflow in **8 phases**. Each phase produces a clear artifact and **blocks** the next phase.

This skill transforms you from a checklist-follower into a **senior PPC specialist** who:
- **Understands the business first** - Context shapes every interpretation
- Validates assumptions before making recommendations
- Quantifies every finding in DKK impact
- Protects intentional strategies from "optimization"
- Prioritizes findings by severity and business impact
- Creates actionable, prioritized recommendations

---

## CRITICAL RULES

1. **Never skip Phase 0** - Discovery interview blocks everything else
2. **Context shapes interpretation** - A "high CPA" is only bad if it exceeds targets
3. **Don't "fix" intentional strategies** - Check `$WORKING_WELL` before flagging
4. **Every finding needs severity** - CRITICAL / HIGH / MEDIUM / LOW (no exceptions)
5. **Every finding needs DKK impact** - Quantify or estimate all findings
6. **Query RAG at decision points** - Use `query_knowledge("audit")` and `get_methodology("audit")`
7. **Three tentpoles first** - Business understanding, conversion tracking, search terms
8. **Lead with impact** - Executive summary first, details in appendices

---

## Data Fetching (REQUIRED FIRST STEP)

**Before ANY analysis, fetch all Google Ads data using the audit script.**

### Run the Audit Data Fetch

```bash
# From the plugin root directory
python scripts/audit_account.py --customer-id [CUSTOMER_ID]

# Optional: Include GA4 data (if available)
python scripts/audit_account.py --customer-id [CUSTOMER_ID] --ga4-domain example.com
```

### Output Files

The script generates:
- `output/audit_[CUSTOMER_ID]_[DATE].json` - Complete structured data
- `output/audit_[CUSTOMER_ID]_[DATE].md` - Preliminary markdown report

### Data Available for Analysis

The JSON output contains ALL data needed for phases 1-5:

| Data Key | Used In | What It Contains |
|----------|---------|------------------|
| `conversion_actions` | Phase 1 | Actions, categories, counting type |
| `campaigns` | Phase 2, 3 | Performance, status, settings |
| `ad_groups` | Phase 2, 3 | Performance, keyword themes |
| `keywords` | Phase 4 | Performance, Quality Score, components |
| `search_terms` | Phase 4 | User queries, spend, conversions |
| `negative_keywords` | Phase 4 | Existing negatives by campaign |
| `ads` | Phase 5 | RSA headlines, descriptions, strength |
| `asset_performance` | Phase 5 | Sitelinks, callouts, snippets |
| `landing_pages` | Phase 5 | URLs, performance metrics |
| `budgets` | Phase 3 | Budget amounts, delivery method |
| `bidding_strategies` | Phase 3 | Strategy type, targets |
| `impression_share` | Phase 3 | IS, IS Lost (Budget), IS Lost (Rank) |
| `auction_insights` | Phase 3 | Competitor overlap, outranking share |
| `geographic` | Phase 2 | Location targeting settings |
| `devices` | Phase 3 | Device performance breakdown |
| `change_history` | All | Recent account changes |
| `recommendations` | Phase 6 | Google's suggestions (cross-reference) |

### Credential Requirements

Credentials must be configured in `~/.mondaybrew/.env`:

```env
GOOGLE_ADS_DEVELOPER_TOKEN=xxx
GOOGLE_ADS_CLIENT_ID=xxx
GOOGLE_ADS_CLIENT_SECRET=xxx
GOOGLE_ADS_REFRESH_TOKEN=xxx
GOOGLE_ADS_LOGIN_CUSTOMER_ID=xxx
```

**If credentials are missing, the script will fail LOUDLY - this prevents hallucinated data.**

### Data Validation

After fetching, verify:
- [ ] JSON file created successfully
- [ ] `conversion_actions` array is populated (or empty if none configured)
- [ ] `campaigns` array has expected campaign count
- [ ] No error messages in script output

**Only proceed to Phase 0 after data is fetched.**

---

## Phase Overview

| Phase | Output Artifact(s) | Gate | What It Determines |
|-------|-------------------|------|-------------------|
| **0. Discovery** | `discovery_brief.md` | BLOCKS ALL | Business context, targets, what's working |
| 1. Tracking Audit | `tracking_audit.md` | BLOCKS Phase 2 | Data trustworthiness, attribution issues |
| 2. Structure Analysis | `structure_analysis.md` | BLOCKS Phase 3 | Campaign organization issues |
| 3. Performance Analysis | `performance_analysis.json` | BLOCKS Phase 4 | Budget/bid strategy issues |
| 4. Keyword Audit | `keyword_audit.json` | BLOCKS Phase 5 | Wasted spend, QS issues, negatives |
| 5. Ad Copy Audit | `ad_copy_audit.json` | BLOCKS Phase 6 | RSA quality, extensions, landing pages |
| 6. Synthesis | `recommendations.json` | BLOCKS Phase 7 | Prioritized findings, action plan |
| 7. Presentation | `audit_presentation.html` | Final | Client deliverable |

---

## Phase 0: Discovery

**Gate:** This phase MUST complete before ANY analysis begins.

### Why Discovery is Non-Negotiable

Without business context:
- A "high CPA" might be perfectly acceptable (high-value customers)
- Brand campaigns might be intentionally aggressive
- Geographic targeting might be strategic, not an error
- Recent changes might explain performance shifts

**A senior PPC specialist never interprets data without context.**

### Discovery Interview (11 Questions)

Present these questions to the user. All except Q10 are MANDATORY.

| # | Question | Variable | Why It Matters |
|---|----------|----------|----------------|
| Q1 | What are your primary business goals? (Leads, Sales, Brand) | `$PRIMARY_GOAL` | Frames entire analysis |
| Q2 | Which campaigns/services are most important to you? | `$AUDIT_FOCUS` | Prioritizes analysis depth |
| Q3 | What's working well right now? | `$WORKING_WELL` | DO NOT flag these as issues |
| Q4 | What concerns do you have about the account? | `$KNOWN_CONCERNS` | Direct investigation targets |
| Q5 | How are conversions tracked? (Forms, calls, purchases?) | `$CONVERSION_TRACKING_METHOD` | Understanding what data represents |
| Q6 | What significant changes were made in last 6 months? | `$RECENT_CHANGES` | Context for performance shifts |
| Q7 | Are there seasonal patterns in your business? | `$SEASONALITY` | Prevents misdiagnosing normal fluctuations |
| Q8 | Brand vs non-brand strategy - any intentional approach? | `$BRAND_STRATEGY` | Don't flag intentional brand bidding |
| Q9 | What's your profit margin or customer lifetime value? | `$PROFIT_MARGIN` | Contextualizes CPA recommendations |
| Q10 | Any competitors you're specifically watching? | `$COMPETITORS` | Auction insights context (optional) |
| Q11 | What would a successful audit outcome look like? | `$SUCCESS_CRITERIA` | Shapes deliverable focus |

### Inferred Variables (derive from account data)

| Variable | Source | Fallback |
|----------|--------|----------|
| `$TARGET_CPA` | Bid strategy targets OR historical performance | Ask client directly |
| `$TARGET_ROAS` | Bid strategy targets OR historical performance | Ask client directly |
| `$BUSINESS_TYPE` | Website analysis | Q1 clarification |
| `$GEO_FOCUS` | Account location targeting | Ask client |

### Website Analysis (REQUIRED)

Before the interview, fetch and analyze the client website:
- Extract business type, services/products
- Identify available landing pages
- Document conversion paths (forms, phone, chat)
- Build `$CANONICAL_SERVICES` list

### RAG Integration

```python
# Get audit methodology
methodology = get_methodology("audit")

# Query for business-type specific audit patterns
patterns = query_knowledge(
    f"Google Ads audit {business_type}",
    content_type="methodology"
)
```

### Output Artifact: `discovery_brief.md`

Use template from `templates/discovery_brief.md`. Must contain:
- All 11 answers stored as variables
- Website analysis summary
- Inferred targets (CPA/ROAS)
- `$CANONICAL_SERVICES` list
- RAG insights retrieved

### Checkpoint

Before proceeding to Phase 1, verify:
- [ ] Q1-Q9, Q11 answered (mandatory questions)
- [ ] Q10 answered (if competitors relevant)
- [ ] Website analyzed
- [ ] `$CANONICAL_SERVICES` list created
- [ ] `$TARGET_CPA` or `$TARGET_ROAS` defined
- [ ] `$WORKING_WELL` documented (protect these)
- [ ] `$BRAND_STRATEGY` documented
- [ ] `discovery_brief.md` created with all variables

**If any checkbox is incomplete: STOP. Do not proceed.**

---

## Phase 1: Conversion & Tracking Audit

**Prerequisite:** Phase 0 `discovery_brief.md` must exist.

**Purpose:** Verify data trustworthiness before analyzing performance.

> If conversion tracking is broken, every other metric is meaningless.

### Analysis Areas

1. **Conversion Actions**
   - List all conversion actions
   - Classify primary vs. secondary
   - Check if they match `$CONVERSION_TRACKING_METHOD`
   - Verify campaign-level goals align with `$PRIMARY_GOAL`

2. **Attribution Model**
   - Document current model → `$ATTRIBUTION_MODEL`
   - **Last-click = HIGH severity finding**
   - Recommend data-driven if eligible

3. **Time Lag Analysis**
   - Calculate Day 1 conversion % → `$DAY1_CONVERSION_PCT`
   - Assess account aggressiveness → `$ACCOUNT_AGGRESSIVENESS`
   - Cross-reference with `$BRAND_STRATEGY`

4. **Enhanced Conversions**
   - Check if enabled → `$ENHANCED_CONVERSIONS`
   - **If disabled for e-commerce: MEDIUM severity**

5. **Data Quality**
   - Trust level assessment → `$CONVERSION_TRUST_LEVEL`
   - 10-15% discrepancy = acceptable
   - >20% discrepancy = needs-verification

### Decision Tree: Time Lag Interpretation

| Day 1 Conversion % | Aggressiveness | Interpretation |
|-------------------|----------------|----------------|
| > 90% | conservative | Brand-heavy; check if intentional |
| 70-90% | moderate | Slightly conservative |
| 50-70% | balanced | Appropriate mix |
| < 50% | aggressive | Long consideration journey |

**Special Case:** If `$BRAND_STRATEGY` = intentional AND Day 1 > 90%:
→ Do NOT flag. Document as "expected given brand strategy."

### Output Artifact: `tracking_audit.md`

### Checkpoint

- [ ] All conversion actions documented
- [ ] `$ATTRIBUTION_MODEL` set
- [ ] `$DAY1_CONVERSION_PCT` calculated
- [ ] `$ACCOUNT_AGGRESSIVENESS` determined
- [ ] `$CONVERSION_TRUST_LEVEL` assessed
- [ ] Attribution finding created (if last-click)
- [ ] `tracking_audit.md` generated

**If `$CONVERSION_TRUST_LEVEL` = unreliable: FLAG AS CRITICAL.**

---

## Phase 2: Account Structure Analysis

**Prerequisite:** Phase 1 `tracking_audit.md` must exist.

**Purpose:** Assess organizational health and alignment with goals.

### Analysis Areas

1. **Campaign Hierarchy**
   - Count campaigns, ad groups
   - Assess fragmentation vs. consolidation
   - Check naming conventions

2. **Network Settings**
   - Display Network on Search campaigns = HIGH severity
   - Search Partners assessment

3. **Geographic Targeting**
   - Location targeting settings
   - "Presence or interest" vs "Presence only"
   - Cross-reference with `$GEO_FOCUS`

4. **Ad Group Organization**
   - Keywords per ad group (target: 3-20)
   - Theme consistency

### Decision Tree: Structure Issues

```
Campaign Count
├── 1-3 campaigns → Potentially under-segmented
├── 4-10 campaigns → Typical structure
└── 20+ campaigns → Check for budget fragmentation

Ad Group Keywords
├── < 3 keywords → Over-segmented (consolidate)
├── 3-20 keywords → Healthy range
└── 50+ keywords → Under-segmented (split)
```

### Output Artifact: `structure_analysis.md`

### Checkpoint

- [ ] Campaign hierarchy documented
- [ ] Network settings checked
- [ ] Geographic targeting reviewed
- [ ] Ad group organization assessed
- [ ] `structure_analysis.md` generated

---

## Phase 3: Campaign Performance Analysis

**Prerequisite:** Phase 2 `structure_analysis.md` must exist.

**Purpose:** Assess efficiency and identify scaling opportunities.

### Analysis Windows

- Last 30 days (recent trends)
- Last 90 days (primary analysis)
- Last 180 days (patterns/seasonality)

### Key Metrics

- Cost, Conversions, CPA, ROAS
- CTR, Conversion Rate
- Impression Share (IS)
- IS Lost (Budget), IS Lost (Rank)

### Decision Tree: Budget Analysis

```
IS Lost (Budget) vs IS Lost (Rank)

High Budget Loss, Low Rank Loss
└── Budget opportunity - can scale

Low Budget Loss, High Rank Loss
└── Efficiency issue - fix QS/bids first

Both High
└── Prioritize rank, then budget

Both Low
└── Capturing opportunity well
```

### Decision Tree: Bid Strategy Evaluation

```
Manual CPC + Any Volume
├── < 15 conversions/month → Stay manual
└── > 15 conversions/month → Test smart bidding

Target CPA + Actual > Target
└── Raise target OR improve QS OR improve CVR

Target ROAS + Constrained Spend
└── Lower ROAS target to allow more spend
```

### Output Artifact: `performance_analysis.json`

### Checkpoint

- [ ] 30/90/180 day metrics calculated
- [ ] Budget utilization analyzed
- [ ] Bid strategy effectiveness assessed
- [ ] Auction insights reviewed
- [ ] `performance_analysis.json` generated

---

## Phase 4: Keyword & Search Term Analysis

**Prerequisite:** Phase 3 `performance_analysis.json` must exist.

**Purpose:** Identify wasted spend and optimization opportunities. This is a **TENTPOLE** phase.

> "Search terms report is the heartbeat of your entire account."

### Analysis Areas

1. **Search Terms Wasted Spend**
   - Filter: Clicks >= 100 AND CPA > `$TARGET_CPA` (or zero conversions)
   - Calculate total → `$TOTAL_WASTED_SPEND`
   - Validate each term against `$CANONICAL_SERVICES`

2. **Quality Score Distribution**
   - Calculate spend-weighted QS → `$QS_WEIGHTED_AVG`
   - Flag: QS 1-3 keywords consuming significant budget
   - Document QS components (CTR, Ad Relevance, LP Experience)

3. **Negative Keyword Gaps**
   - Count negatives vs. positives → `$NEGATIVE_POSITIVE_RATIO`
   - **Target: 1:1 ratio minimum**

4. **N-Gram Analysis**
   - Run 2-gram, 3-gram analysis
   - Extract top wasting/converting patterns

### Decision Tree: Quality Score Diagnosis

| QS | Severity | Primary Issue | Action |
|----|----------|---------------|--------|
| 1 | CRITICAL | Landing page/policy | Investigate immediately |
| 2-3 | HIGH | Expected CTR | Improve ad copy |
| 4-6 | MEDIUM | Expected CTR | Systematic improvement |
| 7-8 | LOW | Minor | Maintain |
| 9-10 | NONE | Excellent | Protect |

### Decision Tree: Negative Ratio Assessment

| Ratio | Assessment | Severity |
|-------|------------|----------|
| < 0.3:1 | Severely under-protected | HIGH |
| 0.3-0.6:1 | Under-protected | MEDIUM |
| 0.6-1:1 | Moderate | LOW |
| >= 1:1 | Good | NONE |

### Output Artifact: `keyword_audit.json`

### Checkpoint

- [ ] `$TOTAL_WASTED_SPEND` calculated
- [ ] `$QS_WEIGHTED_AVG` calculated
- [ ] `$NEGATIVE_POSITIVE_RATIO` calculated
- [ ] N-gram analysis completed
- [ ] All findings have DKK impact
- [ ] `keyword_audit.json` generated

---

## Phase 5: Ad Copy & Asset Analysis

**Prerequisite:** Phase 4 `keyword_audit.json` must exist.

**Purpose:** Assess ad quality and extension utilization.

### Analysis Areas

1. **RSA Strength Distribution**
   - Headline count (target: 10-15)
   - Description count (target: 4)
   - Message diversity

2. **Extensions**
   - Sitelinks presence and performance
   - Callouts, structured snippets
   - Call extensions

3. **Landing Page Alignment**
   - URL verification (no 404s)
   - Message match with ads
   - Page speed (if accessible)

### Decision Tree: RSA Evaluation

```
Headlines
├── 1-4 headlines → CRITICAL
├── 5-9 headlines → HIGH
└── 10-15 headlines → GOOD

Descriptions
├── 1 description → CRITICAL
├── 2-3 descriptions → HIGH
└── 4 descriptions → GOOD
```

### Output Artifact: `ad_copy_audit.json`

### Checkpoint

- [ ] RSA strength documented
- [ ] Extension utilization assessed
- [ ] Landing pages verified
- [ ] All findings have severity
- [ ] `ad_copy_audit.json` generated

---

## Phase 6: Synthesis & Recommendations

**Prerequisite:** Phase 5 `ad_copy_audit.json` must exist.

**Purpose:** Consolidate findings into prioritized action plan.

### Process

1. **Aggregate all findings** from Phases 1-5
2. **Apply severity scoring** using `decision-trees/severity-scoring.md`
3. **Validate against `$WORKING_WELL`** - exclude intentional strategies
4. **Quantify DKK impact** for each finding
5. **Classify Quick Wins** (< 2hr, no dependencies, 7-day impact)
6. **Create priority action plan** (P0/P1/P2)

### Severity Levels

| Level | Criteria | Timeframe |
|-------|----------|-----------|
| CRITICAL | Blocking OR 50%+ waste | P0: Week 1 |
| HIGH | 20-50% impact | P1: Month 1 |
| MEDIUM | Improvement opportunity | P2: Months 2-3 |
| LOW | Best practice | As time permits |

### Action Plan Structure

```json
{
  "P0": { "timeframe": "Week 1", "focus": "Critical fixes" },
  "P1": { "timeframe": "Month 1", "focus": "High-impact + quick wins" },
  "P2": { "timeframe": "Months 2-3", "focus": "Strategic changes" }
}
```

### Output Artifact: `recommendations.json`

### Checkpoint

- [ ] All findings aggregated
- [ ] Each finding has severity and DKK impact
- [ ] Findings validated against `$WORKING_WELL`
- [ ] Quick wins identified
- [ ] Action plan has P0, P1, P2 items
- [ ] `recommendations.json` generated

---

## Phase 7: Presentation

**Prerequisite:** Phase 6 `recommendations.json` must exist.

**Purpose:** Generate client-ready deliverable.

### Structure

1. **Executive Summary**
   - Critical finding headline
   - Key metrics snapshot
   - Severity matrix
   - Total wasted spend / opportunity

2. **Quick Wins**
   - Immediate actions (< 2hr each)
   - Expected impact

3. **Detailed Findings**
   - By section (Tracking, Structure, Performance, Keywords, Ads)
   - Filterable by severity

4. **Priority Action Plan**
   - P0: Week 1
   - P1: Month 1
   - P2: Months 2-3

5. **Appendix**
   - Technical details
   - Full data tables

### Output Artifact: `audit_presentation.html`

Use template from `templates/audit_presentation.html`.

### Final Checkpoint

- [ ] Executive summary populated
- [ ] Quick wins listed
- [ ] All findings categorized
- [ ] Action plan complete
- [ ] `audit_presentation.html` generated

---

## RAG Integration Summary

| When | Query | Purpose |
|------|-------|---------|
| Phase 0 | `get_methodology("audit")` | Get audit methodology |
| Phase 0 | `query_knowledge("audit business type")` | Type-specific guidance |
| Phase 1 | `query_knowledge("conversion tracking audit")` | Tracking best practices |
| Phase 4 | `query_knowledge("negative keywords n-gram")` | Keyword analysis patterns |
| Phase 5 | `query_knowledge("RSA audit extensions")` | Ad copy best practices |

---

## Decision Trees Reference

- `decision-trees/severity-scoring.md` - Finding severity assignment
- `decision-trees/finding-classification.md` - Canonical finding categories
- `decision-trees/quality-score-diagnosis.md` - QS interpretation
- `decision-trees/bid-strategy-evaluation.md` - Bid strategy assessment
- `decision-trees/budget-analysis.md` - Budget opportunity analysis

---

## Canonical Finding Categories

Every finding MUST have exactly one category:

| Category ID | Phase |
|-------------|-------|
| `TRACKING_CONVERSION` | 1 |
| `TRACKING_ATTRIBUTION` | 1 |
| `TRACKING_ENHANCED` | 1 |
| `TRACKING_DATA_QUALITY` | 1 |
| `STRUCTURE_CAMPAIGN` | 2 |
| `STRUCTURE_ADGROUP` | 2 |
| `STRUCTURE_NETWORK` | 2 |
| `STRUCTURE_GEO` | 2 |
| `PERFORMANCE_BUDGET` | 3 |
| `PERFORMANCE_BID_STRATEGY` | 3 |
| `PERFORMANCE_COMPETITION` | 3 |
| `KEYWORD_QS` | 4 |
| `KEYWORD_SEARCH_TERMS` | 4 |
| `KEYWORD_NEGATIVES` | 4 |
| `ADS_RSA` | 5 |
| `ADS_EXTENSIONS` | 5 |
| `ADS_LANDING_PAGE` | 5 |

---

*Skill version: 1.0.0*
*Based on: PPC_SPECIALIST_AUDIT_FRAMEWORK.md and mb-keyword-analysis patterns*
