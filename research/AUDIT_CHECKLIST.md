# Google Ads Audit Checklist

A comprehensive checklist for conducting PPC account audits. Use alongside the PPC Specialist Audit Framework.

**Pattern:** This checklist follows the phase-gating approach from `mb-keyword-analysis`. Each phase has a checkpoint that MUST be complete before proceeding.

---

## Pre-Audit Requirements

- [ ] Google Ads Customer ID obtained → `$CUSTOMER_ID`
- [ ] Website URL confirmed → `$WEBSITE_URL`
- [ ] Audit period defined (default: 90 days) → `$AUDIT_PERIOD_DAYS`
- [ ] Client contact for discovery interview scheduled
- [ ] Access to Google Ads account verified

---

## Phase 0: Discovery

> ⛔ **GATE: Cannot proceed to Phase 1 without completing ALL items below.**

### Website Analysis
- [ ] Business type identified → `$BUSINESS_TYPE` = [e-commerce / lead-gen / local-service / B2B / SaaS]
- [ ] Primary products/services documented → `$CANONICAL_SERVICES` (minimum 3)
- [ ] Service/product hierarchy understood
- [ ] Available landing pages catalogued
- [ ] Conversion paths identified (forms, phone, chat, purchase)
- [ ] Geographic focus noted → `$GEO_FOCUS`
- [ ] Unique value propositions extracted
- [ ] Competitor positioning understood

### Discovery Interview (11 Questions with Variable Mapping)

**Core Questions (MANDATORY):**
- [ ] Q1: Primary business goals → `$PRIMARY_GOAL` = [leads / sales / brand-awareness]
- [ ] Q2: Most important campaigns/services → `$AUDIT_FOCUS`
- [ ] Q3: What's working well → `$WORKING_WELL` (CRITICAL: protect these in audit)
- [ ] Q4: Current concerns → `$KNOWN_CONCERNS` (prioritize investigation)
- [ ] Q5: How conversions tracked → `$CONVERSION_TRACKING_METHOD`
- [ ] Q6: Recent changes (last 6 months) → `$RECENT_CHANGES`
- [ ] Q7: Seasonal patterns → `$SEASONALITY`
- [ ] Q8: Brand vs non-brand strategy → `$BRAND_STRATEGY` = [intentional / opportunistic / defensive / none]
- [ ] Q9: Profit margin / Customer LTV → `$PROFIT_MARGIN`

**Context Questions:**
- [ ] Q10: Competitors to watch → `$COMPETITORS`
- [ ] Q11: Desired audit outcome → `$SUCCESS_CRITERIA`

### Target Metrics (Infer if not stated)
- [ ] `$TARGET_CPA` defined (from bid strategy OR historical average OR interview)
- [ ] `$TARGET_ROAS` defined (if e-commerce/sales focus)
- [ ] Confidence level documented: [HIGH = stated / MEDIUM = calculated / INFERRED = estimated]

### Discovery Output
- [ ] `discovery_brief.md` created using template
- [ ] All `$VARIABLE` values populated
- [ ] `$WORKING_WELL` explicitly documented (even if empty)

## ✅ Checkpoint: Phase 0 Complete

| Requirement | Status |
|-------------|--------|
| Q1-Q9 answered | [ ] |
| Q11 answered | [ ] |
| `$CANONICAL_SERVICES` has ≥3 items | [ ] |
| `$TARGET_CPA` or `$TARGET_ROAS` defined | [ ] |
| `$BRAND_STRATEGY` documented | [ ] |
| discovery_brief.md generated | [ ] |

**If any checkbox is incomplete: STOP. Do not proceed to Phase 1.**

---

## Phase 1: Conversion & Tracking Audit

> ⚠️ **TENTPOLE PHASE: "Is the data even trustworthy?"**
>
> If conversion tracking is broken, every other metric is meaningless.

### Conversion Actions
- [ ] All conversion actions listed
- [ ] Primary vs. secondary classification reviewed
- [ ] Each conversion action firing correctly (check Web pages tab)
- [ ] Campaign-level conversion goals match `$PRIMARY_GOAL`

### Attribution
- [ ] Attribution model documented → `$ATTRIBUTION_MODEL`
- [ ] Last-click attribution flagged as HIGH severity if present
- [ ] Data-driven attribution recommended if not in use

### Time Lag Analysis
- [ ] Time lag distribution analyzed
- [ ] Day 1 conversion % calculated → `$DAY1_CONVERSION_PCT`
- [ ] Account aggressiveness assessed → `$ACCOUNT_AGGRESSIVENESS`
- [ ] Cross-referenced with `$BRAND_STRATEGY` (if intentional brand, high Day1% is expected)

