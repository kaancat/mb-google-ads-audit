# Google Ads Audit Plugin Architecture

## Design Based on Research Findings

This document defines the plugin architecture for `mb-google-ads-audit`, informed by deep research into PPC specialist audit methodology and patterns from the production `mb-keyword-analysis` plugin.

---

## Core Design Principles

1. **Discovery Before Diagnosis** - Cannot interpret data without business context
2. **Three Tentpoles First** - Business understanding, conversion tracking, search terms
3. **Quantify Everything** - Every finding needs DKK impact estimation
4. **Severity is Mandatory** - CRITICAL / HIGH / MEDIUM / LOW for all findings
5. **Don't Fix Intentional Strategies** - Validate assumptions with discovery
6. **Lead with Impact** - Executive summary first, details in appendices
7. **Phase Gating is Absolute** - Each phase BLOCKS the next via checkpoint validation
8. **Variable Storage Pattern** - Use `$VARIABLE_NAME` for cross-phase data access

---

## Variable Storage Pattern

Variables are stored and referenced across phases using the `$VARIABLE_NAME` convention.

### Core Variables (Set in Phase 0)

| Variable | Set In | Description |
|----------|--------|-------------|
| `$BUSINESS_TYPE` | Phase 0 | e-commerce, lead-gen, local-service, B2B, SaaS |
| `$PRIMARY_GOAL` | Phase 0 | leads, sales, brand-awareness |
| `$TARGET_CPA` | Phase 0 | Target cost per acquisition (DKK) |
| `$TARGET_ROAS` | Phase 0 | Target return on ad spend (%) |
| `$GEO_FOCUS` | Phase 0 | Geographic focus from website/interview |
| `$WORKING_WELL` | Phase 0 | List of things client says are working (DO NOT FLAG) |
| `$KNOWN_CONCERNS` | Phase 0 | List of specific concerns to investigate |
| `$BRAND_STRATEGY` | Phase 0 | intentional, opportunistic, defensive, none |
| `$PROFIT_MARGIN` | Phase 0 | Profit margin or customer LTV (contextualizes CPA) |
| `$AUDIT_FOCUS` | Phase 0 | Priority areas from interview |
| `$CANONICAL_SERVICES` | Phase 0 | List of services/products from website (single source of truth) |

### Derived Variables (Set in Analysis Phases)

| Variable | Set In | Description |
|----------|--------|-------------|
| `$CONVERSION_TRUST_LEVEL` | Phase 1 | trustworthy, needs-verification, unreliable |
| `$ATTRIBUTION_MODEL` | Phase 1 | Current attribution model |
| `$DAY1_CONVERSION_PCT` | Phase 1 | Percentage of conversions on Day 1 |
| `$ACCOUNT_AGGRESSIVENESS` | Phase 1 | conservative, moderate, balanced, aggressive |
| `$TOTAL_WASTED_SPEND` | Phase 4 | Cumulative wasted spend (DKK) |
| `$QS_WEIGHTED_AVG` | Phase 4 | Spend-weighted Quality Score average |
| `$NEGATIVE_POSITIVE_RATIO` | Phase 4 | Negative keywords : Positive keywords ratio |
| `$CRITICAL_COUNT` | Phase 6 | Number of CRITICAL findings |
| `$HIGH_COUNT` | Phase 6 | Number of HIGH findings |

---

## Workflow Architecture

### Phase Structure (7 Phases)

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 0: DISCOVERY                                              │
│  ├── Website Analysis                                            │
│  └── Discovery Interview (11 questions)                          │
│  Output: discovery_brief.md                                      │
│  GATE: Cannot proceed without completion                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: CONVERSION & TRACKING AUDIT                            │
│  ├── Conversion Actions Review                                   │
│  ├── Attribution Model Assessment                                │
│  ├── Time Lag Analysis                                           │
│  └── Data Quality Check                                          │
│  Output: tracking_audit.md                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 2: ACCOUNT STRUCTURE ANALYSIS                             │
│  ├── Campaign Hierarchy Review                                   │
│  ├── Ad Group Organization                                       │
│  ├── Naming Conventions                                          │
│  ├── Network Settings                                            │
│  └── Geographic Targeting                                        │
│  Output: structure_analysis.md                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 3: CAMPAIGN PERFORMANCE ANALYSIS                          │
│  ├── Metrics (30/90/180 day windows)                             │
│  ├── Budget Utilization                                          │
│  ├── Bid Strategy Effectiveness                                  │
│  ├── Auction Insights                                            │
│  └── Targets vs Actuals                                          │
│  Output: performance_analysis.json                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 4: KEYWORD & SEARCH TERM ANALYSIS                         │
│  ├── Quality Score Distribution (by spend)                       │
│  ├── QS Component Analysis                                       │
│  ├── Search Terms Wasted Spend                                   │
│  ├── Negative Keyword Gaps                                       │
│  ├── N-Gram Analysis                                             │
│  └── Keyword Opportunities                                       │
│  Output: keyword_audit.json                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 5: AD COPY & ASSET ANALYSIS                               │
│  ├── RSA Strength Distribution                                   │
│  ├── Headline/Description Coverage                               │
│  ├── Asset Performance Analysis                                  │
│  ├── Extension Utilization                                       │
│  └── Landing Page Alignment                                      │
│  Output: ad_copy_audit.json                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 6: SYNTHESIS & RECOMMENDATIONS                            │
│  ├── Severity Matrix Generation                                  │
│  ├── Quick Wins Extraction                                       │
│  ├── Wasted Spend Quantification                                 │
│  └── Action Plan Prioritization (P0/P1/P2)                       │
│  Output: recommendations.json                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 7: PRESENTATION                                           │
│  ├── Executive Summary                                           │
│  ├── Findings by Section                                         │
│  ├── Prioritized Action Plan                                     │
│  └── Technical Appendices                                        │
│  Output: audit_presentation.html                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Plugin Directory Structure

