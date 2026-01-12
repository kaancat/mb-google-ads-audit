# Phase 3: Campaign Performance Analysis

**Status:** Analysis Phase - Efficiency & Scaling Assessment

## Purpose

Assess campaign efficiency and identify scaling opportunities. This phase answers:

- Are campaigns hitting their targets?
- Where is budget being wasted?
- What scaling opportunities exist?
- Is the bid strategy working?

---

## Prerequisites

- Phase 0 completed with `discovery_brief.md` generated
- Phase 1 completed with `tracking_audit.md` generated
- Phase 2 completed with `structure_analysis.md` generated
- `$TARGET_CPA` or `$TARGET_ROAS` from Phase 0
- `$CONVERSION_TRUST_LEVEL` from Phase 1

---

## Inputs Required

1. **Campaign metrics** - Cost, Conversions, CPA, ROAS, CTR, etc.
2. **Impression share data** - IS, IS Lost (Budget), IS Lost (Rank)
3. **Bid strategy settings** - Strategy type, targets, performance
4. **Auction insights** - Competitor overlap, position metrics
5. **Budget data** - Daily budgets, limited by budget status

---

## Analysis Windows

Always analyze across multiple time windows to identify trends:

| Window | Purpose |
|--------|---------|
| **Last 30 days** | Recent trends, latest performance |
| **Last 90 days** | Primary analysis period |
| **Last 180 days** | Long-term patterns, seasonality |

**Compare against `$SEASONALITY` from Phase 0** - Don't flag normal seasonal drops.

---

## Step 1: Overall Metrics Assessment

### Fetch and Calculate

For each campaign and overall:
- Cost (DKK)
- Conversions
- CPA (Cost / Conversions)
- ROAS (Conversion Value / Cost)
- Clicks
- Impressions
- CTR (Clicks / Impressions)
- Conversion Rate (Conversions / Clicks)

### Performance Assessment Matrix

Compare actuals to targets from Phase 0:

```
CPA vs $TARGET_CPA
├── Actual CPA <= Target
│   └── GOOD - Hitting or beating target
│
├── Actual CPA 1-1.3x Target
│   └── ACCEPTABLE - Within tolerance
│
├── Actual CPA 1.3-2x Target
│   └── MEDIUM - Underperforming
│   └── Investigate root cause
│
└── Actual CPA > 2x Target
    └── HIGH - Significantly underperforming
    └── Deep analysis needed
```

```
ROAS vs $TARGET_ROAS
├── Actual ROAS >= Target
│   └── GOOD - Hitting or beating target
│
├── Actual ROAS 0.7-1x Target
│   └── MEDIUM - Room for improvement
│
└── Actual ROAS < 0.7x Target
    └── HIGH - Underperforming
```

### Data Reliability Disclaimer

**CRITICAL:**

```
IF $CONVERSION_TRUST_LEVEL = "unreliable":
    → Add disclaimer to all performance findings:
    "Note: Conversion data reliability is questionable (see Phase 1).
     These findings should be verified against external data."
```

---

## Step 2: Budget Analysis

### Fetch and Document

For each campaign:
- Daily budget
- Is campaign limited by budget?
- Impression Share Lost (Budget) %
- Impression Share Lost (Rank) %
- Search Impression Share %

### Decision Tree: Budget Opportunity Assessment

```
IS Lost (Budget) vs IS Lost (Rank)

High IS Lost (Budget) + Low IS Lost (Rank)
├── AND campaign is profitable (CPA <= target)?
│   └── OPPORTUNITY - Can scale with more budget
│   └── Estimate: Additional impressions × conversion rate × margin
│   └── MEDIUM priority
│
└── AND campaign is unprofitable?
    └── No action - fix efficiency first
    └── Don't add budget to losing campaign

Low IS Lost (Budget) + High IS Lost (Rank)
└── EFFICIENCY issue
    └── Fix Quality Score / bids before adding budget
    └── Adding budget won't help here

Both High
└── Prioritize rank improvement first
    └── Then evaluate budget opportunity

Both Low (<10% each)
└── GOOD - Capturing available opportunity well
    └── May need to expand targeting for growth
```

### Budget Fragmentation Check

```
Total daily budget / Number of campaigns

Average budget < 5x $TARGET_CPA
└── HIGH - Budgets too fragmented
└── Recommendation: Consolidate campaigns
└── Learning algorithms need sufficient data

Example: Target CPA 200 DKK, 20 campaigns at 100 DKK/day each
= Avg budget is only 0.5x target CPA
= CRITICAL budget fragmentation
```

