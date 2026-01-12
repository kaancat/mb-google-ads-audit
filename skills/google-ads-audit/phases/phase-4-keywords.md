# Phase 4: Keyword & Search Term Analysis

**Status:** TENTPOLE Phase - Critical for Wasted Spend Identification

## Purpose

Identify wasted spend and optimization opportunities in keywords and search terms. This is a **TENTPOLE** phase because:

> **"Search terms report is the heartbeat of your entire account. That's what you're spending your money on."**

This phase directly quantifies `$TOTAL_WASTED_SPEND` - often the most impactful finding in the entire audit.

---

## Prerequisites

- Phase 0 completed with `discovery_brief.md` generated
- Phase 1 completed with `tracking_audit.md` generated
- Phase 2 completed with `structure_analysis.md` generated
- Phase 3 completed with `performance_analysis.json` generated
- `$TARGET_CPA` from Phase 0
- `$CANONICAL_SERVICES` from Phase 0 (for relevance validation)
- `$WORKING_WELL` from Phase 0 (don't flag intentional)

---

## Inputs Required

1. **Keyword data** - All keywords with Quality Score components
2. **Search terms report** - 90+ days of search term data
3. **Negative keyword lists** - Account and campaign level
4. **`$CANONICAL_SERVICES`** - For relevance checking
5. **`$TARGET_CPA`** - For performance thresholds

---

## Variables Set in This Phase

| Variable | Source | Description |
|----------|--------|-------------|
| `$TOTAL_WASTED_SPEND` | Search terms analysis | Sum of spend on irrelevant/non-converting terms (DKK) |
| `$QS_WEIGHTED_AVG` | Keyword analysis | Spend-weighted Quality Score average |
| `$NEGATIVE_POSITIVE_RATIO` | Keyword counts | Negative keywords : Positive keywords ratio |
| `$TOP_WASTING_TERMS` | N-gram analysis | Top 10 wasting search term patterns |
| `$TOP_CONVERTING_TERMS` | N-gram analysis | Top 10 converting search term patterns |

---

## Step 1: Quality Score Distribution Analysis

### Fetch and Calculate

For all enabled keywords with impressions:
- Quality Score (1-10 or null)
- Expected CTR component (Above average / Average / Below average)
- Ad Relevance component
- Landing Page Experience component
- Spend
- Clicks
- Conversions

### Calculate Spend-Weighted QS Average

```
$QS_WEIGHTED_AVG = Σ(QS × Spend) / Σ(Spend)

Only include keywords where QS is not null.
```

### Decision Tree: Quality Score Diagnosis

| QS Score | Severity | Primary Issue | Action |
|----------|----------|---------------|--------|
| **1** | `CRITICAL` | Usually policy/landing page | Investigate immediately |
| **2-3** | `HIGH` | Expected CTR (fix first) | Improve ad copy, test headlines |
| **4-6** | `MEDIUM` | Expected CTR | Systematic improvement |
| **7-8** | `LOW` | Good performance | Maintain, minor tweaks |
| **9-10** | `NONE` | Excellent | Protect - don't change |

### QS Component Diagnosis Priority

When diagnosing low QS keywords, prioritize by component weight:

1. **Expected CTR (~65% of QS weight)** → Fix first
2. **Ad Relevance (~25% of QS weight)** → Fix second
3. **Landing Page Experience (~10% of QS weight)** → Fix third

### QS Distribution by Spend

Create distribution table:

| QS Band | Keyword Count | Spend (DKK) | Spend % |
|---------|--------------|-------------|---------|
| QS 1 | X | X | X% |
| QS 2-3 | X | X | X% |
| QS 4-6 | X | X | X% |
| QS 7-8 | X | X | X% |
| QS 9-10 | X | X | X% |
| QS null | X | X | X% |

**Finding Triggers:**
- QS 1-3 consuming >20% of spend = **HIGH**
- QS 4-6 consuming >50% of spend = **MEDIUM**
- QS null on high-spend keywords = **MEDIUM** (investigate)

---

## Step 2: Search Terms Wasted Spend Analysis

### Filter for Analysis

Pull search terms with significant spend:
- Clicks >= 10 OR
- Spend >= 500 DKK OR
- Part of n-gram pattern

### Decision Tree: Search Term Action

```
For each search term with significant spend:

Step 1: RELEVANCE CHECK
├── Is term relevant to $CANONICAL_SERVICES?
│   ├── NO → NEGATIVE KEYWORD
│   │   └── Match type: exact (specific) or phrase (pattern)
│   │   └── Add spend to $TOTAL_WASTED_SPEND
│   │
│   └── YES → Continue to Step 2

Step 2: PERFORMANCE CHECK
├── Has conversions at acceptable CPA?
│   ├── CPA <= $TARGET_CPA → KEEP
│   │   └── Consider: Add as positive keyword?
│   │
│   └── CPA > $TARGET_CPA or 0 conversions → Continue to Step 3

Step 3: INTENT CHECK
├── Does term show purchase/action intent?
│   ├── NO → NEGATIVE KEYWORD (phrase)
│   │   └── Examples: "free", "DIY", "how to", "jobs"
│   │   └── Add spend to $TOTAL_WASTED_SPEND
│   │
│   └── YES → Continue to Step 4

Step 4: OPTIMIZATION OPTIONS (relevant + intent + poor performance)
└── Options:
    ├── Lower bids on triggering keyword
    ├── Improve Quality Score
    ├── Test different ad copy
    └── Improve landing page relevance
```

### Validation Against $CANONICAL_SERVICES

**CRITICAL:** Every search term flagged as irrelevant MUST be validated against `$CANONICAL_SERVICES`:

```
If search term contains words from $CANONICAL_SERVICES:
    → Likely relevant, investigate further
    → Don't automatically flag as waste

If search term is completely unrelated to all services:
    → Flag as waste
    → Add to negative keyword recommendations
```

### Cross-Reference with $WORKING_WELL

```
Before flagging any search term pattern:
├── Is it mentioned in $WORKING_WELL?
│   └── YES → Do NOT flag
│       └── Client explicitly said this is working
│
└── NO → Proceed with flagging
```

---

## Step 3: Negative Keyword Analysis

### Count Current Negatives

| Level | Count |
|-------|-------|
| Account-level negatives | X |
| Campaign-level negatives | X |
| **Total negatives** | X |
| **Total positive keywords** | X |

### Calculate Ratio

```
$NEGATIVE_POSITIVE_RATIO = Total negatives / Total positives
```

### Decision Tree: Negative Keyword Ratio Assessment

| Ratio | Assessment | Severity | Action |
|-------|------------|----------|--------|
| **< 0.3:1** | Severely under-protected | `HIGH` | Urgent negative audit needed |
| **0.3-0.6:1** | Under-protected | `MEDIUM` | Negative audit recommended |
| **0.6-1:1** | Moderate protection | `LOW` | Review for gaps |
| **≥ 1:1** | Good protection | `NONE` | Check for over-blocking |

> **"I have never seen a profitable account that did not have a serious negative keyword strategy."**

### Generate Negative Keyword Recommendations

From wasted spend analysis, create list of recommended negatives:

| Keyword | Match Type | Scope | Reason | Est. Savings (DKK) |
|---------|------------|-------|--------|-------------------|
| [keyword] | exact/phrase | account/campaign | [reason] | [spend saved] |

---

## Step 4: N-Gram Analysis

### Process

1. Export all search terms with metrics
2. Break into 2-grams and 3-grams
3. Aggregate metrics by n-gram
4. Identify patterns

### Top Wasting Patterns → `$TOP_WASTING_TERMS`

Find n-grams with:
- High spend
- Low/no conversions
- Poor CPA

Example output:
```
Pattern: "free [service]"
Occurrences: 45 search terms
Total Spend: 12,500 DKK
Total Conversions: 0
Recommendation: Add "free" as account-level negative
```

### Top Converting Patterns → `$TOP_CONVERTING_TERMS`

Find n-grams with:
- Good conversion rate
- CPA below target
- Consistent performance

Example output:
```
Pattern: "[service] pris" (price)
Occurrences: 28 search terms
Total Spend: 8,200 DKK
Total Conversions: 35
CPA: 234 DKK
Recommendation: Ensure coverage, consider dedicated ad group
```

---

## Step 5: Calculate Total Wasted Spend

### Sum All Wasted Spend Sources

```
$TOTAL_WASTED_SPEND =
    SUM(spend on irrelevant search terms) +
    SUM(spend on low-intent terms with 0 conversions) +
    SUM(spend on terms with CPA > 3x target and no strategic value)
```

**This is often the single most impactful finding in the entire audit.**

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get keyword analysis methodology
keyword_guidance = query_knowledge(
    "keyword Quality Score search terms wasted spend",
    content_type="methodology"
)

# Get negative keyword best practices
negative_guidance = query_knowledge(
    "negative keywords n-gram analysis protection",
    content_type="best_practice"
)

# If QS issues found
if avg_qs < 5:
    qs_guidance = query_knowledge(
        "Quality Score improvement expected CTR ad relevance",
        content_type="methodology"
    )
```

---

## Findings Generation

For each issue identified, create a finding with:

| Field | Value |
|-------|-------|
| `id` | F00X (continue from Phase 3) |
| `title` | Action-oriented title |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `category` | One of: `KEYWORD_QS`, `KEYWORD_SEARCH_TERMS`, `KEYWORD_NEGATIVES` |
| `description` | Detailed explanation with data |
| `impact_dkk` | **REQUIRED** - Quantified wasted spend |
| `evidence` | Specific search terms/keywords |
| `recommendation` | Specific action to take |

### Common Findings for This Phase

| Issue | Category | Severity | Example |
|-------|----------|----------|---------|
| Massive wasted spend | `KEYWORD_SEARCH_TERMS` | CRITICAL | "X DKK spent on irrelevant terms (50%+ of budget)" |
| Wasted spend pattern | `KEYWORD_SEARCH_TERMS` | HIGH | "12,500 DKK on 'free [service]' terms, 0 conversions" |
| Low QS consuming budget | `KEYWORD_QS` | HIGH | "QS 1-3 keywords consuming 35% of spend" |
| No negative protection | `KEYWORD_NEGATIVES` | HIGH | "0.2:1 negative ratio, severely under-protected" |
| QS 1 keywords | `KEYWORD_QS` | CRITICAL | "5 keywords with QS 1, may have policy issues" |

---

## Checkpoint: Phase 4 Complete

Before proceeding to Phase 5, ALL checkboxes must be checked:

- [ ] Quality Score distribution calculated by spend
- [ ] `$QS_WEIGHTED_AVG` calculated
- [ ] Low QS keywords documented with components
- [ ] Search terms analyzed (90+ days)
- [ ] Each irrelevant term validated against `$CANONICAL_SERVICES`
- [ ] Wasted spend terms cross-referenced with `$WORKING_WELL`
- [ ] `$TOTAL_WASTED_SPEND` calculated
- [ ] Negative keyword counts documented
- [ ] `$NEGATIVE_POSITIVE_RATIO` calculated
- [ ] N-gram analysis completed
- [ ] `$TOP_WASTING_TERMS` identified
- [ ] `$TOP_CONVERTING_TERMS` identified
- [ ] Negative keyword recommendations generated
- [ ] All findings have DKK impact quantified
- [ ] RAG methodology queried
- [ ] `keyword_audit.json` generated per schema

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 5.**

---

## Output Artifact

**File:** `keyword_audit.json`
**Location:** `audits/{client-name}/keyword_audit.json`

Must conform to `schemas/keyword_audit.schema.json`:

```json
{
  "audit_period": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "days": 90
  },
  "summary": {
    "total_keywords": 250,
    "total_search_terms": 1500,
    "total_wasted_spend_dkk": 45000,
    "qs_weighted_avg": 5.8,
    "negative_positive_ratio": 0.4,
    "total_negatives": 100,
    "total_positives": 250
  },
  "quality_score_analysis": {
    "distribution": {
      "qs_1": { "keyword_count": 5, "spend": 2000, "spend_pct": 4 },
      "qs_2_3": { "keyword_count": 20, "spend": 8000, "spend_pct": 16 },
      "qs_4_6": { "keyword_count": 80, "spend": 20000, "spend_pct": 40 },
      "qs_7_8": { "keyword_count": 100, "spend": 15000, "spend_pct": 30 },
      "qs_9_10": { "keyword_count": 30, "spend": 4000, "spend_pct": 8 },
      "qs_null": { "keyword_count": 15, "spend": 1000, "spend_pct": 2 }
    },
    "low_qs_keywords": [
      {
        "keyword": "example keyword",
        "quality_score": 3,
        "expected_ctr": "Below average",
        "ad_relevance": "Average",
        "landing_page_exp": "Average",
        "spend": 5000,
        "clicks": 200,
        "conversions": 2,
        "campaign": "Campaign Name",
        "ad_group": "Ad Group Name"
      }
    ]
  },
  "search_term_analysis": {
    "wasted_spend_terms": [
      {
        "search_term": "free service example",
        "spend": 3500,
        "clicks": 150,
        "conversions": 0,
        "relevance": "low_intent",
        "recommendation": "add_negative_phrase",
        "campaign": "Campaign Name"
      }
    ],
    "top_converting_terms": [
      {
        "search_term": "service pris copenhagen",
        "spend": 2000,
        "clicks": 80,
        "conversions": 12,
        "cpa": 166.67,
        "campaign": "Campaign Name"
      }
    ],
    "ngram_analysis": {
      "top_wasting_patterns": [
        {
          "pattern": "free",
          "occurrences": 45,
          "total_spend": 12500,
          "total_conversions": 0
        }
      ],
      "top_converting_patterns": [
        {
          "pattern": "pris",
          "occurrences": 28,
          "total_spend": 8200,
          "total_conversions": 35
        }
      ]
    }
  },
  "negative_keyword_analysis": {
    "current_negatives": {
      "account_level": 50,
      "campaign_level": 50,
      "total": 100
    },
    "ratio_assessment": "under_protected",
    "recommended_negatives": [
      {
        "keyword": "free",
        "match_type": "phrase",
        "scope": "account",
        "reason": "45 terms, 12,500 DKK, 0 conversions",
        "potential_savings_dkk": 12500
      }
    ]
  },
  "findings": [
    {
      "id": "F020",
      "title": "45,000 DKK wasted on irrelevant search terms",
      "severity": "HIGH",
      "category": "KEYWORD_SEARCH_TERMS",
      "description": "...",
      "impact_dkk": 45000,
      "evidence": "150 search terms, detailed in appendix",
      "recommendation": "Implement negative keyword list (see recommendations)"
    }
  ]
}
```

---

*Phase 4 is often where the money is found. Wasted spend is tangible, quantifiable, and actionable - make sure `$TOTAL_WASTED_SPEND` is accurate and impactful.*
