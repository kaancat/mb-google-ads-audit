# Phase 1: Conversion & Tracking Audit

**Status:** Foundation Phase - Validates Data Trustworthiness

## Purpose

Verify data trustworthiness before analyzing performance. This is the fundamental question:

> **"Is the data even trustworthy?"**

> **If conversion tracking is broken, every other metric is meaningless.**

---

## Prerequisites

- Phase 0 completed with `discovery_brief.md` generated
- `$CONVERSION_TRACKING_METHOD` from Phase 0 available

---

## Inputs Required

1. **Audit data JSON** - From `output/audit_[CUSTOMER_ID]_[DATE].json`
2. **`$CONVERSION_TRACKING_METHOD`** - From Phase 0 discovery

### Data Access

All data comes from the audit JSON fetched at start of workflow:

```python
# Load the audit data
import json
with open("output/audit_[CUSTOMER_ID]_[DATE].json") as f:
    audit_data = json.load(f)

# Access conversion data
conversion_actions = audit_data["google_ads"]["conversion_actions"]
# Each action has: name, category, status, counting_method, value_settings

# Access campaign-level conversion data
campaigns = audit_data["google_ads"]["campaigns"]
# Each campaign has: conversions, conversion_value, cost

# Access change history for tracking changes
change_history = audit_data["google_ads"]["change_history"]
# Filter for conversion-related changes
```

---

## Variables Set in This Phase

| Variable | Source | Values |
|----------|--------|--------|
| `$CONVERSION_TRUST_LEVEL` | Data quality analysis | `trustworthy`, `needs-verification`, `unreliable` |
| `$ATTRIBUTION_MODEL` | Account settings | `last-click`, `data-driven`, `position-based`, etc. |
| `$DAY1_CONVERSION_PCT` | Time lag report | 0-100% |
| `$ACCOUNT_AGGRESSIVENESS` | Time lag analysis | `conservative`, `moderate`, `balanced`, `aggressive` |
| `$ENHANCED_CONVERSIONS` | Account settings | `enabled`, `disabled` |

---

## Step 1: Conversion Actions Review

### Fetch and Document

1. **List all conversion actions**
   - Name
   - Category (Lead, Purchase, Page view, etc.)
   - Status (Primary vs. Secondary)
   - Counting method (One vs. Every)
   - Value setting

2. **Classify Actions**
   - Primary conversions (actual business goals)
   - Secondary conversions (micro-conversions)
   - Campaign-level goals (if different from account-level)

3. **Verify Against Interview**
   - Compare to `$CONVERSION_TRACKING_METHOD`
   - Does the account setup match what the client described?
   - Any missing conversion types?

### Detection Rules

| Condition | Finding |
|-----------|---------|
| No conversion actions configured | **CRITICAL** - No tracking |
| Only "Page views" or engagement conversions as primary | **HIGH** - Wrong primary goal |
| Primary = lead form but no form submit action | **HIGH** - Missing key action |
| Count = "Every" for lead forms | **MEDIUM** - Potential double counting |
| No offline conversion import when mentioned in interview | **MEDIUM** - Incomplete tracking |

---

## Step 2: Attribution Model Assessment

### Document Current Model

Store as: `$ATTRIBUTION_MODEL`

Possible values:
- `last-click`
- `first-click`
- `linear`
- `time-decay`
- `position-based`
- `data-driven`

### Decision Tree: Attribution Evaluation

```
Current Attribution Model
├── last-click
│   └── SEVERITY: HIGH
│   └── Recommendation: Switch to data-driven if eligible
│   └── Impact: Undervaluing upper-funnel campaigns
│
├── first-click
│   └── SEVERITY: MEDIUM
│   └── May overvalue discovery, undervalue closing
│
├── linear / time-decay / position-based
│   └── SEVERITY: LOW
│   └── Better than last-click, but data-driven is preferred
│
└── data-driven
    └── SEVERITY: NONE
    └── Best practice - no action needed
```

