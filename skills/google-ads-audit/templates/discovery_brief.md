# Discovery Brief Template

## Overview

This template captures all discovery information required before starting the Google Ads audit analysis. **ALL variables must be populated before proceeding to Phase 1.**

---

## Account Information

| Field | Variable | Value |
|-------|----------|-------|
| Customer ID | `$CUSTOMER_ID` | |
| Account Name | `$ACCOUNT_NAME` | |
| Website URL | `$WEBSITE_URL` | |
| Audit Period | `$AUDIT_PERIOD_DAYS` | 90 days (default) |
| Audit Date | `$AUDIT_DATE` | |

---

## Website Analysis Summary

**Business Profile:**

| Field | Variable | Value |
|-------|----------|-------|
| Business Type | `$BUSINESS_TYPE` | [e-commerce / lead-gen / local-service / B2B / SaaS] |
| Geographic Focus | `$GEO_FOCUS` | |
| Target Audience | `$TARGET_AUDIENCE` | |

**Canonical Services List (`$CANONICAL_SERVICES`):**

> This is the single source of truth for what the business offers. All keywords and search terms will be validated against this list.

| # | Service/Product Name | Description | Landing Page URL |
|---|---------------------|-------------|------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

*Minimum 3 services required. Add more rows as needed.*

**Conversion Paths Identified:**

- [ ] Contact Form(s)
- [ ] Phone Calls
- [ ] Email Submissions
- [ ] Online Purchases
- [ ] Chat/Messaging
- [ ] Downloads
- [ ] Other: _______________

---

## Discovery Interview Responses

### Core Questions (Q1-Q9 - MANDATORY)

| # | Question | Variable | Answer |
|---|----------|----------|--------|
| Q1 | What are your primary business goals? (Leads, Sales, Brand) | `$PRIMARY_GOAL` | |
| Q2 | Which campaigns/services are most important to you? | `$AUDIT_FOCUS` | |
| Q3 | What's working well right now? | `$WORKING_WELL` | |
| Q4 | What concerns do you have about the account? | `$KNOWN_CONCERNS` | |
| Q5 | How are conversions tracked? (Forms, calls, purchases, offline?) | `$CONVERSION_TRACKING_METHOD` | |
| Q6 | What significant changes were made in the last 6 months? | `$RECENT_CHANGES` | |
| Q7 | Are there seasonal patterns in your business? | `$SEASONALITY` | |
| Q8 | Brand vs non-brand strategy - any intentional approach? | `$BRAND_STRATEGY` | |
| Q9 | What's your profit margin or customer lifetime value? | `$PROFIT_MARGIN` | |

### Optional/Context Questions (Q10-Q11)

| # | Question | Variable | Answer |
|---|----------|----------|--------|
| Q10 | Any competitors you're specifically watching? | `$COMPETITORS` | |
| Q11 | What would a successful audit outcome look like for you? | `$SUCCESS_CRITERIA` | |

---

## Variable Validation

### `$PRIMARY_GOAL` (MANDATORY)
**Valid values:** `leads`, `sales`, `brand-awareness`

| Value | Definition | Implications for Audit |
|-------|------------|----------------------|
| `leads` | Generate leads (forms, calls, inquiries) | Focus on CPA, conversion tracking, lead quality |
| `sales` | Drive direct sales (e-commerce) | Focus on ROAS, revenue tracking, purchase funnel |
| `brand-awareness` | Build brand visibility | Focus on impression share, reach, CPM |

**Selected:** _______________

### `$BRAND_STRATEGY` (MANDATORY)
**Valid values:** `intentional`, `opportunistic`, `defensive`, `none`

| Value | Definition | Audit Impact |
|-------|------------|--------------|
| `intentional` | Brand campaigns are core strategy | Do NOT flag brand as issue. High Day1 conversion % is expected. |
| `opportunistic` | Bid on brand to capture existing searches | Review efficiency but don't criticize existence |
| `defensive` | Protect brand from competitors | Check if competitors are actually bidding |
| `none` | No brand campaigns | Flag if brand searches are being missed |

