# PPC Specialist Audit Framework

## Research Synthesis from Monday Brew Knowledge Base

This document synthesizes deep research into how experienced PPC specialists approach Google Ads account audits. It captures the mindset, methodology, and decision frameworks that inform expert audit practices.

---

## The PPC Specialist Mindset

### Core Philosophy

**"Salesmanship in pixels."** Every decision must be anchored to profit. The goal is not to find things wrong—it's to find opportunities to make more money than what's being spent.

### The Three Tentpoles

Before diving into details, a specialist focuses on three fundamental pillars:

1. **Business Understanding** - You cannot diagnose without context
2. **Conversion Tracking** - Is the data even trustworthy?
3. **Search Terms Report** - Where is money actually being spent?

These three areas alone can reveal 80% of what matters. Everything else is refinement.

### The Three Audit Types (Combine All Three)

| Type | Focus | Key Questions |
|------|-------|---------------|
| **Quick Wins** | Egregious errors, immediate fixes | "What should have been fixed yesterday?" |
| **Strategic** | Business goals alignment, testing framework | "Is this account structured to meet business goals?" |
| **Optimization** | Day-to-day blueprint | "What should be done daily/weekly/monthly?" |

The best audits incorporate all three perspectives.

---

## Phase 0: Business Understanding (The Foundation)

### Why This Comes First

> "I remember once, we signed one of our largest clients. They wanted me to do this whole audit. I quickly looked at the account, got a feel for the website, went into their search terms report, and I saw that 98% of their budget was being spent on branded search. I sent them an email saying, look, I'm not doing an audit. It's not worth it because there's not enough here."

Understanding the business prevents:
- Misdiagnosing intentional strategies as problems
- Recommending changes that don't align with actual goals
- Wasting time on non-issues

### Website Analysis (~1 hour minimum)

**What to extract:**
- Business type (e-commerce, lead gen, local service, B2B, SaaS)
- Products/services offered and their hierarchy
- Conversion paths (forms, phone, chat, purchase)
- Landing pages available (what URLs can ads point to?)
- Geographic focus
- Competitive positioning/unique value propositions

**Why it matters:**
- Informs what conversions should be tracked
- Reveals landing page opportunities
- Helps evaluate ad copy relevance
- Provides context for keyword choices

### Discovery Interview (11 Questions)

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

**Note:** Target CPA/ROAS can often be inferred from account data (conversion goals, historical performance, bid strategy settings).

---

## Phase 1: Conversion Tracking Audit

### The Critical Question

> "Is the data even trustworthy?"

If conversion tracking is broken, every other metric is meaningless.

### What to Check

1. **Conversion Actions Setup**
   - What actions are being tracked?
   - Are they firing on the correct pages?
   - Primary vs. secondary conversion classification
   - Is each campaign optimizing for the correct conversion action(s)?

2. **Attribution Model**
   - **Last-click = Problem.** This doesn't tell the whole story.
   - **Data-driven attribution = Recommended.** It learns patterns from your data.
   - This is a platform to discuss how attribution impacts decision-making.

3. **Enhanced Conversions**
   - Is enhanced conversion tracking activated?
   - Critical for e-commerce: revenue tracking, profit tracking

4. **Time Lag Analysis** (Key Diagnostic)

   | Time Lag Pattern | Interpretation |
   |------------------|----------------|
   | 90% conversions Day 1 | Too conservative; likely brand-heavy |
   | Longer time lag (days 2-10+) | More appropriate non-brand mix |
   | Very long time lag | May indicate considered purchase; affects learning period |

5. **Conversion Data Quality**
   - Compare Google Ads conversions to CRM/backend data
   - 10-15% discrepancy is acceptable
   - 20-30% discrepancy = problem to investigate

### Red Flags
- No conversion tracking at all
- Multiple conversion actions all set as primary
- Campaigns optimizing for different goals than intended
- Significant data discrepancies

---

## Phase 2: Search Terms Report Analysis

### Why This Is a Tentpole

> "Search terms report is the heartbeat of your entire account. That's what you're spending your money on."

### Analysis Method

**Filter for Bad Search Terms:**
```
Filter 1: Clicks >= 100
Filter 2: Cost per conversion > [Target CPA]
```

This reveals search terms with enough data that are clearly underperforming.