```
mb-google-ads-audit/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/
│   └── google-ads-audit.md      # Main /google-ads-audit command
├── skills/
│   └── google-ads-audit/
│       ├── SKILL.md             # Main skill definition
│       ├── phases/
│       │   ├── phase-0-discovery.md
│       │   ├── phase-1-tracking.md
│       │   ├── phase-2-structure.md
│       │   ├── phase-3-performance.md
│       │   ├── phase-4-keywords.md
│       │   ├── phase-5-ads.md
│       │   ├── phase-6-synthesis.md
│       │   └── phase-7-presentation.md
│       ├── decision-trees/
│       │   ├── severity-scoring.md
│       │   ├── finding-classification.md
│       │   ├── bid-strategy-evaluation.md
│       │   ├── quality-score-diagnosis.md
│       │   └── budget-analysis.md
│       ├── templates/
│       │   ├── discovery_brief.md
│       │   ├── tracking_audit.md
│       │   ├── structure_analysis.md
│       │   ├── executive_summary.md
│       │   └── presentation.html
│       └── examples/
│           └── golden_audit_example.md
├── hooks/
│   └── hooks.json               # Phase gate validation
├── research/
│   ├── PPC_SPECIALIST_AUDIT_FRAMEWORK.md
│   ├── AUDIT_CHECKLIST.md
│   └── PLUGIN_ARCHITECTURE.md   # This file
├── schemas/                     # JSON schemas for outputs
│   ├── performance_analysis.schema.json
│   ├── keyword_audit.schema.json
│   ├── ad_copy_audit.schema.json
│   └── recommendations.schema.json
├── CLAUDE.md                    # Plugin context for Claude
└── README.md                    # Documentation
```

---

## Phase Details

### Phase 0: Discovery

**Purpose:** Establish context that shapes all subsequent interpretation.

**GATE: ABSOLUTE BLOCKER**
> ⛔ **STOP. Do not proceed to Phase 1 until ALL checkboxes below are complete.**

**Inputs:**
- Website URL
- Google Ads Customer ID
- Client interview responses

**Process:**
1. Fetch and analyze website
   - Extract business type, services/products
   - Identify available landing pages
   - Document conversion paths
   - Build `$CANONICAL_SERVICES` list
2. Conduct discovery interview
   - Ask 11 questions (can be batched)
   - Clarify ambiguous responses
3. Synthesize into discovery brief with all variables set

**Discovery Questions with Variable Mapping:**

| # | Question | Variable | Required |
|---|----------|----------|----------|
| Q1 | What are your primary business goals? (Leads, Sales, Brand) | `$PRIMARY_GOAL` | ✅ MANDATORY |
| Q2 | Which campaigns/services are most important to you? | `$AUDIT_FOCUS` | ✅ MANDATORY |
| Q3 | What's working well right now? | `$WORKING_WELL` | ✅ MANDATORY |
| Q4 | What concerns do you have about the account? | `$KNOWN_CONCERNS` | ✅ MANDATORY |
| Q5 | How are conversions tracked? (Forms, calls, purchases, offline?) | `$CONVERSION_TRACKING_METHOD` | ✅ MANDATORY |
| Q6 | What significant changes were made in the last 6 months? | `$RECENT_CHANGES` | ✅ MANDATORY |
| Q7 | Are there seasonal patterns in your business? | `$SEASONALITY` | ✅ MANDATORY |
| Q8 | Brand vs non-brand strategy - any intentional approach? | `$BRAND_STRATEGY` | ✅ MANDATORY |
| Q9 | What's your profit margin or customer lifetime value? | `$PROFIT_MARGIN` | ✅ MANDATORY |
| Q10 | Any competitors you're specifically watching? | `$COMPETITORS` | Optional |
| Q11 | What would a successful audit outcome look like for you? | `$SUCCESS_CRITERIA` | ✅ MANDATORY |

**Inferred Variables (derive from website or account data):**

| Variable | Source | Fallback |
|----------|--------|----------|
| `$TARGET_CPA` | Bid strategy targets OR calculate from historical | Ask client directly |
| `$TARGET_ROAS` | Bid strategy targets OR calculate from historical | Ask client directly |
| `$BUSINESS_TYPE` | Website analysis | Q1 clarification |
| `$GEO_FOCUS` | Website + account location targeting | Ask client |

**Output:** `discovery_brief.md` (see templates/discovery_brief.md)

## Checkpoint: Phase 0 Complete