### Eligibility Check for Data-Driven

- Requires 300+ conversions in 30 days OR
- 3,000+ ad interactions in 30 days
- If not eligible, document why

---

## Step 3: Time Lag Analysis

### Calculate Day 1 Conversion Percentage

1. Pull time lag report (days from click to conversion)
2. Calculate: What percentage of conversions happen on Day 1?
3. Store as: `$DAY1_CONVERSION_PCT`

### Determine Account Aggressiveness

Use this decision tree:

| `$DAY1_CONVERSION_PCT` | `$ACCOUNT_AGGRESSIVENESS` | Interpretation |
|------------------------|---------------------------|----------------|
| **> 90%** | `conservative` | Too conservative; likely brand-heavy |
| **70-90%** | `moderate` | Slightly conservative |
| **50-70%** | `balanced` | Appropriate mix |
| **< 50%** | `aggressive` | Long consideration journey |

### Cross-Reference with Brand Strategy

**CRITICAL CHECK:**

```
IF $BRAND_STRATEGY = "intentional" AND $DAY1_CONVERSION_PCT > 90%:
    → Do NOT flag as issue
    → Document: "Expected given intentional brand strategy"
    → No finding generated

ELSE IF $DAY1_CONVERSION_PCT > 90% AND $BRAND_STRATEGY != "intentional":
    → MEDIUM severity finding
    → Recommendation: Investigate non-brand performance
    → May indicate over-reliance on brand
```

Store as: `$ACCOUNT_AGGRESSIVENESS`

---

## Step 4: Enhanced Conversions Check

### Document Status

- Check if Enhanced Conversions is enabled
- Store as: `$ENHANCED_CONVERSIONS` (enabled/disabled)

### Decision Tree: Enhanced Conversions

```
Enhanced Conversions Status
├── enabled
│   └── SEVERITY: NONE
│   └── Good - improves tracking accuracy
│
└── disabled
    ├── AND $BUSINESS_TYPE = "e-commerce"
    │   └── SEVERITY: MEDIUM
    │   └── Recommendation: Enable for better attribution
    │
    └── AND $BUSINESS_TYPE = "lead-gen"
        └── SEVERITY: LOW
        └── Nice to have, but less impactful
```

---

## Step 5: Data Quality Assessment

### Compare to External Data

If available (from client or interview):
- Google Ads conversions vs. CRM/backend numbers
- Calculate discrepancy percentage

### Decision Tree: Conversion Trust Level

```
Discrepancy Analysis
├── No external data available
│   └── $CONVERSION_TRUST_LEVEL = "needs-verification"
│   └── Document: "Unable to verify conversion accuracy"
│
├── Discrepancy < 10%
│   └── $CONVERSION_TRUST_LEVEL = "trustworthy"
│   └── Data is reliable
│
├── Discrepancy 10-20%
│   └── $CONVERSION_TRUST_LEVEL = "needs-verification"
│   └── MEDIUM severity finding
│   └── Recommendation: Investigate discrepancy source
│
└── Discrepancy > 20%
    └── $CONVERSION_TRUST_LEVEL = "unreliable"
    └── HIGH severity finding
    └── ALL subsequent findings must note: "Data reliability concern"
```

Store as: `$CONVERSION_TRUST_LEVEL`

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get tracking-specific methodology
tracking_guidance = query_knowledge(
    "conversion tracking attribution audit",
    content_type="methodology"
)

# If attribution is last-click
if $ATTRIBUTION_MODEL == "last-click":
    attribution_guidance = query_knowledge(
        "last click attribution problems data driven",
        content_type="best_practice"
    )

# If enhanced conversions disabled
if $ENHANCED_CONVERSIONS == "disabled":
    enhanced_guidance = query_knowledge(
        "enhanced conversions setup benefits",
        content_type="methodology"
    )