---

## Step 3: Bid Strategy Evaluation

### Document Current Strategies

For each campaign:
- Bid strategy type
- Target (if applicable)
- Actual performance vs. target
- Conversion volume

### Decision Tree: Bid Strategy Assessment

```
Current Bid Strategy + Performance

Manual CPC
├── Conversions/month >= 15?
│   └── MEDIUM - Consider switching to smart bidding
│   └── Has sufficient data for automation
│
└── Conversions/month < 15?
    └── Manual may be appropriate
    └── LOW - Continue monitoring volume

Target CPA
├── Volume >= 30 conversions/month?
│   ├── Actual CPA within 20% of target?
│   │   └── GOOD - Strategy working
│   │
│   └── Actual CPA > 130% of target?
│       └── HIGH - Strategy underperforming
│       └── Options: Raise target, improve CR, improve QS
│
└── Volume < 30 conversions/month?
    └── MEDIUM - Insufficient data for tCPA
    └── Consider Maximize Conversions or manual

Target ROAS
├── Actual ROAS < 70% of target?
│   └── HIGH - Target too aggressive
│   └── Recommendation: Lower ROAS target
│
└── Spend significantly constrained?
    └── MEDIUM - Target may be limiting scale
    └── Test lower target to see impact

Maximize Conversions (no target)
├── CPA acceptable vs $TARGET_CPA?
│   └── GOOD - Consider adding tCPA
│
└── CPA too high?
    └── MEDIUM - Add target constraint
```

### Budget vs. Bid Strategy Alignment

```
Target CPA bidding + Budget Check

Daily Budget < 10x Target CPA
└── MEDIUM - Budget too constrained for strategy
└── Recommendation: Either raise budget or lower target
└── Algorithm can't optimize with insufficient headroom

Example: Target CPA = 500 DKK, Budget = 200 DKK/day
= Budget is 0.4x target = PROBLEMATIC
```

---

## Step 4: Auction Insights Analysis

### Fetch and Document

Top competitors by:
- Impression share
- Overlap rate
- Position above rate
- Outranking share

### Competitive Assessment

```
For top 5 competitors:

Competitor has >80% impression share vs your ~30%
└── Significant competitive gap
└── MEDIUM - Document competitive landscape
└── May need budget/targeting discussion

Competitor position above rate >70%
└── They're consistently outbidding you
└── Check: Are they paying more or have better QS?

You have highest impression share
└── GOOD - Market leader position
└── Document for client confidence
```

**Note:** Don't generate HIGH/CRITICAL findings from auction insights alone. Competition is context, not a problem to fix.

---

## Step 5: Campaign-Level Prioritization

### Create Performance Tiers

Based on analysis, categorize each campaign:

| Tier | Criteria | Action |
|------|----------|--------|
| **Stars** | CPA <= target, high volume, IS opportunity | Scale - add budget |
| **Workhorses** | CPA <= target, steady performance | Maintain - optimize incrementally |
| **Question Marks** | Mixed signals, potential | Investigate - deep dive needed |
| **Dogs** | CPA > 1.5x target, persistent | Restructure or pause |

Cross-reference with `$AUDIT_FOCUS` from Phase 0 - prioritize campaigns mentioned.

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get performance analysis methodology
performance_guidance = query_knowledge(
    "campaign performance analysis budget bid strategy",
    content_type="methodology"
)

# If bid strategy issues found
if bid_strategy_issues:
    strategy_guidance = query_knowledge(
        "target CPA target ROAS smart bidding optimization",
        content_type="best_practice"
    )

# If budget issues found
if budget_fragmentation:
    budget_guidance = query_knowledge(
        "budget allocation campaign consolidation",
        content_type="best_practice"
    )
