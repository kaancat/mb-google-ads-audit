# Severity Scoring Decision Tree

## Purpose

This decision tree determines the severity level for each audit finding. **Every finding MUST have a severity level assigned.**

---

## Severity Levels

| Level | Badge | Impact Threshold | Response Timeframe |
|-------|-------|------------------|-------------------|
| **CRITICAL** | 🔴 | Blocking optimization OR 50%+ spend waste | Week 1 (P0) |
| **HIGH** | 🟠 | 20-50% budget impact OR significant tracking issue | Month 1 (P1) |
| **MEDIUM** | 🟡 | Improvement opportunity with measurable impact | Months 2-3 (P2) |
| **LOW** | 🟢 | Best practice, nice to have | As time permits |

---

## Decision Flow

### Step 1: Check for Blocking Issues

```
Is this finding blocking optimization?
├── YES → CRITICAL
│   Examples:
│   ├── No conversion tracking configured
│   ├── All ads pointing to 404 pages
│   ├── Account suspended or limited
│   └── No active campaigns
└── NO → Continue to Step 2
```

### Step 2: Calculate Spend Impact

```
What percentage of spend is affected?

├── ≥ 50% of spend wasted/ineffective → CRITICAL
│   Examples:
│   ├── 50%+ of search terms are irrelevant
│   ├── Majority of budget going to non-converting campaigns
│   └── Massive negative keyword gaps affecting most traffic
│
├── 20-50% of spend affected → HIGH
│   Examples:
│   ├── 20-50% of budget on search terms with 0 conversions
│   ├── Low QS keywords consuming 20-50% of spend
│   └── Major attribution model issues affecting half of data
│
├── 5-20% of spend affected → MEDIUM
│   Examples:
│   ├── Some inefficient search terms identified
│   ├── Minor negative keyword gaps
│   └── Suboptimal bid strategy on secondary campaigns
│
└── < 5% of spend affected → LOW
    Examples:
    ├── Minor ad copy improvements needed
    ├── Additional negative keywords (small impact)
    └── Nice-to-have extension additions
```

### Step 3: Apply DKK Threshold Modifiers

After determining base severity from Steps 1-2, apply DKK modifiers:

| Monthly DKK Impact | Modifier |
|-------------------|----------|
| **> 10,000 DKK** | ⬆️ Upgrade severity by 1 level (max CRITICAL) |
| **5,000 - 10,000 DKK** | ➡️ No change |
| **1,000 - 5,000 DKK** | ➡️ No change |
| **< 1,000 DKK** | ⬇️ Downgrade severity by 1 level (min LOW) |

**Example:**
- Finding: Missing sitelinks (base severity: MEDIUM)
- Estimated impact: 12,000 DKK/month missed opportunity
- Final severity: HIGH (upgraded due to DKK threshold)

### Step 4: Check Against `$WORKING_WELL`

```
Is this finding related to something in $WORKING_WELL?
├── YES → EXCLUDE FINDING
│   └── Move to "excluded_findings" in output
│       Document: "Excluded per client indication this is working/intentional"
│
└── NO → Keep finding with calculated severity
```

---

## Category-Specific Severity Guidelines

### Conversion & Tracking (Phase 1)

| Finding | Default Severity | Notes |
|---------|-----------------|-------|
| No conversion tracking | CRITICAL | Blocking - cannot optimize |
| Wrong conversion actions as primary | HIGH | Corrupts all optimization |
| Last-click attribution | HIGH | Misleading data |
| Data-driven not enabled (eligible) | MEDIUM | Improvement opportunity |
| Enhanced conversions not enabled | MEDIUM | E-commerce: upgrade to HIGH |
| Minor tracking discrepancy (10-15%) | LOW | Acceptable range |
| Major tracking discrepancy (>20%) | HIGH | Data quality issue |

### Account Structure (Phase 2)

| Finding | Default Severity | Notes |
|---------|-----------------|-------|
| Display network on Search campaigns | HIGH | Wrong traffic type |
| Severely fragmented campaigns | MEDIUM | Unless intentional |
| Ad groups with <3 keywords | LOW | Review for consolidation |
| Inconsistent naming conventions | LOW | Best practice |
| Wrong location targeting | HIGH | Wasted spend on wrong geo |
| "Interest" instead of "Presence" | MEDIUM | May include irrelevant traffic |