**Selected:** _______________

### `$WORKING_WELL` (MANDATORY)

> **CRITICAL: Anything listed here will be EXCLUDED from findings.**
>
> Do not "fix" what the client says is intentional or working.

List specific campaigns, strategies, or settings that should NOT be flagged:

1. _______________
2. _______________
3. _______________

### `$KNOWN_CONCERNS` (MANDATORY)

> These items get PRIORITY investigation in the audit.

List specific concerns to investigate:

1. _______________
2. _______________
3. _______________

---

## Inferred Variables

These variables are derived from account data if not provided directly:

| Variable | Source | Value | Confidence |
|----------|--------|-------|------------|
| `$TARGET_CPA` | Bid strategy settings / Historical average / Interview | | [HIGH/MEDIUM/INFERRED] |
| `$TARGET_ROAS` | Bid strategy settings / Historical average / Interview | | [HIGH/MEDIUM/INFERRED] |

**Inference Logic for `$TARGET_CPA`:**

1. Check bid strategy targets (if Target CPA strategy) → Use this value (HIGH confidence)
2. Calculate: 90-day average CPA from converting campaigns → Use as baseline (MEDIUM confidence)
3. Ask client directly → Use stated value (HIGH confidence)
4. Calculate: `$PROFIT_MARGIN` × typical order value × acceptable ratio → Estimate (INFERRED confidence)

---

## Checkpoint: Phase 0 Complete

### Mandatory Checkboxes

- [ ] Q1 answered: `$PRIMARY_GOAL` set to valid value
- [ ] Q2 answered: `$AUDIT_FOCUS` documented
- [ ] Q3 answered: `$WORKING_WELL` documented (even if "nothing specific")
- [ ] Q4 answered: `$KNOWN_CONCERNS` documented (even if "no specific concerns")
- [ ] Q5 answered: `$CONVERSION_TRACKING_METHOD` documented
- [ ] Q6 answered: `$RECENT_CHANGES` documented
- [ ] Q7 answered: `$SEASONALITY` documented
- [ ] Q8 answered: `$BRAND_STRATEGY` set to valid value
- [ ] Q9 answered: `$PROFIT_MARGIN` documented
- [ ] Q11 answered: `$SUCCESS_CRITERIA` documented (shapes deliverable focus)

### Service Validation Checkboxes

- [ ] `$CANONICAL_SERVICES` list created with minimum 3 services
- [ ] Each service has a name and description
- [ ] Landing page URLs documented (if available)

### Target Metric Checkboxes

- [ ] `$TARGET_CPA` OR `$TARGET_ROAS` defined (at least one required)
- [ ] Confidence level documented (HIGH/MEDIUM/INFERRED)

### Documentation Checkboxes

- [ ] `$BUSINESS_TYPE` set to valid value
- [ ] `$GEO_FOCUS` documented
- [ ] discovery_brief.md completed and saved

---

## Gate Validation

> **If any checkbox in "Mandatory Checkboxes" is incomplete:**
>
> ⛔ **STOP. Do not proceed to Phase 1.**
>
> Go back and complete missing items or explicitly document why they cannot be answered.

---

## Phase 0 Output Summary

**Variables Set:**
```
$CUSTOMER_ID =
$WEBSITE_URL =
$BUSINESS_TYPE =
$PRIMARY_GOAL =
$TARGET_CPA =
$TARGET_ROAS =
$GEO_FOCUS =
$BRAND_STRATEGY =
$PROFIT_MARGIN =
$WORKING_WELL = [list]
$KNOWN_CONCERNS = [list]
$CANONICAL_SERVICES = [list]
$AUDIT_FOCUS =
$SUCCESS_CRITERIA =
$CONVERSION_TRACKING_METHOD =
$RECENT_CHANGES =
$SEASONALITY =
$COMPETITORS =
```

**Ready for Phase 1:** [ ] YES / [ ] NO

If NO, document blocking issue: _______________

---

*Template version: 1.0*
*Based on: mb-keyword-analysis discovery_brief.md pattern*