```

---

## Findings Generation

For each issue identified, create a finding with:

| Field | Value |
|-------|-------|
| `id` | F001, F002, etc. (sequential) |
| `title` | Action-oriented title |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `category` | One of: `TRACKING_CONVERSION`, `TRACKING_ATTRIBUTION`, `TRACKING_ENHANCED`, `TRACKING_DATA_QUALITY` |
| `description` | Detailed explanation with data |
| `impact_dkk` | Estimated monthly DKK impact (if quantifiable) |
| `evidence` | Specific data supporting finding |
| `recommendation` | Specific action to take |

### Common Findings for This Phase

| Issue | Category | Severity | Example |
|-------|----------|----------|---------|
| No conversion actions | `TRACKING_CONVERSION` | CRITICAL | "Account has zero conversion actions configured" |
| Last-click attribution | `TRACKING_ATTRIBUTION` | HIGH | "Using last-click attribution with X conversions" |
| Missing primary action | `TRACKING_CONVERSION` | HIGH | "No form submission tracking despite lead gen focus" |
| Enhanced conversions disabled | `TRACKING_ENHANCED` | MEDIUM | "Enhanced conversions not enabled for e-commerce" |
| Data discrepancy >20% | `TRACKING_DATA_QUALITY` | HIGH | "33% discrepancy between Ads and CRM conversions" |

---

## Checkpoint: Phase 1 Complete

Before proceeding to Phase 2, ALL checkboxes must be checked:

- [ ] All conversion actions documented
- [ ] `$ATTRIBUTION_MODEL` set
- [ ] `$DAY1_CONVERSION_PCT` calculated
- [ ] `$ACCOUNT_AGGRESSIVENESS` determined using decision tree
- [ ] `$ENHANCED_CONVERSIONS` status documented
- [ ] `$CONVERSION_TRUST_LEVEL` assessed
- [ ] Attribution finding created (if last-click)
- [ ] Enhanced conversions finding created (if disabled + e-commerce)
- [ ] RAG methodology queried
- [ ] `tracking_audit.md` generated with all variables

**If `$CONVERSION_TRUST_LEVEL` = unreliable:**
- FLAG AS CRITICAL
- Document impact on ALL subsequent findings
- Every finding in Phases 2-5 must include disclaimer about data reliability

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 2.**

---

## Output Artifact

**File:** `tracking_audit.md`
**Location:** `audits/{client-name}/tracking_audit.md`

### Template Structure

```markdown
# Tracking Audit: [Client Name]

**Audit Date:** [Date]
**Phase:** 1 - Conversion & Tracking

---

## Summary

| Variable | Value |
|----------|-------|
| $ATTRIBUTION_MODEL | [value] |
| $DAY1_CONVERSION_PCT | [value]% |
| $ACCOUNT_AGGRESSIVENESS | [value] |
| $ENHANCED_CONVERSIONS | [value] |
| $CONVERSION_TRUST_LEVEL | [value] |

---

## Conversion Actions

| Name | Category | Status | Count | Finding |
|------|----------|--------|-------|---------|
| [Name] | [Category] | Primary/Secondary | One/Every | [Any issue] |

---

## Attribution Model

**Current Model:** $ATTRIBUTION_MODEL

[Analysis and finding if applicable]

---

## Time Lag Analysis

**Day 1 Conversion %:** $DAY1_CONVERSION_PCT
**Account Aggressiveness:** $ACCOUNT_AGGRESSIVENESS

[Analysis and cross-reference with $BRAND_STRATEGY]

---

## Enhanced Conversions

**Status:** $ENHANCED_CONVERSIONS

[Analysis and finding if applicable]

---

## Data Quality

**Trust Level:** $CONVERSION_TRUST_LEVEL

[Analysis of any discrepancies]

---

## Findings from This Phase

[List all findings with full details]

---

## Impact on Subsequent Phases

[If $CONVERSION_TRUST_LEVEL is not "trustworthy", document implications]
```

---

*Phase 1 establishes whether we can trust the data. Without trustworthy conversion tracking, all subsequent analysis is compromised.*
