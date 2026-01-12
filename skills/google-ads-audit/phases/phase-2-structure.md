# Phase 2: Account Structure Analysis

**Status:** Foundation Phase - Organizational Health Assessment

## Purpose

Assess organizational health and alignment with business goals. A well-structured account enables efficient optimization; a poorly structured one creates management overhead and budget fragmentation.

---

## Prerequisites

- Phase 0 completed with `discovery_brief.md` generated
- Phase 1 completed with `tracking_audit.md` generated
- `$CANONICAL_SERVICES` list from Phase 0
- `$AUDIT_FOCUS` from Phase 0

---

## Inputs Required

1. **Campaign data** - All campaigns with settings
2. **Ad group data** - All ad groups with settings
3. **Network settings** - Search partners, Display Network
4. **Geographic targeting** - Location targeting settings
5. **Naming conventions** - Campaign and ad group names

---

## Step 1: Campaign Hierarchy Review

### Fetch and Document

1. **List all campaigns**
   - Name
   - Type (Search, Display, Performance Max, Shopping, etc.)
   - Status (Enabled/Paused/Removed)
   - Budget (daily)
   - Network settings

2. **Count and Assess**
   - Total number of campaigns
   - Campaigns per type
   - Active vs. paused ratio

### Decision Tree: Campaign Count Assessment

```
Total Campaign Count
├── 1-3 campaigns
│   ├── Many ad groups per campaign?
│   │   └── MEDIUM - Potentially under-segmented
│   │   └── Check: Different products/services grouped together?
│   └── Few ad groups?
│       └── MEDIUM - Account may be under-developed
│
├── 4-10 campaigns
│   └── TYPICAL structure
│   └── Evaluate: Does structure match $CANONICAL_SERVICES?
│
├── 10-20 campaigns
│   └── More complex account
│   └── Check: Is there duplication or fragmentation?
│
└── 20+ campaigns
    └── HIGH - Potentially over-segmented
    └── Check: Are budgets fragmented?
    └── Check: Similar campaigns competing?
```

### Structure-to-Services Alignment

**CRITICAL CHECK:**

Compare campaign structure to `$CANONICAL_SERVICES` from Phase 0:

```
For each service in $CANONICAL_SERVICES:
├── Has dedicated campaign?
│   └── GOOD - Proper segmentation
│
├── Grouped with other services?
│   └── MEDIUM if high-value service
│   └── Consider: Does it warrant separation?
│
└── No campaign coverage?
    └── HIGH - Gap in coverage
    └── Document in findings
```

---

## Step 2: Ad Group Organization

### Fetch and Document

For each campaign:
1. Number of ad groups
2. Ad group names
3. Keywords per ad group
4. Theme coherence

### Decision Tree: Ad Group Assessment

```
Keywords per Ad Group
├── 1-2 keywords
│   └── Over-segmented (SKAG remnants)
│   └── MEDIUM - Consolidate unless intentional
│   └── Check $WORKING_WELL before flagging
│
├── 3-20 keywords
│   └── HEALTHY range
│   └── No action needed
│
├── 20-50 keywords
│   └── MEDIUM - Consider splitting by theme
│   └── Are keywords thematically coherent?
│
└── 50+ keywords
    └── HIGH - Under-segmented
    └── Recommendation: Split into themed groups
    └── Ad relevance likely suffering
```

### Theme Coherence Check

For each ad group with 10+ keywords:
- Are all keywords related to a single theme?
- Could keywords be split into sub-themes?
- Do keyword match types make sense together?

---

## Step 3: Naming Conventions

### Assess Consistency

1. **Campaign naming**
   - Pattern detection (Brand/Non-brand, Service, Location, etc.)
   - Consistency across campaigns
   - Clarity of purpose from name

2. **Ad group naming**
   - Theme clarity
   - Consistency within campaigns
   - Easy to understand intent

### Decision Tree: Naming Assessment