- [ ] Q1-Q9 answered (core questions - MANDATORY)
- [ ] Q10 answered (if competitors are relevant)
- [ ] Q11 answered (success criteria - MANDATORY)
- [ ] `$CANONICAL_SERVICES` list created from website (minimum 3 services)
- [ ] `$TARGET_CPA` or `$TARGET_ROAS` defined (inferred or stated)
- [ ] `$WORKING_WELL` documented (protect these in findings)
- [ ] `$BRAND_STRATEGY` documented (affects how brand campaigns are evaluated)
- [ ] discovery_brief.md generated with all variables populated

**If any checkbox is incomplete: STOP. Do not proceed to Phase 1.**

**Decision Trees:**
- None (information gathering only)

---

### Phase 1: Conversion & Tracking Audit

**Purpose:** Verify data trustworthiness before analyzing performance. The fundamental question: **"Is the data even trustworthy?"**

> ⚠️ **If conversion tracking is broken, every other metric is meaningless.**

**Inputs:**
- Account conversion actions data
- Attribution settings
- Conversion time lag data
- `$CONVERSION_TRACKING_METHOD` from Phase 0

**Variables Set in This Phase:**

| Variable | Source | Values |
|----------|--------|--------|
| `$CONVERSION_TRUST_LEVEL` | Data quality analysis | trustworthy, needs-verification, unreliable |
| `$ATTRIBUTION_MODEL` | Account settings | last-click, data-driven, position-based, etc. |
| `$DAY1_CONVERSION_PCT` | Time lag report | 0-100% |
| `$ACCOUNT_AGGRESSIVENESS` | Time lag analysis | conservative, moderate, balanced, aggressive |
| `$ENHANCED_CONVERSIONS` | Account settings | enabled, disabled |

**Analysis Areas:**
1. **Conversion Actions**
   - List all conversion actions
   - Classify primary vs. secondary
   - Check firing locations
   - Verify campaign-level goals match `$PRIMARY_GOAL`

2. **Attribution Model**
   - Document current model → `$ATTRIBUTION_MODEL`
   - **Last-click = HIGH severity finding**
   - Recommend data-driven if not in use

3. **Time Lag Analysis**
   - Calculate Day 1 conversion % → `$DAY1_CONVERSION_PCT`
   - Assess account aggressiveness → `$ACCOUNT_AGGRESSIVENESS`
   - Cross-reference with `$BRAND_STRATEGY` from Phase 0

4. **Enhanced Conversions**
   - Check if enabled → `$ENHANCED_CONVERSIONS`
   - **If disabled and e-commerce: MEDIUM severity finding**

5. **Data Quality Check**
   - Compare Google Ads conversions to CRM/backend (if available)
   - 10-15% discrepancy = acceptable
   - >20% discrepancy = `$CONVERSION_TRUST_LEVEL` = needs-verification

**Output:** `tracking_audit.md`

## Checkpoint: Phase 1 Complete

- [ ] All conversion actions documented
- [ ] `$ATTRIBUTION_MODEL` set
- [ ] `$DAY1_CONVERSION_PCT` calculated
- [ ] `$ACCOUNT_AGGRESSIVENESS` determined using decision tree below
- [ ] `$CONVERSION_TRUST_LEVEL` assessed
- [ ] Attribution finding created (if last-click)
- [ ] Enhanced conversions finding created (if disabled)
- [ ] tracking_audit.md generated

**If `$CONVERSION_TRUST_LEVEL` = unreliable: FLAG AS CRITICAL, document impact on all subsequent findings.**

---

**Decision Tree: Time Lag Interpretation → `$ACCOUNT_AGGRESSIVENESS`**

| `$DAY1_CONVERSION_PCT` | `$ACCOUNT_AGGRESSIVENESS` | Interpretation | Recommendation |
|------------------------|---------------------------|----------------|----------------|
| **> 90%** | `conservative` | Too conservative; likely brand-heavy | Cross-check with `$BRAND_STRATEGY`. If not intentional, expand non-brand. |
| **70-90%** | `moderate` | Slightly conservative | Review non-brand campaign performance |
| **50-70%** | `balanced` | Appropriate mix of brand and non-brand | No immediate action |
| **< 50%** | `aggressive` | Long consideration journey | Adjust learning period expectations; ensure sufficient conversion volume |

**Special Case:** If `$BRAND_STRATEGY` = intentional AND `$DAY1_CONVERSION_PCT` > 90%:
→ Do NOT flag as issue. Document as "expected given brand strategy."

---

### Phase 2: Account Structure Analysis

**Purpose:** Assess organizational health and alignment with goals.

**Analysis Areas:**
1. Campaign hierarchy
2. Ad group organization
3. Naming conventions
4. Network settings
5. Geographic targeting

**Output:** `structure_analysis.md`

**Decision Tree: Structure Issues**
```
Campaign Count per Account
├── 1-3 campaigns, many ad groups → Potentially under-segmented
├── 4-10 campaigns → Typical structure
└── 20+ campaigns → Potentially over-segmented
    └── Check: Are budgets fragmented?

Ad Group Keywords
├── < 3 keywords → Over-segmented (consolidate)
├── 3-20 keywords → Healthy range
└── 50+ keywords → Under-segmented (split by theme)
```

---

### Phase 3: Campaign Performance Analysis

