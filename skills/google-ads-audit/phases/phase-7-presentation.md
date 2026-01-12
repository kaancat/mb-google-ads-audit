# Phase 7: Presentation

**Status:** Delivery Phase - Client-Ready Deliverable

## Purpose

Generate the final client-facing deliverable. This phase transforms the technical analysis into a professional, actionable presentation that:

- Leads with impact (executive summary first)
- Uses the Monday Brew branded template
- Presents findings clearly with severity visualization
- Provides a clear action roadmap

---

## Prerequisites

- All Phases 0-6 completed with artifacts generated
- `recommendations.json` from Phase 6 as primary data source
- `audit_presentation.html` template available

---

## Inputs Required

1. **`recommendations.json`** - Master findings and action plan
2. **`discovery_brief.md`** - Business context
3. **Phase outputs** - For supporting details
4. **Template** - `templates/audit_presentation.html`

---

## Presentation Structure

The final deliverable follows this structure:

```
1. EXECUTIVE SUMMARY
   ├── Critical Finding Headline
   ├── Key Metrics Snapshot
   ├── Severity Matrix Summary
   └── Total Impact / Opportunity

2. ACCOUNT OVERVIEW
   ├── Account Structure Visual
   ├── Campaign Summary Table
   └── Performance Trends

3. FINDINGS BY SECTION
   ├── Tracking & Attribution
   ├── Account Structure
   ├── Performance
   ├── Keywords & Search Terms
   └── Ads & Assets

4. PRIORITY ACTION PLAN
   ├── P0: Immediate (Week 1)
   ├── P1: Short-term (Month 1)
   └── P2: Medium-term (Months 2-3)

5. QUICK WINS CHECKLIST

6. TECHNICAL APPENDICES
   ├── Negative Keyword List
   ├── Keyword Additions
   ├── Search Terms to Exclude
   └── Supporting Data Tables
```

---

## Step 1: Executive Summary

### Critical Finding Headline

Lead with the single most impactful finding:

```
IF $CRITICAL_COUNT > 0:
    → Lead with first CRITICAL finding
    → Example: "No Conversion Tracking: Unable to Measure ROI"

ELSE IF $TOTAL_WASTED_SPEND > 20% of budget:
    → Lead with wasted spend
    → Example: "45,000 DKK Wasted on Irrelevant Traffic"

ELSE:
    → Lead with highest-impact finding
    → Example: "Opportunity: Scale High-Performing Campaigns"
```

### Key Metrics Snapshot

| Metric | Value | Assessment |
|--------|-------|------------|
| Total Cost (90 days) | X DKK | - |
| Conversions | X | - |
| CPA | X DKK | vs target: +/-X% |
| ROAS | X% | vs target: +/-X% |
| Wasted Spend | X DKK | X% of budget |

### Severity Matrix

```
| Severity | Count | Total Impact |
|----------|-------|--------------|
| 🔴 CRITICAL | X | X DKK |
| 🟠 HIGH | X | X DKK |
| 🟡 MEDIUM | X | - |
| 🟢 LOW | X | - |
```

### Total Opportunity

```
Total Impact: $TOTAL_IMPACT_DKK DKK/month
Quick Wins: $QUICK_WINS_COUNT items (implementable in Week 1)
```

---

## Step 2: Account Overview

### Account Structure Visual

Create a visual representation:
- Number of campaigns by type
- Active vs. paused
- Budget distribution

### Campaign Summary Table

| Campaign | Type | Status | 90d Cost | Conv | CPA | Assessment |
|----------|------|--------|----------|------|-----|------------|
| [Name] | [Type] | [Status] | [DKK] | [X] | [DKK] | [Star/Workhorse/etc] |

### Performance Trends

If significant trends identified:
- Month-over-month comparison
- Seasonality patterns
- Recent changes impact

---

## Step 3: Findings by Section

### Section Organization

Present findings grouped by category:

```markdown
### 🔍 Tracking & Attribution

[List TRACKING_* findings]

### 🏗️ Account Structure

[List STRUCTURE_* findings]

### 📊 Performance

[List PERFORMANCE_* findings]

### 🔑 Keywords & Search Terms

[List KEYWORD_* findings]

### 📝 Ads & Assets

[List ADS_* findings]
```

### Finding Presentation Format

For each finding:

```markdown
#### [Severity Badge] [Title]

**Impact:** X DKK/month
**Category:** [Category]

**What We Found:**
[Description with evidence]

**Recommendation:**
[Specific action to take]

**Owner:** Agency / Client / Both
```

### Severity Badges

Use visual badges:
- 🔴 CRITICAL
- 🟠 HIGH
- 🟡 MEDIUM
- 🟢 LOW

---

## Step 4: Priority Action Plan

### P0: Immediate (Week 1)

```markdown
## 🚨 Week 1: Critical Fixes

Focus: Stop the bleeding

| # | Action | Owner | Impact |
|---|--------|-------|--------|
| 1 | [Action from P0] | [Owner] | [Impact] |
```

### P1: Short-term (Month 1)

