# Phase 0: Discovery

**Status:** GATE - Blocks all subsequent phases

## Prerequisites

None - this is the entry point for the audit workflow.

---

## Purpose

Establish the business context that shapes all subsequent data interpretation. Without this phase:
- A "high CPA" might be perfectly acceptable (high-value customers)
- Brand campaigns might be intentionally aggressive
- Geographic targeting might be strategic, not an error
- Recent changes might explain performance shifts

**A senior PPC specialist never interprets data without context.**

---

## Inputs Required

1. **Website URL** - Client's main website
2. **Google Ads Customer ID** - For data access
3. **Client interview responses** - 11 discovery questions

---

## Step 1: Website Analysis

Before asking any questions, analyze the client website.

### Actions

1. **Fetch the homepage** using WebFetch
2. **Extract internal links** from:
   - `<nav>` elements
   - `<footer>` elements
   - Service/product listings
3. **Fetch key pages:**
   - Service/product pages
   - About page
   - Contact page
   - Pricing page (if found)
4. **Try `/sitemap.xml`** for additional URLs

### Extract and Document

| Information | Where to Store |
|-------------|----------------|
| Business type | `$BUSINESS_TYPE` |
| Services/products offered | `$CANONICAL_SERVICES` |
| Geographic focus | `$GEO_FOCUS` |
| Conversion paths (forms, phone, chat) | `$CONVERSION_PATHS` |
| Available landing pages | List in brief |

### Business Type Detection

| Signals | Business Type |
|---------|---------------|
| Physical address, service area, "near me" | `local-service` |
| Product catalog, cart, checkout | `e-commerce` |
| Contact form, demo request, "get quote" | `lead-gen` |
| Free trial, pricing tiers, features | `SaaS` |
| Services page, case studies, B2B focus | `B2B` |

---

## Step 2: Discovery Interview

Ask all 11 questions. Use `AskUserQuestion` tool for structured input.

### Mandatory Questions (Q1-Q9, Q11)

#### Q1: Primary Business Goals
**Ask:** "What are your primary business goals? (Leads, Sales, Brand awareness)"
**Store as:** `$PRIMARY_GOAL`
**Options:** leads, sales, brand-awareness

#### Q2: Priority Campaigns/Services
**Ask:** "Which campaigns or services are most important to you right now?"
**Store as:** `$AUDIT_FOCUS`
**Impact:** Determines analysis depth priorities

#### Q3: What's Working Well
**Ask:** "What's working well in the account right now? Any campaigns or strategies you want to protect?"
**Store as:** `$WORKING_WELL`
**Impact:** DO NOT flag these as issues in the audit

#### Q4: Known Concerns
**Ask:** "What concerns do you have about the account? Anything specific you want investigated?"
**Store as:** `$KNOWN_CONCERNS`
**Impact:** Direct investigation targets

#### Q5: Conversion Tracking
**Ask:** "How are conversions tracked? (Form submissions, phone calls, purchases, offline imports?)"
**Store as:** `$CONVERSION_TRACKING_METHOD`
**Impact:** Understanding what data represents

#### Q6: Recent Changes
**Ask:** "What significant changes were made in the last 6 months? (New campaigns, budget changes, agency changes?)"
**Store as:** `$RECENT_CHANGES`
**Impact:** Context for performance shifts

#### Q7: Seasonality
**Ask:** "Are there seasonal patterns in your business? (Busy/slow months, annual events?)"
**Store as:** `$SEASONALITY`
**Impact:** Prevents misdiagnosing normal fluctuations

#### Q8: Brand Strategy
**Ask:** "Do you have a specific strategy for brand vs non-brand campaigns? Is brand bidding intentional?"
**Store as:** `$BRAND_STRATEGY`
**Options:** intentional, opportunistic, defensive, none
**Impact:** Don't flag intentional brand campaigns as issues

#### Q9: Profit Margin / LTV
**Ask:** "What's your profit margin or customer lifetime value? (Helps contextualize CPA recommendations)"
**Store as:** `$PROFIT_MARGIN`
**Impact:** Contextualizes whether CPA is "too high"