**Purpose:** Assess efficiency and identify scaling opportunities.

**Analysis Windows:**
- Last 30 days (recent trends)
- Last 90 days (primary analysis)
- Last 180 days (patterns/seasonality)

**Key Metrics:**
- Cost, Conversions, CPA, ROAS
- CTR, Conversion Rate
- Impression Share (IS)
- IS Lost (Budget), IS Lost (Rank)

**Output:** `performance_analysis.json`

**Decision Tree: Budget Analysis**
```
IS Lost (Budget) vs IS Lost (Rank)

High IS Lost (Budget), Low IS Lost (Rank)
└── Budget opportunity - can scale with more budget

Low IS Lost (Budget), High IS Lost (Rank)
└── Efficiency issue - fix QS/bids before adding budget

Both High
└── Prioritize rank first, then budget

Both Low
└── Capturing available opportunity well
```

**Decision Tree: Bid Strategy Evaluation**
```
Current Bid Strategy + Data Volume

Manual CPC + Any Volume
└── Consider: Is there enough data for smart bidding?
    ├── < 15 conversions/month → Stay manual
    └── > 15 conversions/month → Test target CPA/ROAS

Target CPA + Low Volume
└── Check: Daily budget vs target CPA
    ├── Budget < 10x CPA → Insufficient budget
    └── Budget > 10x CPA → May need more time

Target CPA + High Volume, Actual > Target
└── Options:
    ├── Raise target (more aggressive)
    ├── Improve conversion rate
    └── Improve Quality Score

Target ROAS + Constrained Spend
└── Target may be too aggressive
    └── Lower ROAS target to allow more spend
```

---

### Phase 4: Keyword & Search Term Analysis

**Purpose:** Identify wasted spend and optimization opportunities. This is a **TENTPOLE** phase.

> 💡 **"Search terms report is the heartbeat of your entire account. That's what you're spending your money on."**

**Inputs:**
- Keyword data with Quality Score
- Search terms report (90+ days)
- Negative keyword lists (account and campaign level)
- `$TARGET_CPA` from Phase 0
- `$CANONICAL_SERVICES` from Phase 0

**Variables Set in This Phase:**

| Variable | Source | Description |
|----------|--------|-------------|
| `$TOTAL_WASTED_SPEND` | Search terms analysis | Sum of spend on irrelevant/non-converting terms |
| `$QS_WEIGHTED_AVG` | Keyword analysis | Spend-weighted Quality Score average |
| `$NEGATIVE_POSITIVE_RATIO` | Keyword counts | Negative keywords : Positive keywords ratio |
| `$TOP_WASTING_TERMS` | N-gram analysis | Top 10 wasting search term patterns |
| `$TOP_CONVERTING_TERMS` | N-gram analysis | Top 10 converting search term patterns |

**Analysis Areas:**

