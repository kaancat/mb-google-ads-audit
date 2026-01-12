# Phase 5: Ad Copy & Asset Analysis

**Status:** Analysis Phase - Creative & Extension Assessment

## Purpose

Assess ad quality and extension utilization. This phase identifies:

- Underfilled RSAs (major quick win opportunity)
- Missing extensions (easy fixes)
- Landing page alignment issues
- Asset performance problems

---

## Prerequisites

- Phase 0 completed with `discovery_brief.md` generated
- Phase 1-4 completed
- `$CANONICAL_SERVICES` from Phase 0 (for message alignment)
- `$CONVERSION_PATHS` from Phase 0 (for landing page alignment)

---

## Inputs Required

1. **Ad data** - All RSAs with headlines, descriptions, strength
2. **Asset performance** - Sitelinks, callouts, structured snippets with metrics
3. **Landing page URLs** - Final URLs from ads
4. **Ad group to keyword mapping** - For relevance assessment

---

## Step 1: RSA Strength Analysis

### Fetch and Document

For all enabled RSAs:
- Ad Strength (Excellent, Good, Average, Poor)
- Number of headlines (max 15)
- Number of descriptions (max 4)
- Impressions, clicks, conversions

### RSA Strength Distribution

| Strength | Count | % of Total |
|----------|-------|------------|
| Excellent | X | X% |
| Good | X | X% |
| Average | X | X% |
| Poor | X | X% |

### Decision Tree: RSA Evaluation

```
RSA Completeness Assessment

HEADLINES
├── 1-4 headlines
│   └── SEVERITY: CRITICAL
│   └── Severely under-filled
│   └── Quick Win: Add more headlines immediately
│
├── 5-9 headlines
│   └── SEVERITY: HIGH
│   └── Under-filled
│   └── Recommendation: Add to reach 10-15
│
└── 10-15 headlines
    └── GOOD
    └── Check diversity (see below)

DESCRIPTIONS
├── 1 description
│   └── SEVERITY: CRITICAL
│   └── Severely under-filled
│   └── Quick Win: Add 3 more descriptions
│
├── 2-3 descriptions
│   └── SEVERITY: HIGH
│   └── Under-filled
│   └── Recommendation: Add to reach 4
│
└── 4 descriptions
    └── GOOD
```

### Identify Underfilled Ads

Create list of RSAs needing attention:

| Campaign | Ad Group | Headlines | Descriptions | Strength | Severity |
|----------|----------|-----------|--------------|----------|----------|
| [Name] | [Name] | X/15 | X/4 | [Strength] | [CRITICAL/HIGH/MEDIUM] |

**Quick Win Opportunity:** Any RSA with <10 headlines or <4 descriptions is a quick win.

---

## Step 2: Message Diversity Assessment

### For Each RSA

Analyze headlines for:
- Unique value propositions
- Different angles/messages
- Keyword variation
- Call-to-action diversity

### Decision Tree: Diversity Assessment

```
Headline Diversity Check

All headlines are variations of same message?
└── MEDIUM - Lacks diversity
└── Example: All 15 headlines say "Best [Service] in [City]"
└── Recommendation: Add different angles (price, quality, speed, trust)

Duplicate headlines across ad groups?
└── LOW - Missed personalization opportunity
└── Different ad groups should have tailored messages

No CTA variation?
└── LOW - Test different CTAs
└── Examples: "Get Quote", "Call Now", "Book Today", "Learn More"
```

### Message-to-Service Alignment

Check headlines against `$CANONICAL_SERVICES`:

```
For each ad group:
├── Do headlines mention the specific service?
│   └── NO → MEDIUM finding
│   └── Generic headlines reduce ad relevance
│
└── YES → Check next ad group
```

---

## Step 3: Extension Analysis

### Document Extension Presence

For each campaign, check:

| Extension Type | Present | Count | Campaigns Missing |
|---------------|---------|-------|-------------------|
| Sitelinks | Yes/No | X | [List] |
| Callouts | Yes/No | X | [List] |
| Structured Snippets | Yes/No | X | [List] |
| Call Extension | Yes/No | 1 | [List] |
| Location Extension | Yes/No | X | [List] |

### Decision Tree: Extension Requirements