**Time Lag Decision Tree:**
| `$DAY1_CONVERSION_PCT` | `$ACCOUNT_AGGRESSIVENESS` | Action |
|------------------------|---------------------------|--------|
| > 90% | conservative | Check if `$BRAND_STRATEGY` = intentional. If not, flag. |
| 70-90% | moderate | Review non-brand performance |
| 50-70% | balanced | No action |
| < 50% | aggressive | Adjust learning period expectations |

### Enhanced Conversions
- [ ] Enhanced conversions status checked → `$ENHANCED_CONVERSIONS`
- [ ] Revenue/profit tracking evaluated (if `$BUSINESS_TYPE` = e-commerce)

### Data Quality
- [ ] Conversion data compared to CRM/backend (if available)
- [ ] Discrepancy percentage calculated
- [ ] >20% discrepancy → `$CONVERSION_TRUST_LEVEL` = needs-verification
- [ ] 10-15% discrepancy = acceptable

### Variables Set
- [ ] `$ATTRIBUTION_MODEL` documented
- [ ] `$DAY1_CONVERSION_PCT` calculated
- [ ] `$ACCOUNT_AGGRESSIVENESS` determined
- [ ] `$CONVERSION_TRUST_LEVEL` assessed = [trustworthy / needs-verification / unreliable]
- [ ] `$ENHANCED_CONVERSIONS` documented

### Tracking Audit Output
- [ ] `tracking_audit.md` created
- [ ] All findings have severity ratings from decision tree
- [ ] All CRITICAL/HIGH findings have DKK impact estimated

## ✅ Checkpoint: Phase 1 Complete

| Requirement | Status |
|-------------|--------|
| `$ATTRIBUTION_MODEL` set | [ ] |
| `$DAY1_CONVERSION_PCT` calculated | [ ] |
| `$ACCOUNT_AGGRESSIVENESS` determined | [ ] |
| `$CONVERSION_TRUST_LEVEL` assessed | [ ] |
| tracking_audit.md generated | [ ] |

**If `$CONVERSION_TRUST_LEVEL` = unreliable: Document as CRITICAL finding. All subsequent findings must note data quality caveat.**

---

## Phase 2: Search Terms & Keywords

> 💡 **TENTPOLE PHASE: "Search terms report is the heartbeat of your entire account."**
>
> This is where money is actually being spent.