```
Naming Convention Quality
├── Consistent, descriptive pattern
│   └── GOOD
│   └── Example: "Search | Service | Geo | Intent"
│
├── Partially consistent
│   └── LOW - Room for improvement
│   └── Document pattern recommendations
│
└── No clear pattern / confusing names
    └── MEDIUM - Management inefficiency
    └── Recommendation: Implement naming convention
```

---

## Step 4: Network Settings

### Document Settings

For each campaign:
- Include Search Partners: Yes/No
- Include Display Network: Yes/No (for Search campaigns)

### Decision Tree: Network Settings

```
Search Campaign Network Settings
├── Search Partners = Yes
│   ├── Performance data available?
│   │   ├── Search Partners CTR < Google Search CTR by 50%+
│   │   │   └── MEDIUM - Consider disabling
│   │   │   └── Quantify wasted spend
│   │   └── Performance acceptable
│   │       └── No action
│   └── No segment data visible
│       └── LOW - Recommend reviewing segment
│
├── Display Network = Yes (on Search campaign)
│   └── HIGH - Almost always bad
│   └── Recommendation: Disable or split to dedicated Display campaign
│   └── Quantify Display spend on Search campaigns
│
└── Both disabled
    └── GOOD - Focused on core network
```

---

## Step 5: Geographic Targeting

### Document Settings

For each campaign:
- Target locations
- Excluded locations
- Location options (Presence vs. Interest)

### Decision Tree: Geographic Assessment

```
Geographic Targeting
├── Location Options = "People in or interested in"
│   └── HIGH - Leads to irrelevant traffic
│   └── Recommendation: Change to "Presence: People in your locations"
│   └── Exception: International e-commerce may want interest-based
│
├── Targeting matches $GEO_FOCUS?
│   ├── Yes → GOOD
│   └── No → MEDIUM
│       └── Why is targeting different from stated focus?
│       └── Check $WORKING_WELL - might be intentional
│
├── No excluded locations
│   └── LOW - Consider adding problem areas
│   └── Based on performance data
│
└── Over-broad targeting
    └── Example: All of Europe when business is local
    └── MEDIUM to HIGH based on spend waste
```

### Cross-Reference with Business Context

**CRITICAL CHECK:**

```
IF $BUSINESS_TYPE = "local-service":
    → Targeting should be local (city, region, radius)
    → National/international targeting = HIGH finding

IF $GEO_FOCUS exists:
    → Compare targeting to stated focus
    → Mismatch = MEDIUM finding (document)
```

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get structure best practices
structure_guidance = query_knowledge(
    "Google Ads account structure campaign ad group organization",
    content_type="best_practice"
)

# If over-segmented (many campaigns)
if campaign_count > 15:
    consolidation_guidance = query_knowledge(
        "campaign consolidation fragmented budgets",
        content_type="methodology"
    )

# If SKAG structure detected
if avg_keywords_per_adgroup < 3:
    skag_guidance = query_knowledge(
        "SKAG single keyword ad groups consolidation",
        content_type="best_practice"
    )