```

---

## Findings Generation

For each issue identified, create a finding with:

| Field | Value |
|-------|-------|
| `id` | F00X (continue from Phase 2) |
| `title` | Action-oriented title |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `category` | One of: `PERFORMANCE_BUDGET`, `PERFORMANCE_BID_STRATEGY`, `PERFORMANCE_COMPETITION` |
| `description` | Detailed explanation with data |
| `impact_dkk` | Estimated monthly DKK impact |
| `evidence` | Specific metrics supporting finding |
| `recommendation` | Specific action to take |

### Common Findings for This Phase

| Issue | Category | Severity | Example |
|-------|----------|----------|---------|
| Budget opportunity | `PERFORMANCE_BUDGET` | MEDIUM | "Campaign X losing 40% IS to budget, CPA 20% below target" |
| Budget fragmentation | `PERFORMANCE_BUDGET` | HIGH | "23 campaigns averaging 75 DKK/day vs 300 DKK target CPA" |
| Bid strategy mismatch | `PERFORMANCE_BID_STRATEGY` | HIGH | "Target CPA on campaign with 8 conversions/month" |
| Constrained tROAS | `PERFORMANCE_BID_STRATEGY` | MEDIUM | "tROAS 400%, actual 380%, spend down 60%" |
| CPA 2x target | `PERFORMANCE_BID_STRATEGY` | HIGH | "Campaign X CPA 600 DKK vs 300 DKK target" |

---

## Checkpoint: Phase 3 Complete

Before proceeding to Phase 4, ALL checkboxes must be checked:

- [ ] Metrics fetched for 30/90/180 day windows
- [ ] Performance compared to `$TARGET_CPA` or `$TARGET_ROAS`
- [ ] IS Lost (Budget) and IS Lost (Rank) documented
- [ ] Budget opportunities identified and quantified
- [ ] Budget fragmentation assessed (avg budget vs target CPA)
- [ ] Bid strategies reviewed for each campaign
- [ ] Bid strategy vs. conversion volume assessed
- [ ] Auction insights pulled and documented
- [ ] Campaigns tiered (Stars/Workhorses/Question Marks/Dogs)
- [ ] RAG methodology queried
- [ ] All findings have category from: `PERFORMANCE_BUDGET`, `PERFORMANCE_BID_STRATEGY`, `PERFORMANCE_COMPETITION`
- [ ] `performance_analysis.json` generated per schema

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 4.**

---

## Output Artifact

**File:** `performance_analysis.json`
**Location:** `audits/{client-name}/performance_analysis.json`

Must conform to `schemas/performance_analysis.schema.json`:

```json
{
  "audit_period": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "days": 90
  },
  "overall_metrics": {
    "cost": 50000,
    "conversions": 150,
    "cpa": 333.33,
    "roas": 2.5,
    "clicks": 5000,
    "impressions": 100000,
    "ctr": 5.0,
    "conversion_rate": 3.0,
    "impression_share": 45.2
  },
  "campaigns": [
    {
      "name": "Campaign Name",
      "type": "SEARCH",
      "status": "ENABLED",
      "metrics_30d": { /* metrics */ },
      "metrics_90d": { /* metrics */ },
      "metrics_180d": { /* metrics */ },
      "limited_by_budget": true,
      "is_lost_budget_pct": 25.5,
      "is_lost_rank_pct": 10.2,
      "bid_strategy": "TARGET_CPA",
      "bid_target": 300,
      "tier": "star"
    }
  ],
  "budget_analysis": {
    "total_daily_budget": 2000,
    "avg_budget_per_campaign": 100,
    "campaigns_limited_by_budget": ["Campaign A", "Campaign B"],
    "budget_opportunity_dkk": 5000,
    "fragmentation_ratio": 0.33,
    "fragmentation_assessment": "fragmented"
  },
  "bid_strategy_analysis": [
    {
      "campaign": "Campaign Name",
      "strategy": "TARGET_CPA",
      "target": 300,
      "actual": 350,
      "monthly_conversions": 45,
      "assessment": "underperforming",
      "recommendation": "Raise target to 350 or improve QS"
    }
  ],
  "auction_insights": {
    "top_competitors": [
      {
        "domain": "competitor.dk",
        "impression_share": 65.2,
        "overlap_rate": 85.3,
        "position_above_rate": 55.0,
        "outranking_share": 40.5
      }
    ],
    "your_average_position": 2.3,
    "market_position_assessment": "strong_challenger"
  },
  "findings": [
    {
      "id": "F010",
      "title": "Budget opportunity in Campaign A",
      "severity": "MEDIUM",
      "category": "PERFORMANCE_BUDGET",
      "description": "...",
      "impact_dkk": 5000,
      "evidence": "40% IS lost to budget, CPA 20% below target",
      "recommendation": "Increase daily budget from 200 to 400 DKK"
    }
  ]
}
```

---

*Phase 3 quantifies performance and identifies scaling opportunities. Numbers tell the story - quantify impact in DKK wherever possible.*