**Key Questions:**
1. How much budget is going to irrelevant searches?
2. Are there obvious negative keyword gaps?
3. Is the account too brand-heavy or not brand-heavy enough?
4. What percentage of spend goes to converting vs. non-converting terms?

### Decision Framework for Each Search Term

```
Is this search term relevant to the business?
├── NO → Add as negative keyword immediately
└── YES → Is it profitable?
    ├── YES → Keep, potentially expand
    └── NO → Could it become profitable?
        ├── NO (clearly irrelevant intent) → Negative keyword
        └── YES (good intent, poor performance) → Options:
            ├── Lower bids
            ├── Improve Quality Score
            ├── Improve ad copy relevance
            ├── Improve landing page
            └── Adjust bid strategy
```

### N-Gram Analysis

Export search term data and run n-gram analysis to identify:
- Which words/phrases generate the most conversions
- Which words/phrases waste the most spend
- Patterns for account-level negative keywords

**Best Practice:** Account-level negatives should be broad match. When creating new campaigns, these lists protect immediately.

### Wasted Spend Quantification

Every finding should include estimated DKK impact:
- "Search term X received 500 clicks, 0 conversions = Y DKK wasted"
- "12 search terms are eating 40% of budget with no conversions"

---

## Phase 3: Account Structure Analysis

### What to Evaluate

1. **Campaign Organization**
   - Does structure match business goals?
   - Too fragmented? (too many small campaigns)
   - Too consolidated? (everything in one campaign)
   - Naming conventions consistent?

2. **Ad Group Organization**
   - Keywords relevant to ads and landing pages?
   - Too few keywords per ad group (< 3)?
   - Keywords spanning multiple product categories?

3. **Network Settings**
   - Search campaigns opted into Search Partners? (often lower quality)
   - Display network enabled on search campaigns? (usually bad)

4. **Geographic Targeting**
   - Aligned with business service areas?
   - Location options (presence vs. interest)?

### Common Issues

| Issue | Diagnosis | Recommendation |
|-------|-----------|----------------|
| 2-3 keywords per ad group | Over-segmented | Consolidate similar themes |
| 1 ad group with 50+ keywords | Under-segmented | Split by theme/intent |
| Search Partners enabled | Often lower quality traffic | Test turning off |
| Display on Search | Misaligned intent | Disable |

---

## Phase 4: Quality Score Analysis

### Understanding Quality Score Components

| Component | Weight | What It Measures |
|-----------|--------|------------------|
| Expected CTR | ~65% | Historical click-through rate performance |
| Ad Relevance | ~25% | Keyword-to-ad relevance |
| Landing Page Experience | ~10% | Page quality, load time, relevance |

### Quality Score Interpretation

| Score | Assessment | Action |
|-------|------------|--------|
| 1 | Critical - likely not serving | Investigate immediately; often landing page issue |
| 2-3 | Bad but salvageable | Work on all components |
| 4-6 | Average | Improve CTR and relevance |
| 7-8 | Good | Maintain, minor optimizations |
| 9-10 | Excellent | Protect, don't change unnecessarily |

### Key Insight

> "I have never in my life seen a Google Ads account that was really well put together, that was highly profitable, that did not have a serious negative keyword strategy. Many of the accounts we manage have more negative keywords than positive keywords."

**Target:** 1:1 ratio of negative to positive keywords.

### When to Ignore Low Quality Scores

- Certain industries have "glass ceilings" (legal, financial, pharmaceutical)
- Brand keywords often have naturally lower QS
- Very low volume keywords may not have enough data

---

## Phase 5: Bid Strategy Analysis

### Bid Strategy Audit Questions

1. What bid strategy is being used?
2. Is it appropriate for the campaign's goals and data volume?
3. If using targets (CPA/ROAS), what are targets vs. actuals?

### Bid Strategy Appropriateness

| Bid Strategy | Best For | Requirements |
|--------------|----------|--------------|
| Manual CPC | New campaigns, full control needed | Time for management |
| Target CPA | Lead gen, consistent conversion values | 2-3+ conversions/day/campaign |
| Target ROAS | E-commerce, variable order values | Revenue data, consistent volume |
| Maximize Conversions | Learning phase, volume focus | Conversion tracking |
| Maximize Conv. Value | E-commerce learning phase | Revenue tracking |

### Budget Alignment

| Bid Strategy | Minimum Daily Budget |
|--------------|---------------------|
| Target CPA | 10-15x your target CPA |
| Target ROAS | 10-15x average order value |