```
Core Extensions (REQUIRED)

Sitelinks
├── Present at account/campaign level?
│   ├── NO → HIGH severity
│   │   └── Quick Win: Add sitelinks
│   │   └── Estimate: +10-15% CTR improvement
│   │
│   └── YES → Check count
│       ├── < 4 sitelinks → MEDIUM
│       │   └── Target: 4-8 sitelinks
│       └── >= 4 sitelinks → GOOD

Callouts
├── Present?
│   ├── NO → MEDIUM severity
│   │   └── Quick Win: Add callouts
│   │   └── Easy USP highlights
│   │
│   └── YES → Check count
│       ├── < 4 callouts → LOW
│       └── >= 4 callouts → GOOD

Structured Snippets
├── Present?
│   ├── NO → LOW severity
│   │   └── Nice to have
│   │
│   └── YES → GOOD

Business-Specific Extensions

$BUSINESS_TYPE = "local-service"?
├── Location extension missing → MEDIUM
├── Call extension missing → MEDIUM

$BUSINESS_TYPE = "e-commerce"?
├── Price extensions missing → LOW
├── Promotion extensions missing → LOW
```

### Extension Performance Analysis

For sitelinks with significant data (1000+ impressions):

| Sitelink | Clicks | Impressions | CTR | Assessment |
|----------|--------|-------------|-----|------------|
| [Text] | X | X | X% | Good/Review |

**Performance Flags:**
- CTR < 0.5% = Review sitelink text/relevance
- 0 clicks with high impressions = Consider replacing

---

## Step 4: Landing Page Analysis

### Document Landing Pages

For each ad group or unique final URL:
- URL
- Associated keywords/themes
- Status (accessible, 404, redirect)

### Decision Tree: Landing Page Assessment

```
Landing Page Issues

HTTP Status
├── 404 Error
│   └── SEVERITY: CRITICAL
│   └── Ads pointing to broken pages
│   └── Wasting all spend on these ads
│
├── Redirect
│   └── SEVERITY: MEDIUM
│   └── Adds load time
│   └── Check: Does it go to relevant page?
│
└── 200 OK
    └── Continue checks

HTTPS Check
├── Not HTTPS?
│   └── SEVERITY: MEDIUM
│   └── Trust and ranking issues

Homepage Usage
├── % of ads pointing to homepage
│   ├── > 50% → HIGH
│   │   └── Missing dedicated landing pages
│   │   └── Reduces relevance and QS
│   │
│   └── <= 50% → Check relevance

Message Match
├── Does landing page match ad message?
│   ├── NO → MEDIUM
│   │   └── "Ad says X, landing page doesn't mention X"
│   │   └── Hurts QS and conversion rate
│   │
│   └── YES → GOOD
```

### Specific Checks

1. **Service landing pages** - Do ads for each service link to dedicated service pages?
2. **Keyword alignment** - Does the landing page content match the ad group keywords?
3. **Conversion path** - Is the conversion action clear on the landing page?

Cross-reference with `$CONVERSION_PATHS` from Phase 0.

---

## Step 5: Asset Performance Filter

### High-Spend, Low-Conversion Assets

Filter for:
- Clicks > 300 AND Conversions < 3
- OR Spend > 2x $TARGET_CPA AND Conversions = 0

### Decision Tree: Asset Performance

```
Asset Performance Issues

Clicks > 300 AND Conversions < 3
└── HIGH - Underperforming asset
└── Options:
    ├── Pause asset
    ├── Review landing page
    └── Check audience/targeting

Clicks > 1000 AND CPA > 2x $TARGET_CPA
└── MEDIUM - Significant investment, poor return
└── Deep dive: Why is this asset getting clicks but not converting?

High Impressions, Low CTR (< 1%)
└── MEDIUM - Ad copy/relevance issue
└── Review headline/description combination
```

---

## RAG Queries

Before completing this phase, query RAG:

```python
# Get RSA best practices
rsa_guidance = query_knowledge(
    "RSA responsive search ads headlines descriptions optimization",
    content_type="best_practice"
)

# Get extension guidance
extension_guidance = query_knowledge(
    "sitelinks callouts structured snippets extensions",
    content_type="methodology"
)

# Get landing page best practices
landing_guidance = query_knowledge(
    "landing page relevance ad copy alignment",
    content_type="best_practice"
)
```

---

## Findings Generation

For each issue identified, create a finding with:

| Field | Value |
|-------|-------|
| `id` | F00X (continue from Phase 4) |
| `title` | Action-oriented title |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `category` | One of: `ADS_RSA`, `ADS_EXTENSIONS`, `ADS_LANDING_PAGE` |
| `description` | Detailed explanation with data |
| `impact_dkk` | Estimated impact (if quantifiable) |
| `evidence` | Specific ads/extensions |
| `recommendation` | Specific action to take |

### Common Findings for This Phase