1. **Search Terms Wasted Spend Analysis**
   - Filter: `Clicks >= 100 AND CPA > $TARGET_CPA` (or no conversions)
   - Calculate: Total wasted spend → `$TOTAL_WASTED_SPEND`
   - Validate each term against `$CANONICAL_SERVICES`
   - Cross-reference with `$WORKING_WELL` (don't flag intentional)

2. **Quality Score Distribution (by spend)**
   - Calculate spend-weighted QS average → `$QS_WEIGHTED_AVG`
   - Flag: Keywords with QS 1-3 consuming significant budget
   - Document QS components for each low-QS keyword

3. **Negative Keyword Gaps**
   - Count current negatives vs. positives → `$NEGATIVE_POSITIVE_RATIO`
   - **Target: 1:1 ratio minimum**
   - Identify obvious missing negatives from search terms

4. **N-Gram Analysis**
   - Export search term data
   - Run n-gram analysis (2-gram, 3-gram)
   - Extract → `$TOP_WASTING_TERMS`, `$TOP_CONVERTING_TERMS`

**Output:** `keyword_audit.json`

## Checkpoint: Phase 4 Complete

- [ ] `$TOTAL_WASTED_SPEND` calculated
- [ ] `$QS_WEIGHTED_AVG` calculated
- [ ] `$NEGATIVE_POSITIVE_RATIO` calculated
- [ ] N-gram analysis completed
- [ ] All wasted spend findings have DKK impact
- [ ] Each irrelevant search term validated against `$CANONICAL_SERVICES`
- [ ] Negative keyword recommendations generated
- [ ] keyword_audit.json generated

---

**Decision Tree: Quality Score Diagnosis**

| QS Score | Severity | Primary Issue (Check First) | Secondary Check | Action |
|----------|----------|----------------------------|-----------------|--------|
| **1** | `CRITICAL` | Landing page (policy/relevance) | Often account-level issue | Investigate immediately - may not be serving |
| **2-3** | `HIGH` | Expected CTR (65% weight) | Ad relevance (25%) | Improve ad copy, test new headlines |
| **4-6** | `MEDIUM` | Expected CTR | Landing page (10%) | Systematic improvement - CTR focus |
| **7-8** | `LOW` | None - good performance | Minor optimizations | Maintain, don't change unnecessarily |
| **9-10** | `NONE` | Excellent | Protect this keyword | Do NOT change |

**QS Component Weights (for diagnosis prioritization):**
- Expected CTR: ~65% of QS weight → Fix first
- Ad Relevance: ~25% of QS weight → Fix second
- Landing Page Experience: ~10% of QS weight → Fix third

---

**Decision Tree: Search Term Action**

```
For each search term with significant spend (100+ clicks OR $500+ DKK):

Step 1: Relevance Check
├── Is term relevant to $CANONICAL_SERVICES?
│   ├── NO → NEGATIVE KEYWORD (exact match)
│   │   └── Severity: Based on spend level
│   └── YES → Continue to Step 2

Step 2: Performance Check
├── Is CPA ≤ $TARGET_CPA (or has conversions)?
│   ├── YES → KEEP
│   │   └── Consider: Expand as positive keyword?
│   └── NO → Continue to Step 3

Step 3: Intent Check
├── Does term show purchase/action intent?
│   ├── NO → NEGATIVE KEYWORD (phrase match)
│   │   └── Examples: "free", "DIY", "how to" with no conversions
│   └── YES → Continue to Step 4

Step 4: Optimization Options
└── Term is relevant + has good intent + poor performance
    ├── Option A: Lower bids on this term
    ├── Option B: Improve Quality Score
    ├── Option C: Test different ad copy
    └── Option D: Improve landing page relevance
```

---

**Decision Tree: Negative Keyword Ratio Assessment**

| `$NEGATIVE_POSITIVE_RATIO` | Assessment | Severity | Action |
|----------------------------|------------|----------|--------|
| **< 0.3:1** | Severely under-protected | `HIGH` | Urgent negative keyword audit needed |
| **0.3-0.6:1** | Under-protected | `MEDIUM` | Negative keyword audit recommended |
| **0.6-1:1** | Moderate protection | `LOW` | Review for gaps |
| **≥ 1:1** | Good protection | `NONE` | Maintain, check for over-blocking |

> 💡 **"I have never seen a profitable account that did not have a serious negative keyword strategy."**

---

### Phase 5: Ad Copy & Asset Analysis

**Purpose:** Assess ad quality and extension utilization.

**Analysis Areas:**
1. RSA strength distribution
2. Headline count (target: 10-15)
3. Description count (target: 4)
4. Message diversity
5. Extension presence and performance
6. Landing page alignment

**Output:** `ad_copy_audit.json`

**Decision Tree: RSA Evaluation**
```
RSA Completeness

Headlines
├── 1-4 headlines → CRITICAL - Severely under-filled
├── 5-9 headlines → HIGH - Should add more
├── 10-15 headlines → GOOD
└── Check diversity: Are messages varied?

Descriptions
├── 1 description → CRITICAL
├── 2-3 descriptions → HIGH
└── 4 descriptions → GOOD
```

**Decision Tree: Asset Performance**
```
Asset Performance Filter

Clicks > 300 AND Conversions < 3
└── HIGH - Underperforming asset consuming budget
    └── Evaluate: Pause, replace, or optimize

Clicks > 1000 AND CPA > 2x target
└── MEDIUM - Significant investment, poor return
    └── Deep dive into why

High impressions, low CTR
└── MEDIUM - Ad copy/relevance issue
```

---

### Phase 6: Synthesis & Recommendations

**Purpose:** Consolidate findings into prioritized action plan.

**Inputs:**
- All findings from Phases 1-5
- `$TOTAL_WASTED_SPEND` from Phase 4
- `$SUCCESS_CRITERIA` from Phase 0
- `$WORKING_WELL` from Phase 0 (to protect)

**Variables Set in This Phase:**

| Variable | Source | Description |
|----------|--------|-------------|
| `$CRITICAL_COUNT` | Finding aggregation | Number of CRITICAL findings |
| `$HIGH_COUNT` | Finding aggregation | Number of HIGH findings |
| `$MEDIUM_COUNT` | Finding aggregation | Number of MEDIUM findings |
| `$LOW_COUNT` | Finding aggregation | Number of LOW findings |
| `$QUICK_WINS_COUNT` | Finding filter | Number of quick win opportunities |
| `$TOTAL_IMPACT_DKK` | Sum of all findings | Total estimated DKK impact |

**Process:**
1. Aggregate all findings from phases 1-5
2. Apply severity scoring using decision tree below
3. Validate findings against `$WORKING_WELL` (remove if intentional)
4. Quantify DKK impact for each finding
5. Categorize as Quick Win / Strategic / Optimization
6. Create priority action plan

**Output:** `recommendations.json`

---

## Canonical Finding Categories

> **These are the ONLY valid categories for findings. Each finding MUST have exactly one category.**

| Category ID | Category Name | Phase | Description |
|-------------|---------------|-------|-------------|
| `TRACKING_CONVERSION` | Conversion Tracking | 1 | Conversion action setup issues |
| `TRACKING_ATTRIBUTION` | Attribution Model | 1 | Attribution model issues |
| `TRACKING_ENHANCED` | Enhanced Conversions | 1 | Enhanced conversion settings |
| `TRACKING_DATA_QUALITY` | Data Quality | 1 | Conversion data discrepancies |
| `STRUCTURE_CAMPAIGN` | Campaign Structure | 2 | Campaign organization issues |
| `STRUCTURE_ADGROUP` | Ad Group Structure | 2 | Ad group organization issues |
| `STRUCTURE_NETWORK` | Network Settings | 2 | Search partners, display on search |
| `STRUCTURE_GEO` | Geographic Targeting | 2 | Location targeting issues |
| `PERFORMANCE_BUDGET` | Budget Utilization | 3 | Limited by budget, budget allocation |
| `PERFORMANCE_BID_STRATEGY` | Bid Strategy | 3 | Bid strategy effectiveness |
| `PERFORMANCE_COMPETITION` | Competition | 3 | Auction insights, impression share |
| `KEYWORD_QS` | Quality Score | 4 | Quality Score issues |
| `KEYWORD_SEARCH_TERMS` | Search Terms | 4 | Wasted spend on search terms |
| `KEYWORD_NEGATIVES` | Negative Keywords | 4 | Negative keyword gaps |
| `ADS_RSA` | RSA Quality | 5 | Headline/description issues |
| `ADS_EXTENSIONS` | Extensions | 5 | Missing or underperforming extensions |
| `ADS_LANDING_PAGE` | Landing Pages | 5 | Landing page alignment issues |

---

## Severity Scoring Decision Tree

**Step 1: Determine Base Severity**

| Condition | Base Severity |
|-----------|---------------|
| Blocking optimization (no conversion tracking, broken URLs) | `CRITICAL` |
| Spend waste ≥ 50% of budget | `CRITICAL` |
| Spend waste 20-50% of budget | `HIGH` |
| Significant tracking issue affecting all data | `HIGH` |
| Improvement opportunity with measurable impact | `MEDIUM` |
| Best practice, nice to have | `LOW` |

**Step 2: Apply DKK Threshold Modifiers**

| Monthly Impact | Modifier |
|----------------|----------|
| > 10,000 DKK | +1 severity level (max CRITICAL) |
| 5,000 - 10,000 DKK | No change |
| 1,000 - 5,000 DKK | No change |
| < 1,000 DKK | -1 severity level (min LOW) |

**Step 3: Check Against `$WORKING_WELL`**

```
Is this finding related to something in $WORKING_WELL?
├── YES → REMOVE FINDING (do not include in report)
│   └── Document: "Excluded per client indication this is working/intentional"
└── NO → Keep finding with calculated severity
```

**Step 4: Quick Win Classification**

A finding is a "Quick Win" if ALL of the following:
- Implementation time < 2 hours
- No external dependencies (client approval, external tools)
- Measurable impact within 7 days
- Severity is HIGH or MEDIUM

---

## Action Plan Priority Assignment

| Priority | Timeframe | Criteria | Examples |
|----------|-----------|----------|----------|
| **P0** | Week 1 | CRITICAL findings OR blocking issues | No conversion tracking, 404 landing pages, massive wasted spend |
| **P1** | Month 1 | HIGH findings + Quick Wins | Negative keyword gaps, attribution model, low QS keywords |
| **P2** | Months 2-3 | MEDIUM/LOW findings + Strategic changes | Extension additions, bid strategy tests, structure reorganization |

**Action Plan Structure:**
```json
{
  "P0_immediate": {
    "timeframe": "Week 1",
    "focus": "Critical fixes, stop the bleeding",
    "severity_filter": ["CRITICAL"],
    "items": []
  },
  "P1_short_term": {
    "timeframe": "Month 1",
    "focus": "High-impact optimizations, quick wins",
    "severity_filter": ["HIGH", "QUICK_WIN"],
    "items": []
  },
  "P2_medium_term": {
    "timeframe": "Months 2-3",
    "focus": "Strategic changes, testing framework",
    "severity_filter": ["MEDIUM", "LOW"],
    "items": []
  }
}
```

## Checkpoint: Phase 6 Complete

- [ ] All findings from Phases 1-5 aggregated
- [ ] Each finding has severity assigned using decision tree
- [ ] Each finding has DKK impact estimated
- [ ] Each finding has exactly one category from canonical list
- [ ] Findings cross-referenced against `$WORKING_WELL`
- [ ] `$CRITICAL_COUNT`, `$HIGH_COUNT`, `$MEDIUM_COUNT`, `$LOW_COUNT` calculated
- [ ] Quick wins identified and counted
- [ ] `$TOTAL_IMPACT_DKK` calculated
- [ ] Action plan has items in P0, P1, AND P2 categories
- [ ] recommendations.json generated

---

### Phase 7: Presentation

**Purpose:** Generate client-ready deliverable.

**Output:** `audit_presentation.html`

**Structure:**
1. Executive Summary
   - Critical finding headline
   - Key metrics snapshot
   - Severity matrix summary
   - Total wasted spend / opportunity

2. Account Overview
   - Account structure visual
   - Campaign summary table
   - Performance trends

3. Findings by Section
   - Tracking & Attribution
   - Account Structure
   - Performance
   - Keywords & Search Terms
   - Ads & Assets

4. Priority Action Plan
   - P0: Immediate (Week 1)
   - P1: Short-term (Month 1)
   - P2: Medium-term (Months 2-3)

5. Technical Appendices
   - Full negative keyword recommendations
   - Keyword additions
   - Detailed metrics tables
   - Supporting data

---

## Hooks Configuration

**hooks.json:**
```json
{
  "hooks": [
    {
      "event": "phase_transition",
      "from": "discovery",
      "to": "tracking",
      "condition": "discovery_brief_complete",
      "on_fail": "Cannot proceed to analysis without completing discovery interview."
    },
    {
      "event": "finding_created",
      "action": "require_severity",
      "on_fail": "All findings must have a severity rating (CRITICAL/HIGH/MEDIUM/LOW)."
    },
    {
      "event": "finding_created",
      "action": "require_impact",
      "on_fail": "All findings should include estimated DKK impact."
    },
    {
      "event": "phase_complete",
      "phase": "synthesis",
      "action": "validate_action_plan",
      "on_fail": "Action plan must have items in P0, P1, and P2 categories."
    }
  ]
}
```

---

## MCP RAG Integration

**Tools to Use:**

```javascript
// Before starting any phase
query_knowledge("audit [topic]", n_results=10)

// For specific methodology
get_methodology("audit")

// For deliverable format
get_deliverable_schema("audit")

// Example usage in phases:

// Phase 4: Keywords
query_knowledge("negative keywords n-gram analysis wasted spend")
query_knowledge("Quality Score diagnosis optimization")

// Phase 5: Ads
query_knowledge("RSA responsive search ads headlines descriptions")
query_knowledge("sitelinks callouts extensions audit")

// Phase 3: Performance
query_knowledge("bid strategy target CPA target ROAS evaluation")
query_knowledge("auction insights impression share competition")
```

---

## Schema Definitions

### performance_analysis.schema.json
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["audit_period", "campaigns", "overall_metrics", "budget_analysis", "bid_strategy_analysis"],
  "properties": {
    "audit_period": {
      "type": "object",
      "properties": {
        "start_date": { "type": "string", "format": "date" },
        "end_date": { "type": "string", "format": "date" },
        "days": { "type": "integer" }
      }
    },
    "campaigns": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string" },
          "status": { "type": "string" },
          "metrics_30d": { "$ref": "#/definitions/metrics" },
          "metrics_90d": { "$ref": "#/definitions/metrics" },
          "metrics_180d": { "$ref": "#/definitions/metrics" },
          "limited_by_budget": { "type": "boolean" },
          "is_lost_budget_pct": { "type": "number" },
          "is_lost_rank_pct": { "type": "number" }
        }
      }
    },
    "overall_metrics": { "$ref": "#/definitions/metrics" },
    "budget_analysis": {
      "type": "object",
      "properties": {
        "total_daily_budget": { "type": "number" },
        "campaigns_limited_by_budget": { "type": "array" },
        "budget_opportunity_dkk": { "type": "number" }
      }
    },
    "bid_strategy_analysis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "campaign": { "type": "string" },
          "strategy": { "type": "string" },
          "target": { "type": "number" },
          "actual": { "type": "number" },
          "assessment": { "type": "string" }
        }
      }
    }
  },
  "definitions": {
    "metrics": {
      "type": "object",
      "properties": {
        "cost": { "type": "number" },
        "conversions": { "type": "number" },
        "cpa": { "type": "number" },
        "roas": { "type": "number" },
        "clicks": { "type": "integer" },
        "impressions": { "type": "integer" },
        "ctr": { "type": "number" },
        "conversion_rate": { "type": "number" },
        "impression_share": { "type": "number" }
      }
    }
  }
}
```

### recommendations.schema.json
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["findings", "action_plan", "summary", "metadata"],
  "properties": {
    "metadata": {
      "type": "object",
      "required": ["audit_date", "customer_id", "audit_period_days"],
      "properties": {
        "audit_date": { "type": "string", "format": "date" },
        "customer_id": { "type": "string" },
        "audit_period_days": { "type": "integer" },
        "business_type": {
          "type": "string",
          "enum": ["e-commerce", "lead-gen", "local-service", "B2B", "SaaS"],
          "description": "From $BUSINESS_TYPE variable"
        },
        "target_cpa": { "type": "number", "description": "From $TARGET_CPA variable (DKK)" },
        "target_roas": { "type": "number", "description": "From $TARGET_ROAS variable (%)" }
      }
    },
    "summary": {
      "type": "object",
      "required": ["total_wasted_spend_dkk", "critical_count", "high_count", "medium_count", "low_count"],
      "properties": {
        "total_wasted_spend_dkk": {
          "type": "number",
          "description": "From $TOTAL_WASTED_SPEND - cumulative DKK wasted in audit period"
        },
        "critical_count": { "type": "integer", "description": "From $CRITICAL_COUNT" },
        "high_count": { "type": "integer", "description": "From $HIGH_COUNT" },
        "medium_count": { "type": "integer", "description": "From $MEDIUM_COUNT" },
        "low_count": { "type": "integer", "description": "From $LOW_COUNT" },
        "quick_wins_count": { "type": "integer", "description": "From $QUICK_WINS_COUNT" },
        "total_impact_dkk": { "type": "number", "description": "From $TOTAL_IMPACT_DKK" }
      }
    },
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "title", "severity", "category", "description", "recommendation", "priority"],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^F[0-9]{3}$",
            "description": "Finding ID in format F001, F002, etc."
          },
          "title": {
            "type": "string",
            "maxLength": 100,
            "description": "Clear, action-oriented title. Example: 'No conversion tracking configured'"
          },
          "severity": {
            "type": "string",
            "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
            "description": "CRITICAL: Blocking/50%+ waste. HIGH: 20%+ impact. MEDIUM: Opportunity. LOW: Nice to have."
          },
          "category": {
            "type": "string",
            "enum": [
              "TRACKING_CONVERSION", "TRACKING_ATTRIBUTION", "TRACKING_ENHANCED", "TRACKING_DATA_QUALITY",
              "STRUCTURE_CAMPAIGN", "STRUCTURE_ADGROUP", "STRUCTURE_NETWORK", "STRUCTURE_GEO",
              "PERFORMANCE_BUDGET", "PERFORMANCE_BID_STRATEGY", "PERFORMANCE_COMPETITION",
              "KEYWORD_QS", "KEYWORD_SEARCH_TERMS", "KEYWORD_NEGATIVES",
              "ADS_RSA", "ADS_EXTENSIONS", "ADS_LANDING_PAGE"
            ],
            "description": "MUST be from canonical finding categories. See PLUGIN_ARCHITECTURE.md"
          },
          "description": {
            "type": "string",
            "description": "Detailed description of the issue with supporting data"
          },
          "impact_dkk": {
            "type": "number",
            "minimum": 0,
            "description": "Estimated monthly DKK impact. REQUIRED for CRITICAL/HIGH findings."
          },
          "evidence": {
            "type": "string",
            "description": "Specific data supporting this finding. Example: '12 search terms, 500+ clicks, 0 conversions'"
          },
          "recommendation": {
            "type": "string",
            "description": "Specific, actionable recommendation"
          },
          "priority": {
            "type": "string",
            "enum": ["P0", "P1", "P2"],
            "description": "P0: Week 1. P1: Month 1. P2: Months 2-3."
          },
          "is_quick_win": {
            "type": "boolean",
            "description": "True if: <2hr implementation, no dependencies, measurable impact within 7 days"
          },
          "validation_status": {
            "type": "string",
            "enum": ["CONFIRMED", "EXCLUDED_INTENTIONAL", "NEEDS_VERIFICATION"],
            "description": "EXCLUDED_INTENTIONAL = related to $WORKING_WELL, was removed from findings"
          }
        }
      }
    },
    "action_plan": {
      "type": "object",
      "required": ["P0", "P1", "P2"],
      "properties": {
        "P0": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["finding_id", "action", "owner"],
            "properties": {
              "finding_id": { "type": "string", "pattern": "^F[0-9]{3}$" },
              "action": { "type": "string" },
              "owner": { "type": "string", "enum": ["client", "agency", "both"] }
            }
          },
          "description": "Week 1 actions - CRITICAL findings only"
        },
        "P1": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["finding_id", "action", "owner"],
            "properties": {
              "finding_id": { "type": "string", "pattern": "^F[0-9]{3}$" },
              "action": { "type": "string" },
              "owner": { "type": "string", "enum": ["client", "agency", "both"] }
            }
          },
          "description": "Month 1 actions - HIGH findings + Quick Wins"
        },
        "P2": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["finding_id", "action", "owner"],
            "properties": {
              "finding_id": { "type": "string", "pattern": "^F[0-9]{3}$" },
              "action": { "type": "string" },
              "owner": { "type": "string", "enum": ["client", "agency", "both"] }
            }
          },
          "description": "Months 2-3 actions - MEDIUM/LOW findings + Strategic"
        }
      }
    },
    "excluded_findings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "reason": { "type": "string", "description": "Why it was excluded - reference to $WORKING_WELL item" }
        }
      },
      "description": "Findings that were identified but excluded because they match $WORKING_WELL"
    }
  }
}
```