### Campaign Performance (Phase 3)

| Finding | Default Severity | Notes |
|---------|-----------------|-------|
| Campaigns limited by budget (profitable) | MEDIUM | Opportunity, not problem |
| Campaigns limited by budget (unprofitable) | HIGH | Wasting limited budget |
| Bid strategy not appropriate for data volume | HIGH | Undermining optimization |
| Target vs actual CPA gap >50% | HIGH | Target unrealistic |
| Low impression share due to rank | MEDIUM | Efficiency opportunity |
| Low impression share due to budget | See above | Depends on profitability |

### Keywords & Search Terms (Phase 4)

| Finding | Default Severity | Notes |
|---------|-----------------|-------|
| QS 1 keywords with significant spend | CRITICAL | Likely not serving/policy issue |
| QS 2-3 keywords with significant spend | HIGH | Major inefficiency |
| QS 4-6 keywords with significant spend | MEDIUM | Room for improvement |
| Negative:Positive ratio < 0.3:1 | HIGH | Severely under-protected |
| Negative:Positive ratio 0.3-0.6:1 | MEDIUM | Under-protected |
| Search terms wasted spend >20% | HIGH | Major leak |
| Search terms wasted spend 10-20% | MEDIUM | Needs attention |
| Search terms wasted spend <10% | LOW | Minor cleanup |

### Ads & Assets (Phase 5)

| Finding | Default Severity | Notes |
|---------|-----------------|-------|
| RSAs with 1-4 headlines | CRITICAL | Severely under-filled |
| RSAs with 5-9 headlines | HIGH | Should add more |
| RSAs with only 1 description | CRITICAL | Severely under-filled |
| RSAs with 2-3 descriptions | HIGH | Should add more |
| Missing sitelinks | HIGH | Most important extension |
| Missing callouts | MEDIUM | Important but secondary |
| Missing structured snippets | LOW | Nice to have |
| Landing page 404 errors | CRITICAL | Blocking conversions |
| Slow landing page | MEDIUM | Affects QS |
| Ad copy typos | MEDIUM | Professionalism |

---

## Quick Win Classification

After severity is assigned, determine if finding is a "Quick Win":

```
Quick Win Criteria (ALL must be true):
├── Implementation time < 2 hours
├── No external dependencies (client approval, external tools)
├── Measurable impact within 7 days
└── Severity is HIGH or MEDIUM

If ALL criteria met → is_quick_win = true
Otherwise → is_quick_win = false
```

**Common Quick Wins:**
- Adding obvious negative keywords
- Fixing ad copy typos
- Pausing clearly underperforming search terms
- Enabling enhanced conversions
- Adding missing sitelinks (if copy exists)
- Disabling Display Network on Search campaigns

**NOT Quick Wins:**
- Restructuring campaigns
- Changing bid strategies (need learning period)
- Creating new landing pages
- Major QS improvements (take time)

---

## Output Format

For each finding, document:

```json
{
  "id": "F001",
  "title": "[Clear, action-oriented title]",
  "severity": "CRITICAL|HIGH|MEDIUM|LOW",
  "severity_rationale": "[Why this severity level was assigned]",
  "category": "[From canonical category list]",
  "description": "[Detailed description]",
  "impact_dkk": 12500,
  "evidence": "[Specific supporting data]",
  "recommendation": "[Specific action to take]",
  "priority": "P0|P1|P2",
  "is_quick_win": true|false
}
```

---

## Validation Rules

1. **CRITICAL findings must have:**
   - Clear blocking issue OR spend waste ≥50%
   - DKK impact estimate (even if approximate)
   - Specific recommendation

2. **HIGH findings must have:**
   - DKK impact estimate
   - Evidence with data

3. **All findings must:**
   - Be checked against `$WORKING_WELL`
   - Have exactly one category from canonical list
   - Have a clear recommendation

---

*Decision tree version: 1.0*
*Based on: PPC_SPECIALIST_AUDIT_FRAMEWORK.md severity criteria*