```

---

## Findings Generation

For each issue identified, create a finding with:

| Field | Value |
|-------|-------|
| `id` | F00X (continue from Phase 1) |
| `title` | Action-oriented title |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `category` | One of: `STRUCTURE_CAMPAIGN`, `STRUCTURE_ADGROUP`, `STRUCTURE_NETWORK`, `STRUCTURE_GEO` |
| `description` | Detailed explanation with data |
| `impact_dkk` | Estimated monthly DKK impact (if quantifiable) |
| `evidence` | Specific data supporting finding |
| `recommendation` | Specific action to take |

### Common Findings for This Phase

| Issue | Category | Severity | Example |
|-------|----------|----------|---------|
| Budget fragmentation | `STRUCTURE_CAMPAIGN` | HIGH | "23 campaigns, avg budget 50 DKK/day" |
| SKAG structure | `STRUCTURE_ADGROUP` | MEDIUM | "120 ad groups with 1-2 keywords each" |
| Display on Search | `STRUCTURE_NETWORK` | HIGH | "2 Search campaigns have Display enabled, X DKK spend" |
| Interest-based targeting | `STRUCTURE_GEO` | HIGH | "Using 'interested in' location targeting" |
| Service gap | `STRUCTURE_CAMPAIGN` | MEDIUM | "No campaign covering [service from $CANONICAL_SERVICES]" |
| Geographic mismatch | `STRUCTURE_GEO` | MEDIUM | "Local business targeting all of Denmark" |

---

## Checkpoint: Phase 2 Complete

Before proceeding to Phase 3, ALL checkboxes must be checked:

- [ ] All campaigns documented with settings
- [ ] Campaign count assessed against business complexity
- [ ] Ad group organization reviewed (keywords per ad group)
- [ ] Naming conventions assessed
- [ ] Network settings documented and evaluated
- [ ] Geographic targeting reviewed against `$GEO_FOCUS`
- [ ] Location options checked (Presence vs. Interest)
- [ ] Structure compared to `$CANONICAL_SERVICES`
- [ ] RAG methodology queried
- [ ] All findings have category from: `STRUCTURE_CAMPAIGN`, `STRUCTURE_ADGROUP`, `STRUCTURE_NETWORK`, `STRUCTURE_GEO`
- [ ] `structure_analysis.md` generated

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 3.**

---

## Output Artifact

**File:** `structure_analysis.md`
**Location:** `audits/{client-name}/structure_analysis.md`

### Template Structure

```markdown
# Structure Analysis: [Client Name]

**Audit Date:** [Date]
**Phase:** 2 - Account Structure

---

## Summary

| Metric | Value |
|--------|-------|
| Total Campaigns | [X] |
| Active Campaigns | [X] |
| Total Ad Groups | [X] |
| Avg Keywords/Ad Group | [X] |
| Search Partners Enabled | [X of Y campaigns] |
| Display on Search | [X of Y campaigns] |

---

## Campaign Hierarchy

| Campaign | Type | Status | Budget | Ad Groups | Networks |
|----------|------|--------|--------|-----------|----------|
| [Name] | [Type] | [Status] | [DKK] | [Count] | [Settings] |

### Assessment
[Analysis of campaign structure vs. business complexity and $CANONICAL_SERVICES]

---

## Ad Group Organization

### Keywords per Ad Group Distribution

| Range | Count | Assessment |
|-------|-------|------------|
| 1-2 | [X] | Over-segmented |
| 3-20 | [X] | Healthy |
| 20-50 | [X] | Review themes |
| 50+ | [X] | Under-segmented |

### Theme Coherence
[Analysis of ad group themes]

---

## Naming Conventions

**Campaign Pattern:** [Describe pattern or lack thereof]
**Ad Group Pattern:** [Describe pattern or lack thereof]

### Assessment
[Good/Needs improvement with recommendations]

---

## Network Settings

| Campaign | Search Partners | Display Network | Finding |
|----------|-----------------|-----------------|---------|
| [Name] | Yes/No | Yes/No | [Issue if any] |

### Impact Quantification
[If Display on Search or problematic Search Partners, quantify spend]

---

## Geographic Targeting

| Campaign | Locations | Options | Matches $GEO_FOCUS |
|----------|-----------|---------|-------------------|
| [Name] | [Locations] | Presence/Interest | Yes/No |

### Assessment
[Analysis against $GEO_FOCUS and $BUSINESS_TYPE]

---

## Service Coverage Gap Analysis

| Service (from $CANONICAL_SERVICES) | Campaign Coverage | Assessment |
|-----------------------------------|-------------------|------------|
| [Service 1] | [Campaign name or "None"] | [Gap/OK] |

---

## Findings from This Phase

[List all findings with full details]
```

---

*Phase 2 establishes the organizational foundation. Structure issues compound over time - fixing them early prevents larger problems.*