### Search Terms Report Analysis
- [ ] Search terms exported (90+ day window)
- [ ] Filtered for: `Clicks >= 100 AND CPA > $TARGET_CPA` (or no conversions)
- [ ] Each term validated against `$CANONICAL_SERVICES`
- [ ] Wasted spend calculated → `$TOTAL_WASTED_SPEND`
- [ ] Irrelevant search terms identified
- [ ] Cross-referenced with `$WORKING_WELL` (don't flag intentional)

**Search Term Decision Tree:**
```
For each search term with significant spend:
1. Is it relevant to $CANONICAL_SERVICES?
   NO → Negative keyword
2. Is CPA ≤ $TARGET_CPA (or has conversions)?
   YES → Keep (consider expanding)
   NO → Check intent
3. Does term show purchase intent?
   NO → Negative keyword
   YES → Optimization needed (bids, QS, ad copy, landing page)
```

### N-Gram Analysis
- [ ] Search terms data exported
- [ ] N-gram analysis run (2-gram, 3-gram)
- [ ] Top wasting words/phrases identified → `$TOP_WASTING_TERMS`
- [ ] Top converting words/phrases identified → `$TOP_CONVERTING_TERMS`
- [ ] Account-level negative opportunities extracted

### Negative Keyword Audit
- [ ] Account-level negative lists reviewed
- [ ] Campaign-level negatives reviewed
- [ ] Negative:Positive ratio calculated → `$NEGATIVE_POSITIVE_RATIO`
- [ ] Negative keyword gaps identified

**Negative Keyword Ratio Assessment:**
| Ratio | Severity | Action |
|-------|----------|--------|
| < 0.3:1 | HIGH | Urgent negative keyword audit |
| 0.3-0.6:1 | MEDIUM | Negative keyword audit recommended |
| 0.6-1:1 | LOW | Review for gaps |
| ≥ 1:1 | NONE | Good protection (check for over-blocking) |

### Quality Score Analysis
- [ ] QS distribution by spend analyzed → `$QS_WEIGHTED_AVG`
- [ ] QS 1-3 keywords with significant spend flagged (CRITICAL/HIGH)
- [ ] QS component breakdown reviewed (CTR 65%, Relevance 25%, LP 10%)
- [ ] QS improvement opportunities prioritized by spend

**Quality Score Severity:**
| QS | Severity | Primary Issue to Fix |
|----|----------|---------------------|
| 1 | CRITICAL | Landing page (policy/relevance) |
| 2-3 | HIGH | Expected CTR first |
| 4-6 | MEDIUM | CTR improvements |
| 7-10 | LOW/NONE | Maintain |

### Variables Set
- [ ] `$TOTAL_WASTED_SPEND` calculated
- [ ] `$QS_WEIGHTED_AVG` calculated
- [ ] `$NEGATIVE_POSITIVE_RATIO` calculated
- [ ] `$TOP_WASTING_TERMS` documented
- [ ] `$TOP_CONVERTING_TERMS` documented

### Keyword Audit Output
- [ ] `keyword_audit.json` created
- [ ] Each finding has DKK impact calculated
- [ ] Each finding validated against `$CANONICAL_SERVICES`
- [ ] Negative keyword recommendations documented with match types

## ✅ Checkpoint: Phase 2 Complete

| Requirement | Status |
|-------------|--------|
| `$TOTAL_WASTED_SPEND` calculated | [ ] |
| `$QS_WEIGHTED_AVG` calculated | [ ] |
| `$NEGATIVE_POSITIVE_RATIO` calculated | [ ] |
| N-gram analysis completed | [ ] |
| All wasted spend findings have DKK impact | [ ] |
| keyword_audit.json generated | [ ] |

---

## Phase 3: Account Structure

### Campaign Organization
- [ ] Campaign naming conventions reviewed
- [ ] Campaign goals alignment checked
- [ ] Over-segmentation assessed
- [ ] Under-segmentation assessed
- [ ] Campaign consolidation opportunities noted

### Ad Group Organization
- [ ] Ad group to keyword relevance checked
- [ ] Ad groups with <3 keywords flagged
- [ ] Ad groups spanning multiple themes flagged
- [ ] Ad group to landing page alignment verified

### Network Settings
- [ ] Search Partners setting documented
- [ ] Display Network on Search campaigns flagged
- [ ] Recommendations for network changes

### Geographic Targeting
- [ ] Location targeting reviewed
- [ ] Location options (presence vs. interest) checked
- [ ] Geographic performance analyzed

### Structure Audit Output
- [ ] `structure_analysis.md` created
- [ ] Structure issues prioritized
- [ ] Reorganization recommendations documented

---

## Phase 4: Campaign Performance

### Performance Metrics (30/90/180 day windows)
- [ ] Cost
- [ ] Conversions
- [ ] CPA
- [ ] ROAS
- [ ] Click-through rate
- [ ] Conversion rate
- [ ] Impression share

### Budget Analysis
- [ ] Campaigns limited by budget identified
- [ ] IS Lost (Budget) calculated
- [ ] IS Lost (Rank) calculated
- [ ] Budget opportunity quantified
- [ ] Budget vs. bid strategy alignment checked

### Bid Strategy Analysis
- [ ] Current bid strategy documented
- [ ] Bid strategy appropriateness evaluated
- [ ] Target vs. actual performance compared
- [ ] Budget sufficiency for bid strategy verified
- [ ] Bid strategy recommendations documented

### Auction Insights
- [ ] Top competitors identified
- [ ] Overlap rates analyzed
- [ ] Position above rates compared
- [ ] Competitive trends over time reviewed

### Performance Audit Output
- [ ] `performance_analysis.json` created
- [ ] Key performance issues listed
- [ ] Scaling opportunities identified
- [ ] Budget recommendations documented

---

## Phase 5: Ads & Assets

### RSA Analysis
- [ ] Ad strength distribution documented
- [ ] Headlines per ad counted (target: 10-15)
- [ ] Descriptions per ad counted (target: 4)
- [ ] Message diversity assessed
- [ ] Pinned headlines reviewed
- [ ] Ad copy relevance to keywords checked
- [ ] Typos identified

### Extension/Asset Audit
- [ ] Sitelinks: Present? Relevant? Performance?
- [ ] Callouts: Present? Compelling?
- [ ] Structured Snippets: Present? Appropriate?
- [ ] Call Extensions: Present? (if local)
- [ ] Location Extensions: Present? (if local)
- [ ] Price Extensions: Present? (if applicable)

### Asset Performance
- [ ] High-spend, low-conversion assets identified
- [ ] Filter applied: $300+ clicks, <3 conversions
- [ ] Underperforming assets flagged

### Ad Audit Output
- [ ] `ad_copy_audit.json` created
- [ ] Ad copy recommendations documented
- [ ] Extension opportunities listed
- [ ] Asset optimization recommendations

---

## Phase 6: Landing Pages

### URL Verification
- [ ] All landing page URLs tested
- [ ] 404 errors identified
- [ ] Redirect issues noted

### Landing Page Quality
- [ ] Page load speed acceptable
- [ ] Mobile experience functional
- [ ] Clear CTA present
- [ ] Content relevant to ad message
- [ ] Form/conversion path working

### Landing Page Opportunities
- [ ] Missing landing page opportunities identified
- [ ] Homepage-only campaigns flagged
- [ ] Landing page improvement recommendations

---

## Phase 7: Audiences

### Remarketing Audiences
- [ ] Remarketing audiences set up?
- [ ] Audience lists reviewed
- [ ] List sizes documented

### Observation Audiences
- [ ] Observation audiences applied?
- [ ] Audience performance analyzed
- [ ] Audience insights documented

### Audience Opportunities
- [ ] Missing audience opportunities identified
- [ ] Custom segment opportunities noted

---

## Phase 8: Synthesis & Recommendations

> 🎯 **AGGREGATION PHASE: Consolidate all findings into actionable deliverable.**

### Finding Aggregation
- [ ] All findings from Phases 1-7 collected
- [ ] Each finding validated against `$WORKING_WELL`
- [ ] Excluded findings documented with reason (if related to `$WORKING_WELL`)

### Severity Matrix
- [ ] All findings have severity from decision tree: [CRITICAL / HIGH / MEDIUM / LOW]
- [ ] Each finding has exactly one category from canonical list
- [ ] DKK impact estimated for all CRITICAL/HIGH findings
- [ ] Severity modifiers applied based on DKK thresholds

**Severity Counts:**
- [ ] `$CRITICAL_COUNT` calculated
- [ ] `$HIGH_COUNT` calculated
- [ ] `$MEDIUM_COUNT` calculated
- [ ] `$LOW_COUNT` calculated
- [ ] `$TOTAL_IMPACT_DKK` calculated (sum of all finding impacts)

### Quick Wins Extraction
- [ ] Quick win criteria applied to each finding
- [ ] `$QUICK_WINS_COUNT` calculated
- [ ] Each quick win has: <2hr implementation, no dependencies, 7-day impact

**Quick Win Criteria (ALL must be true):**
- Implementation time < 2 hours
- No external dependencies
- Measurable impact within 7 days
- Severity is HIGH or MEDIUM

### Wasted Spend Summary
- [ ] `$TOTAL_WASTED_SPEND` from Phase 2 included
- [ ] Wasted spend broken down by category
- [ ] Total opportunity quantified

### Action Plan Creation
- [ ] P0 (Week 1) = CRITICAL findings only
- [ ] P1 (Month 1) = HIGH findings + Quick Wins
- [ ] P2 (Months 2-3) = MEDIUM/LOW findings + Strategic changes
- [ ] Each action has owner assigned: [client / agency / both]

### Variables Set
- [ ] `$CRITICAL_COUNT` finalized
- [ ] `$HIGH_COUNT` finalized
- [ ] `$MEDIUM_COUNT` finalized
- [ ] `$LOW_COUNT` finalized
- [ ] `$QUICK_WINS_COUNT` finalized
- [ ] `$TOTAL_IMPACT_DKK` finalized

### Recommendations Output
- [ ] `recommendations.json` created following schema
- [ ] All findings have required fields: id, title, severity, category, description, recommendation, priority
- [ ] All CRITICAL/HIGH findings have impact_dkk
- [ ] Excluded findings documented

## ✅ Checkpoint: Phase 8 Complete

| Requirement | Status |
|-------------|--------|
| All findings aggregated from Phases 1-7 | [ ] |
| Each finding has severity and category | [ ] |
| Each finding cross-referenced against `$WORKING_WELL` | [ ] |
| Quick wins identified | [ ] |
| Action plan has P0, P1, AND P2 items | [ ] |
| recommendations.json generated | [ ] |

**If Action Plan is empty in any priority tier: Review findings - at minimum there should be MEDIUM optimization opportunities.**

---

## Phase 9: Presentation

### Deliverable Creation
- [ ] Executive summary finalized
- [ ] Key metrics table created
- [ ] Severity matrix formatted
- [ ] Section-by-section findings documented
- [ ] Priority action plan formatted
- [ ] Technical appendices prepared

### Presentation Output
- [ ] `audit_presentation.html` generated
- [ ] All supporting data files complete

---

## Quick Reference: Severity Criteria

| Level | Criteria | Examples |
|-------|----------|----------|
| CRITICAL | Blocking optimization, 50%+ spend waste | No conversion tracking, massive irrelevant spend |
| HIGH | 20%+ budget impact, significant issue | Poor QS keywords eating budget, attribution problems |
| MEDIUM | Improvement opportunity | Missing extensions, suboptimal bid strategy |
| LOW | Best practice, nice to have | Ad copy tweaks, minor QS improvements |

---

## Quick Reference: Key Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Time Lag Day 1 | >90% | Flag as too conservative/brand-heavy |
| QS Keywords | 1-3 with significant spend | Critical priority |
| Negative:Positive Ratio | <1:1 | Likely missing negatives |
| IS Lost (Budget) | >20% | Budget opportunity exists |
| IS Lost (Rank) | >20% | Efficiency issue to fix |
| Headlines per RSA | <5 | Flag for improvement |
| Descriptions per RSA | <3 | Flag for improvement |
| Conversion discrepancy | >20% | Tracking issue |

---

## Quick Reference: Budget Guidelines

| Bid Strategy | Minimum Daily Budget |
|--------------|---------------------|
| Target CPA | 10-15x target CPA |
| Target ROAS | 10-15x average order value |
| Maximize Conversions | 10-15x expected CPA |

---

## Variable Reference Summary

All variables used in the audit workflow, organized by phase where they are set.

### Phase 0: Discovery Variables

| Variable | Type | Description |
|----------|------|-------------|
| `$CUSTOMER_ID` | string | Google Ads Customer ID |
| `$WEBSITE_URL` | string | Client website URL |
| `$AUDIT_PERIOD_DAYS` | integer | Audit period (default: 90) |
| `$BUSINESS_TYPE` | enum | e-commerce, lead-gen, local-service, B2B, SaaS |
| `$PRIMARY_GOAL` | enum | leads, sales, brand-awareness |
| `$TARGET_CPA` | number | Target cost per acquisition (DKK) |
| `$TARGET_ROAS` | number | Target return on ad spend (%) |
| `$GEO_FOCUS` | string | Geographic focus |
| `$WORKING_WELL` | list | Things to NOT flag in audit |
| `$KNOWN_CONCERNS` | list | Priority investigation areas |
| `$BRAND_STRATEGY` | enum | intentional, opportunistic, defensive, none |
| `$PROFIT_MARGIN` | string | Profit margin or customer LTV |
| `$AUDIT_FOCUS` | string | Priority areas from interview |
| `$CANONICAL_SERVICES` | list | Services from website (single source of truth) |
| `$SUCCESS_CRITERIA` | string | What client wants from audit |
| `$CONVERSION_TRACKING_METHOD` | string | How conversions are tracked |
| `$RECENT_CHANGES` | string | Changes in last 6 months |
| `$SEASONALITY` | string | Seasonal patterns |
| `$COMPETITORS` | list | Competitors to watch |

### Phase 1: Tracking Variables

| Variable | Type | Description |
|----------|------|-------------|
| `$CONVERSION_TRUST_LEVEL` | enum | trustworthy, needs-verification, unreliable |
| `$ATTRIBUTION_MODEL` | string | Current attribution model |
| `$DAY1_CONVERSION_PCT` | number | Day 1 conversion percentage |
| `$ACCOUNT_AGGRESSIVENESS` | enum | conservative, moderate, balanced, aggressive |
| `$ENHANCED_CONVERSIONS` | enum | enabled, disabled |

### Phase 2: Keyword Variables

| Variable | Type | Description |
|----------|------|-------------|
| `$TOTAL_WASTED_SPEND` | number | Cumulative wasted spend (DKK) |
| `$QS_WEIGHTED_AVG` | number | Spend-weighted Quality Score average |
| `$NEGATIVE_POSITIVE_RATIO` | number | Negative:Positive keyword ratio |
| `$TOP_WASTING_TERMS` | list | Top 10 wasting search term patterns |
| `$TOP_CONVERTING_TERMS` | list | Top 10 converting search term patterns |

### Phase 8: Synthesis Variables

| Variable | Type | Description |
|----------|------|-------------|
| `$CRITICAL_COUNT` | integer | Number of CRITICAL findings |
| `$HIGH_COUNT` | integer | Number of HIGH findings |
| `$MEDIUM_COUNT` | integer | Number of MEDIUM findings |
| `$LOW_COUNT` | integer | Number of LOW findings |
| `$QUICK_WINS_COUNT` | integer | Number of quick win opportunities |
| `$TOTAL_IMPACT_DKK` | number | Total estimated DKK impact |

---

*Use this checklist alongside PPC_SPECIALIST_AUDIT_FRAMEWORK.md for comprehensive audit coverage.*
*Pattern reference: mb-keyword-analysis plugin variable storage system.*