#### Q10: Competitors (Optional)
**Ask:** "Any competitors you're specifically watching in auctions?"
**Store as:** `$COMPETITORS`
**Impact:** Auction insights context

#### Q11: Success Criteria
**Ask:** "What would a successful audit outcome look like for you?"
**Store as:** `$SUCCESS_CRITERIA`
**Impact:** Shapes deliverable focus

---

## Step 3: Derive Target Metrics

After interview, derive or confirm target metrics.

### Target CPA / Target ROAS

**Sources (in priority order):**
1. Bid strategy targets in account
2. Calculate from historical performance
3. Ask client directly

```
If Target CPA bid strategy exists:
    $TARGET_CPA = bid_strategy_target

Else if has conversion data:
    $TARGET_CPA = 30-day average CPA

Else:
    Ask: "What's your target cost per conversion/lead?"
```

**Store as:** `$TARGET_CPA` (DKK) or `$TARGET_ROAS` (%)

---

## Step 4: Synthesize Discovery Brief

Create `discovery_brief.md` with all collected information.

### Required Sections

```markdown
# Discovery Brief: [Client Name]

**Audit Date:** [Date]
**Customer ID:** [ID]

---

## Business Context

**Business Type:** $BUSINESS_TYPE
**Primary Goal:** $PRIMARY_GOAL
**Geographic Focus:** $GEO_FOCUS

### Services/Products (Canonical List)
$CANONICAL_SERVICES

### Conversion Paths
$CONVERSION_PATHS

---

## Interview Responses

### Q1: Primary Goals
$PRIMARY_GOAL

### Q2: Priority Focus
$AUDIT_FOCUS

### Q3: What's Working Well
$WORKING_WELL

### Q4: Known Concerns
$KNOWN_CONCERNS

### Q5: Conversion Tracking
$CONVERSION_TRACKING_METHOD

### Q6: Recent Changes
$RECENT_CHANGES

### Q7: Seasonality
$SEASONALITY

### Q8: Brand Strategy
$BRAND_STRATEGY

### Q9: Profit Margin / LTV
$PROFIT_MARGIN

### Q10: Competitors
$COMPETITORS

### Q11: Success Criteria
$SUCCESS_CRITERIA

---

## Derived Targets

**Target CPA:** $TARGET_CPA DKK
**Target ROAS:** $TARGET_ROAS %

**Source:** [bid strategy / calculated / client input]

---

## Protected Areas (Do Not Flag)

Based on Q3 ($WORKING_WELL), the following should NOT be flagged as issues:
- [List items from $WORKING_WELL]

---

## Investigation Priorities

Based on Q4 ($KNOWN_CONCERNS), investigate:
- [List items from $KNOWN_CONCERNS]

---

## RAG Insights

[Include relevant methodology and patterns from RAG queries]
```

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get audit methodology
methodology = get_methodology("audit")

# Query for business-type specific patterns
patterns = query_knowledge(
    f"Google Ads audit {$BUSINESS_TYPE}",
    content_type="methodology"
)

# If concerns mentioned
if $KNOWN_CONCERNS:
    concern_guidance = query_knowledge(
        f"audit {$KNOWN_CONCERNS}",
        content_type="best_practice"
    )
```

---

## Checkpoint: Phase 0 Complete

Before proceeding to Phase 1, ALL checkboxes must be checked:

- [ ] Website analyzed
- [ ] `$CANONICAL_SERVICES` list created (minimum 3 items)
- [ ] Q1-Q9 answered (mandatory questions)
- [ ] Q11 answered (success criteria)
- [ ] Q10 answered (if competitors relevant)
- [ ] `$TARGET_CPA` or `$TARGET_ROAS` defined
- [ ] `$WORKING_WELL` documented
- [ ] `$BRAND_STRATEGY` documented
- [ ] RAG methodology queried
- [ ] `discovery_brief.md` created with all variables

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 1.**

---

## Output Artifact

**File:** `discovery_brief.md`
**Location:** `audits/{client-name}/discovery_brief.md`

---

*Phase 0 is the foundation of a quality audit. Rushing through discovery leads to misinterpretation of data.*
