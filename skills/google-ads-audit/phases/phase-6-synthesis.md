# Phase 6: Synthesis & Recommendations

**Status:** Consolidation Phase - Master Findings & Action Plan

## Purpose

Consolidate all findings into a prioritized action plan. This phase:

- Aggregates findings from Phases 1-5
- Applies consistent severity scoring
- Validates against `$WORKING_WELL` (remove intentional items)
- Quantifies total DKK impact
- Creates prioritized action plan (P0/P1/P2)
- Identifies quick wins

---

## Prerequisites

- All Phases 0-5 completed with artifacts generated:
  - `discovery_brief.md`
  - `tracking_audit.md`
  - `structure_analysis.md`
  - `performance_analysis.json`
  - `keyword_audit.json`
  - `ad_copy_audit.json`

---

## Inputs Required

1. **All findings from Phases 1-5**
2. **`$WORKING_WELL`** from Phase 0 (for validation)
3. **`$SUCCESS_CRITERIA`** from Phase 0 (for alignment)
4. **`$TOTAL_WASTED_SPEND`** from Phase 4
5. **`$TARGET_CPA`** or **`$TARGET_ROAS`** from Phase 0

---

## Variables Set in This Phase

| Variable | Source | Description |
|----------|--------|-------------|
| `$CRITICAL_COUNT` | Finding aggregation | Number of CRITICAL findings |
| `$HIGH_COUNT` | Finding aggregation | Number of HIGH findings |
| `$MEDIUM_COUNT` | Finding aggregation | Number of MEDIUM findings |
| `$LOW_COUNT` | Finding aggregation | Number of LOW findings |
| `$QUICK_WINS_COUNT` | Finding filter | Number of quick win opportunities |
| `$TOTAL_IMPACT_DKK` | Sum of all findings | Total estimated monthly DKK impact |

---

## Step 1: Aggregate All Findings

### Collect Findings

Gather all findings from phases 1-5:

| Phase | Source File | Expected Categories |
|-------|-------------|---------------------|
| 1 | `tracking_audit.md` | TRACKING_* |
| 2 | `structure_analysis.md` | STRUCTURE_* |
| 3 | `performance_analysis.json` | PERFORMANCE_* |
| 4 | `keyword_audit.json` | KEYWORD_* |
| 5 | `ad_copy_audit.json` | ADS_* |

### Validate Categories

**Every finding MUST have exactly one category from the canonical list:**

| Phase | Valid Categories |
|-------|-----------------|
| 1 | `TRACKING_CONVERSION`, `TRACKING_ATTRIBUTION`, `TRACKING_ENHANCED`, `TRACKING_DATA_QUALITY` |
| 2 | `STRUCTURE_CAMPAIGN`, `STRUCTURE_ADGROUP`, `STRUCTURE_NETWORK`, `STRUCTURE_GEO` |
| 3 | `PERFORMANCE_BUDGET`, `PERFORMANCE_BID_STRATEGY`, `PERFORMANCE_COMPETITION` |
| 4 | `KEYWORD_QS`, `KEYWORD_SEARCH_TERMS`, `KEYWORD_NEGATIVES` |
| 5 | `ADS_RSA`, `ADS_EXTENSIONS`, `ADS_LANDING_PAGE` |

**If a finding has no category or wrong category: FIX IT before proceeding.**

---

## Step 2: Validate Against $WORKING_WELL

### Cross-Reference Each Finding

```
For each finding:
├── Is it related to something in $WORKING_WELL?
│   ├── YES → EXCLUDE from final findings
│   │   └── Add to "excluded_findings" list with reason
│   │   └── Example: "Excluded: Client indicated brand campaigns are working well"
│   │
│   └── NO → Keep finding
```

### Document Exclusions

Create `excluded_findings` list:

```json
{
  "title": "High CPA on Brand Campaign",
  "reason": "Excluded per $WORKING_WELL - client indicated brand bidding is intentional",
  "working_well_reference": "Brand campaigns are working well for us"
}
```

---

## Step 3: Apply Severity Scoring

### Decision Tree: Severity Assignment

**Step A: Determine Base Severity**

| Condition | Base Severity |
|-----------|---------------|
| Blocking optimization (no conversion tracking, broken URLs) | `CRITICAL` |
| Spend waste ≥ 50% of budget | `CRITICAL` |
| Spend waste 20-50% of budget | `HIGH` |
| Significant tracking issue affecting all data | `HIGH` |
| Improvement opportunity with measurable impact | `MEDIUM` |
| Best practice, nice to have | `LOW` |