---

## Implementation Notes

### Data Extraction Requirements

**From Google Ads API (via existing backend services):**

| Data | API Resource | Purpose |
|------|--------------|---------|
| Account settings | Customer | Basic account info |
| Conversion actions | ConversionAction | Tracking audit |
| Campaigns + metrics | Campaign | Performance analysis |
| Ad groups + metrics | AdGroup | Structure analysis |
| Keywords + QS | KeywordView | Keyword audit |
| Search terms | SearchTermView | Wasted spend analysis |
| Ads + RSA data | Ad | Ad copy audit |
| Assets/Extensions | Asset, CampaignAsset | Extension audit |
| Auction insights | AuctionInsights | Competition analysis |
| Geographic data | GeographicView | Geo analysis |
| Device data | N/A (segments) | Device analysis |

### Dependencies

- `backend/services/ads_connector.py` - Google Ads API wrapper
- `backend/scripts/audit_account.py` - Existing audit data fetching
- MCP RAG tools for methodology guidance

---

## Next Steps

1. [ ] Create `SKILL.md` main skill definition
2. [ ] Create phase-specific prompt files
3. [ ] Implement decision tree files
4. [ ] Create output templates
5. [ ] Implement hooks.json validation
6. [ ] Create JSON schemas for outputs
7. [ ] Build presentation template
8. [ ] Test with sample account data
9. [ ] Iterate based on real audit results

---

*This architecture is designed to be implemented incrementally. Start with Phase 0 and the core skill definition, then build out subsequent phases.*