| Issue | Category | Severity | Example |
|-------|----------|----------|---------|
| Severely underfilled RSAs | `ADS_RSA` | CRITICAL | "8 RSAs with only 2-3 headlines" |
| Missing sitelinks | `ADS_EXTENSIONS` | HIGH | "No sitelinks on 4 campaigns" |
| 404 landing pages | `ADS_LANDING_PAGE` | CRITICAL | "3 ad groups pointing to broken URLs" |
| Homepage overuse | `ADS_LANDING_PAGE` | HIGH | "75% of ads point to homepage" |
| Missing callouts | `ADS_EXTENSIONS` | MEDIUM | "Callouts not set up for account" |

---

## Checkpoint: Phase 5 Complete

Before proceeding to Phase 6, ALL checkboxes must be checked:

- [ ] RSA strength distribution documented
- [ ] Average headlines/descriptions calculated
- [ ] Underfilled RSAs identified (<10 headlines or <4 descriptions)
- [ ] Message diversity assessed
- [ ] Headlines checked against `$CANONICAL_SERVICES`
- [ ] Sitelinks presence and performance documented
- [ ] Callouts presence documented
- [ ] Structured snippets presence documented
- [ ] Call/location extensions checked (if applicable)
- [ ] Landing page URLs verified (no 404s)
- [ ] HTTPS check completed
- [ ] Homepage usage percentage calculated
- [ ] Message match assessed
- [ ] High-spend/low-conversion assets identified
- [ ] RAG methodology queried
- [ ] `ad_copy_audit.json` generated per schema

**If ANY checkbox is incomplete: STOP. Do not proceed to Phase 6.**

---

## Output Artifact

**File:** `ad_copy_audit.json`
**Location:** `audits/{client-name}/ad_copy_audit.json`

Must conform to `schemas/ad_copy_audit.schema.json`:

```json
{
  "audit_period": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "days": 90
  },
  "summary": {
    "total_ads": 45,
    "total_ad_groups": 20,
    "avg_headlines": 8.5,
    "avg_descriptions": 3.2,
    "ads_with_poor_strength": 12,
    "extension_coverage_pct": 65
  },
  "rsa_analysis": {
    "strength_distribution": {
      "excellent": 5,
      "good": 15,
      "average": 15,
      "poor": 10
    },
    "headline_distribution": {
      "1_4": 8,
      "5_9": 20,
      "10_15": 17
    },
    "description_distribution": {
      "1": 5,
      "2_3": 25,
      "4": 15
    },
    "underfilled_ads": [
      {
        "campaign": "Campaign Name",
        "ad_group": "Ad Group Name",
        "headlines_count": 4,
        "descriptions_count": 2,
        "ad_strength": "POOR",
        "impressions": 5000,
        "clicks": 200,
        "severity": "CRITICAL"
      }
    ],
    "message_diversity": {
      "unique_headline_themes": 8,
      "duplicate_headlines_found": true,
      "assessment": "needs_improvement"
    }
  },
  "extension_analysis": {
    "sitelinks": {
      "present": true,
      "count": 6,
      "campaigns_missing": ["Campaign C"],
      "performance": [
        {
          "text": "Contact Us",
          "clicks": 500,
          "impressions": 20000,
          "ctr": 2.5
        }
      ]
    },
    "callouts": {
      "present": true,
      "count": 4,
      "campaigns_missing": []
    },
    "structured_snippets": {
      "present": false,
      "count": 0,
      "campaigns_missing": ["All campaigns"]
    },
    "call_extensions": {
      "present": true,
      "phone_number": "+45 XX XX XX XX"
    },
    "location_extensions": {
      "present": false,
      "linked_accounts": 0
    }
  },
  "landing_page_analysis": {
    "total_urls": 25,
    "unique_urls": 12,
    "issues": [
      {
        "url": "https://example.com/old-page",
        "issue_type": "404_error",
        "severity": "CRITICAL",
        "ad_group": "Ad Group Name",
        "campaign": "Campaign Name"
      }
    ],
    "homepage_usage": {
      "ads_using_homepage": 30,
      "total_ads": 45,
      "percentage": 66.7,
      "assessment": "too_high"
    }
  },
  "findings": [
    {
      "id": "F030",
      "title": "8 RSAs with critical underfill (1-4 headlines)",
      "severity": "CRITICAL",
      "category": "ADS_RSA",
      "description": "...",
      "evidence": "8 RSAs averaging 3 headlines each",
      "recommendation": "Add 10+ headlines to each underfilled RSA"
    }
  ]
}
```

---

*Phase 5 often reveals quick wins - underfilled RSAs and missing extensions can be fixed in hours with measurable impact within days.*