**Step B: Apply DKK Threshold Modifiers**

| Monthly Impact | Modifier |
|----------------|----------|
| > 10,000 DKK | +1 severity level (max CRITICAL) |
| 5,000 - 10,000 DKK | No change |
| 1,000 - 5,000 DKK | No change |
| < 1,000 DKK | -1 severity level (min LOW) |

**Step C: Document Severity Rationale**

Each finding must include `severity_rationale`:
- Why this severity was assigned
- Reference to decision tree criteria

---

## Step 4: Quantify DKK Impact

### Requirements by Severity

| Severity | Impact Requirement |
|----------|-------------------|
| `CRITICAL` | **REQUIRED** - Must have `impact_dkk` |
| `HIGH` | **REQUIRED** - Must have `impact_dkk` |
| `MEDIUM` | Recommended if quantifiable |
| `LOW` | Optional |

### Impact Calculation Methods

1. **Wasted Spend** - Direct spend on non-performing elements
   - Example: 12,500 DKK on "free" search terms = 12,500 DKK impact

2. **Opportunity Cost** - Estimated revenue loss from issues
   - Example: Low QS → 20% higher CPC → X DKK extra spend

3. **Efficiency Gain** - Potential improvement from fixes
   - Example: Adding sitelinks → ~10% CTR improvement → X more clicks at current CPC

### Calculate Total Impact

```
$TOTAL_IMPACT_DKK = Sum of all impact_dkk values across findings
```

---

## Step 5: Classify Quick Wins

### Quick Win Criteria

A finding is a "Quick Win" if **ALL** of the following:

| Criterion | Definition |
|-----------|------------|
| Implementation time | < 2 hours |
| Dependencies | No external dependencies (client approval, tools) |
| Measurable impact | Impact visible within 7 days |
| Severity | HIGH or MEDIUM (not LOW) |

### Common Quick Wins

| Finding Type | Time | Why Quick Win |
|--------------|------|---------------|
| Add negative keywords | 30 min | Stop wasted spend immediately |
| Add RSA headlines | 1 hour | Improve ad strength |
| Add sitelinks | 30 min | Improve CTR |
| Fix landing page URLs | 30 min | Stop wasting spend on 404s |
| Change location options | 5 min | Stop irrelevant traffic |
| Disable Display on Search | 5 min | Reallocate budget |

### Mark Quick Wins

Set `is_quick_win: true` on qualifying findings.

Calculate: `$QUICK_WINS_COUNT` = count of quick wins

---

## Step 6: Create Priority Action Plan

### Priority Assignment Rules

| Priority | Timeframe | Criteria |
|----------|-----------|----------|
| **P0** | Week 1 | CRITICAL findings only |
| **P1** | Month 1 | HIGH findings + All Quick Wins |
| **P2** | Months 2-3 | MEDIUM + LOW findings + Strategic |

### Action Plan Structure

For each priority level:

```json
{
  "P0": {
    "timeframe": "Week 1",
    "focus": "Critical fixes - stop the bleeding",
    "items": [
      {
        "finding_id": "F001",
        "action": "Set up conversion tracking",
        "owner": "agency",
        "impact_dkk": 50000
      }
    ]
  },
  "P1": {
    "timeframe": "Month 1",
    "focus": "High-impact optimizations and quick wins",
    "items": [...]
  },
  "P2": {
    "timeframe": "Months 2-3",
    "focus": "Strategic improvements and testing",
    "items": [...]
  }
}
```

### Owner Assignment

| Owner | When to Assign |
|-------|---------------|
| `agency` | Technical implementation (negative keywords, bid changes, ad copy) |
| `client` | Requires access/decisions (landing pages, tracking code, budget) |
| `both` | Collaborative (strategy decisions, structure changes) |

---

## Step 7: Calculate Summary Counts

### Count by Severity

```
$CRITICAL_COUNT = count of CRITICAL findings (after exclusions)
$HIGH_COUNT = count of HIGH findings (after exclusions)
$MEDIUM_COUNT = count of MEDIUM findings (after exclusions)
$LOW_COUNT = count of LOW findings (after exclusions)
```

### Determine Overall Health

| Condition | Overall Health |
|-----------|---------------|
| Any CRITICAL findings | `critical` |
| 3+ HIGH findings OR 5+ MEDIUM | `needs_attention` |
| 1-2 HIGH findings, few MEDIUM | `good` |
| Only LOW findings | `excellent` |

---

## Step 8: Align with Success Criteria

### Compare to $SUCCESS_CRITERIA