```markdown
## ⚡ Month 1: High-Impact Optimizations

Focus: Quick wins and high-priority fixes

| # | Action | Owner | Impact |
|---|--------|-------|--------|
| 1 | [Action from P1] | [Owner] | [Impact] |
```

### P2: Medium-term (Months 2-3)

```markdown
## 🎯 Months 2-3: Strategic Improvements

Focus: Testing framework and optimization

| # | Action | Owner | Impact |
|---|--------|-------|--------|
| 1 | [Action from P2] | [Owner] | [Impact] |
```

---

## Step 5: Quick Wins Checklist

Create actionable checklist:

```markdown
## ✅ Quick Wins Checklist

Implementable in < 2 hours each, impact within 7 days

- [ ] [Quick Win 1] - [Expected Impact]
- [ ] [Quick Win 2] - [Expected Impact]
- [ ] [Quick Win 3] - [Expected Impact]
```

---

## Step 6: Technical Appendices

### Negative Keywords to Add

```markdown
### Account-Level Negatives

| Keyword | Match Type | Reason |
|---------|------------|--------|
| free | phrase | Low intent, 0 conversions |
```

### Keywords to Add

```markdown
### Recommended Keyword Additions

| Keyword | Match Type | Ad Group | Reason |
|---------|------------|----------|--------|
| [keyword] | [type] | [group] | Top converting search term |
```

### Search Terms to Exclude

```markdown
### Top Wasting Search Terms

| Term | Spend | Conversions | Action |
|------|-------|-------------|--------|
| [term] | X DKK | 0 | Add as negative |
```

---

## Step 7: Generate HTML

### Template Injection

Use the `audit_presentation.html` template with Handlebars-style placeholders:

| Placeholder | Data Source |
|-------------|-------------|
| `{{customer_name}}` | `metadata.customer_name` |
| `{{audit_date}}` | `metadata.audit_date` |
| `{{critical_count}}` | `summary.critical_count` |
| `{{total_wasted_spend}}` | `summary.total_wasted_spend_dkk` |
| `{{findings}}` | Loop over `findings` array |
| `{{action_plan_p0}}` | `action_plan.P0.items` |

### Styling

The template uses Monday Brew dark mode styling:
- Background: `#000000`
- Primary text: `#f5f5f5`
- Accent: `#e39712` (gold)
- Severity colors:
  - Critical: `#ef4444` (red)
  - High: `#f97316` (orange)
  - Medium: `#eab308` (yellow)
  - Low: `#22c55e` (green)

### Responsive Design

Template includes:
- Print-optimized styles
- Mobile-responsive layout
- Collapsible sections for appendices

---

## Data Validation Before Generation

### Required Data Checks

Before generating the final presentation:

```
CHECK: summary.critical_count is defined
CHECK: summary.total_wasted_spend_dkk is defined
CHECK: findings array is not empty
CHECK: action_plan.P0, P1, P2 all have items
CHECK: Each finding has: id, title, severity, category, recommendation
CHECK: Each P0/P1/P2 item has: finding_id, action, owner
```

If any check fails: **STOP and fix the data in Phase 6.**

---

## Checkpoint: Phase 7 Complete

Before marking the audit complete, ALL checkboxes must be checked:

- [ ] Executive summary has critical finding headline
- [ ] Key metrics snapshot populated
- [ ] Severity matrix shows counts by level
- [ ] Total impact displayed prominently
- [ ] Account overview section complete
- [ ] All findings organized by section
- [ ] Each finding has severity badge
- [ ] P0 action plan has all CRITICAL items
- [ ] P1 action plan has HIGH items + quick wins
- [ ] P2 action plan has MEDIUM/LOW items
- [ ] Quick wins checklist created
- [ ] Negative keywords appendix populated
- [ ] Search terms appendix populated
- [ ] HTML generated from template
- [ ] Visual styling matches Monday Brew brand
- [ ] File saved to correct location

**If ANY checkbox is incomplete: Fix before delivery.**

---

## Output Artifact

**File:** `audit_presentation.html`
**Location:** `audits/{client-name}/audit_presentation.html`

### Deployment

The HTML file is self-contained and can be:
- Opened directly in browser
- Deployed to Vercel
- Converted to PDF
- Shared via link

---

## Quality Checklist

Before delivery, verify:

### Content Quality
- [ ] Executive summary is compelling and actionable
- [ ] All DKK values are formatted correctly
- [ ] No placeholder text remains
- [ ] All findings have clear recommendations
- [ ] Action plan is realistic and prioritized

### Technical Quality
- [ ] HTML validates without errors
- [ ] All links work (if any)
- [ ] Styling renders correctly
- [ ] Print layout works

### Client Alignment
- [ ] Addresses `$SUCCESS_CRITERIA` from Phase 0
- [ ] Doesn't flag items in `$WORKING_WELL`
- [ ] Respects `$BRAND_STRATEGY` decisions
- [ ] Uses appropriate tone for client

---

*Phase 7 is what the client sees. The presentation quality reflects on the entire audit - make it professional, clear, and actionable.*