**Example:** $50 Target CPA = $500-750/day minimum budget

### Targets vs. Actuals Analysis

| Scenario | Interpretation |
|----------|----------------|
| Target CPA $50, Actual CPA $45 | Campaign may have room to scale |
| Target CPA $50, Actual CPA $75 | Target is too aggressive or campaign underperforming |
| Target ROAS 300%, Actual ROAS 150% | Target too aggressive, constricting spend |

---

## Phase 6: Auction Insights & Competition

### Key Metrics

| Metric | What It Tells You |
|--------|-------------------|
| Impression Share | % of available impressions you're capturing |
| Overlap Rate | How often you compete with specific competitors |
| Position Above Rate | How often you appear above a competitor |
| Top of Page Rate | How often you appear at the top |
| IS Lost (Budget) | Volume lost due to insufficient budget |
| IS Lost (Rank) | Volume lost due to low ad rank (bids/QS) |

### Diagnostic Framework

```
Low Impression Share - Why?
├── High IS Lost (Budget) → Need more budget
├── High IS Lost (Rank) → Need better QS or higher bids
└── Both → Prioritize Rank first (efficiency before scale)
```

### Competitive Intelligence

- 95% overlap rate with irrelevant competitor = one of you has a mismanaged account
- Monitor competitor aggression over time
- Use for strategic positioning decisions

---

## Phase 7: Ad Copy & Assets Audit

### RSA Analysis

**Check for:**
1. Ad Strength rating
2. Number of headlines (target: 10-15, not just 2)
3. Number of descriptions (target: 4, not just 1)
4. Diversity of messages (not just repetitive with one word changed)
5. Pinned headlines (intentional strategy or mistake?)

### Extension/Asset Audit

| Extension Type | Priority | Purpose |
|----------------|----------|---------|
| Sitelinks | HIGH | Most important; adds real estate, direct links |
| Callouts | MEDIUM | USPs, benefits, promos |
| Structured Snippets | MEDIUM | Product/service categories |
| Call Extensions | HIGH (local) | Direct phone contact |
| Price Extensions | MEDIUM | Pre-qualify by showing prices |
| Location Extensions | HIGH (local) | Local business visibility |

### Common Ad Copy Issues

- Typos
- Generic, boring copy
- Missing CTAs
- Headlines not aligned with landing page
- Only 1-2 headlines written
- Only 1 description written

### Asset Performance Filter

> "Filter for assets with $300+ clicks, <3 conversions"

This identifies underperforming assets that are consuming budget.

---

## Phase 8: Budget Analysis

### What to Check

1. **Daily budget allocation across campaigns**
2. **Which campaigns are "Limited by Budget"?**
3. **Budget opportunity analysis**

### Budget Opportunity Matrix

| Status | Impression Share | Action |
|--------|------------------|--------|
| Limited by Budget | IS Lost (Budget) > 20% | Opportunity to scale if profitable |
| Not Limited | IS Lost (Budget) < 5% | Budget is sufficient |
| Limited by Rank | IS Lost (Rank) > IS Lost (Budget) | Fix efficiency before adding budget |

### Hourly Analysis

If campaigns run out of budget early in the day:
- Consider increasing budget
- Or switch to standard delivery (spread throughout day)
- Analyze which hours convert best

---

## Phase 9: Landing Page Audit

### What to Check

1. **URL Accuracy** - Are ads pointing to correct pages?
2. **Page Load Speed** - Technical performance
3. **Relevance** - Does page match ad message?
4. **Clear CTA** - Is the conversion path obvious?
5. **Mobile Experience** - Functional on mobile devices?

### Common Issues

> "We spot a ton of issues when auditing whether or not URLs are accurate. Landing pages are correct."

- Wrong landing pages (often from campaign duplication)
- 404 errors
- Slow load times
- Generic homepage instead of specific landing pages
- No clear call to action

---

## Severity Scoring System

### Severity Levels

| Level | Criteria | Examples |
|-------|----------|----------|
| **CRITICAL** | Blocking optimization, major spend waste | No conversion tracking; 50%+ spend on zero conversions; ads pointing to 404s |
| **HIGH** | Significant impact, needs attention | Poor QS keywords consuming 20%+ budget; last-click attribution; major negative keyword gaps |
| **MEDIUM** | Improvement opportunity | Missing ad extensions; suboptimal bid strategy; no Pmax campaign |
| **LOW** | Best practice, nice to have | Ad copy improvements; additional negative keywords; minor QS optimizations |