From Phase 0, client defined what success looks like.

Verify the action plan addresses:
- Specific concerns mentioned
- Focus areas requested
- Expected outcomes

If gaps exist, note them.

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get synthesis best practices
synthesis_guidance = query_knowledge(
    "audit recommendations prioritization action plan",
    content_type="best_practice"
)

# If many quick wins
if quick_wins_count > 5:
    quickwin_guidance = query_knowledge(
        "quick wins implementation order priority",
        content_type="methodology"
    )
```

---

## Checkpoint: Phase 6 Complete

Before proceeding to Phase 7, ALL checkboxes must be checked:

- [ ] All findings aggregated from Phases 1-5
- [ ] Each finding has valid category from canonical list
- [ ] Each finding validated against `$WORKING_WELL`
- [ ] Excluded findings documented with reasons
- [ ] Severity assigned using decision tree
- [ ] Severity rationale documented for each finding
- [ ] `impact_dkk` set for all CRITICAL and HIGH findings
- [ ] `$TOTAL_IMPACT_DKK` calculated
- [ ] Quick wins identified (< 2hr, no dependencies, 7-day impact)
- [ ] `$QUICK_WINS_COUNT` calculated
- [ ] `$CRITICAL_COUNT`, `$HIGH_COUNT`, `$MEDIUM_COUNT`, `$LOW_COUNT` calculated
- [ ] Action plan has items in P0, P1, AND P2
- [ ] Each action item has owner assigned
- [ ] Overall health determined
- [ ] Alignment with `$SUCCESS_CRITERIA` verified
- [ ] RAG methodology queried
- [ ] `recommendations.json` generated per schema

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 7.**

---

## Output Artifact

**File:** `recommendations.json`
**Location:** `audits/{client-name}/recommendations.json`

Must conform to `schemas/recommendations.schema.json`:

```json
{
  "metadata": {
    "audit_date": "YYYY-MM-DD",
    "customer_id": "123-456-7890",
    "customer_name": "Client Name",
    "audit_period_days": 90,
    "business_type": "lead-gen",
    "target_cpa": 300,
    "primary_goal": "leads"
  },
  "summary": {
    "total_wasted_spend_dkk": 45000,
    "critical_count": 2,
    "high_count": 5,
    "medium_count": 8,
    "low_count": 3,
    "quick_wins_count": 6,
    "total_impact_dkk": 75000,
    "overall_health": "needs_attention"
  },
  "findings": [
    {
      "id": "F001",
      "title": "No conversion tracking configured",
      "severity": "CRITICAL",
      "severity_rationale": "Blocking optimization - cannot measure success",
      "category": "TRACKING_CONVERSION",
      "phase": 1,
      "description": "Account has zero conversion actions configured...",
      "impact_dkk": 50000,
      "evidence": "No conversion actions found in account",
      "recommendation": "Implement conversion tracking for form submissions and calls",
      "priority": "P0",
      "is_quick_win": false,
      "implementation_time": "4-8 hours",
      "requires_client_action": true
    }
  ],
  "action_plan": {
    "P0": {
      "timeframe": "Week 1",
      "focus": "Critical fixes - stop the bleeding",
      "items": [
        {
          "finding_id": "F001",
          "action": "Set up conversion tracking for leads and calls",
          "owner": "both",
          "impact_dkk": 50000
        }
      ]
    },
    "P1": {
      "timeframe": "Month 1",
      "focus": "High-impact optimizations and quick wins",
      "items": [...]
    },
    "P2": {
      "timeframe": "Months 2-3",
      "focus": "Strategic improvements and testing framework",
      "items": [...]
    }
  },
  "quick_wins": [
    {
      "finding_id": "F005",
      "title": "Add negative keywords",
      "action": "Implement negative keyword list for irrelevant terms",
      "expected_impact": "12,500 DKK/month savings",
      "implementation_time": "< 1 hour"
    }
  ],
  "excluded_findings": [
    {
      "title": "High CPA on Brand Campaign",
      "reason": "Client indicated brand bidding is intentional and working well",
      "working_well_reference": "Q3: Brand campaigns are performing well for us"
    }
  ],
  "appendices": {
    "negative_keywords": ["free", "jobs", "DIY", "cheap"],
    "keyword_additions": ["service pris", "best service copenhagen"],
    "search_terms_to_exclude": [
      {
        "term": "free service example",
        "spend": 3500,
        "reason": "0 conversions, low intent"
      }
    ]
  }
}
```

---

*Phase 6 is the culmination of all analysis. The quality of the action plan determines the value of the entire audit.*