### Quantification Required

Every finding needs estimated impact:
- Wasted spend (DKK/month)
- Missed opportunity (estimated conversions)
- Efficiency gain potential (% improvement)

---

## Priority Action Plan Framework

### P0 - Immediate (Week 1)
- Critical issues blocking optimization
- Major wasted spend
- Tracking issues

### P1 - Short-Term (Month 1)
- High-impact optimizations
- Quick wins
- Structure improvements

### P2 - Medium-Term (Months 2-3)
- Strategic changes
- Testing framework setup
- Ongoing optimization cadence

---

## Quick Wins Checklist

### Conversion & Tracking
- [ ] Conversion tracking accuracy verified
- [ ] Attribution model (last-click = problem)
- [ ] Enhanced conversions enabled
- [ ] Campaigns optimizing for correct conversions

### Account Structure
- [ ] Campaign consolidation opportunities
- [ ] Campaign segmentation opportunities
- [ ] Network placements (turn off search partners/display)
- [ ] Pmax campaign launched (if not, consider)

### Keywords & Search Terms
- [ ] Negative keyword audit completed
- [ ] Search terms wasted spend identified
- [ ] N-gram analysis run
- [ ] Account-level negative list exists

### Ads & Assets
- [ ] Ad copy typos checked
- [ ] RSAs have sufficient headlines (10-15)
- [ ] RSAs have sufficient descriptions (4)
- [ ] Sitelinks present and relevant
- [ ] Callouts present
- [ ] Structured snippets (if applicable)

### Bidding & Budget
- [ ] Bid adjustments reviewed (device/location)
- [ ] ROAS/CPA targets vs. actuals analyzed
- [ ] Campaigns limited by budget identified
- [ ] Budget opportunity quantified

### Landing Pages
- [ ] URL accuracy verified
- [ ] Landing pages loading properly
- [ ] Clear CTAs present
- [ ] Pages relevant to ad messages

### Audience
- [ ] Remarketing audiences set up
- [ ] Observation audiences applied
- [ ] Audience performance analyzed

---

## Common Mistakes to Avoid

| Mistake | Correct Approach |
|---------|------------------|
| Flagging brand campaigns as "expensive" | Ask if brand bidding is intentional strategy |
| Assuming high CPA is bad | Compare to client's target and profit margin |
| Recommending changes without context | Understand recent changes and seasonality |
| Missing the forest for trees | Start with three tentpoles, then detail |
| Not quantifying impact | Every finding needs estimated DKK impact |
| Overwhelming with minor issues | Lead with Critical/High, appendix for Low |
| "Fixing" intentional strategies | Ask before changing deliberate choices |
| Ignoring time lag data | Critical for understanding account dynamics |
| Shallow search term analysis | Use filters, n-grams, quantify waste |

---

## Output Format Best Practices

### Executive Summary Structure

1. **Critical Finding** - The most important thing
2. **Key Metrics** - Current state snapshot
3. **Severity Matrix** - All findings ranked
4. **Estimated Impact** - Total wasted spend, opportunity size

### Section Structure

For each analysis section:
1. Current State (data/metrics)
2. Analysis (what this means)
3. Diagnosis (root cause)
4. Recommendation (specific fix)
5. Priority (P0/P1/P2)

### Action Plan Format

| Priority | Timeframe | Focus |
|----------|-----------|-------|
| P0 | Week 1 | Critical fixes, stop the bleeding |
| P1 | Month 1 | Quick wins, significant improvements |
| P2 | Months 2-3 | Strategic changes, testing framework |

---

## Key Quotes to Remember

> "Search terms report is the heartbeat of your entire account."

> "I have never seen a profitable account that did not have a serious negative keyword strategy."

> "If 90% of your conversions are coming in on the first day, your account is too conservative and you're probably doing a lot of brand."

> "Last-click attribution? That's a problem. It's not telling you the whole story."

> "The three tentpoles: Business understanding, Conversion tracking, Search term report."

> "Don't fix what's intentional. Ask first."

---

*This framework synthesizes methodology from the Monday Brew Google Ads course (Section 15: The Google Ads Audit Playbook) and related course materials.*
