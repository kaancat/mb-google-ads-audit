# mb-google-ads-audit Plugin

## Overview

This plugin performs comprehensive Google Ads account audits. It analyzes existing accounts to identify issues, wasted spend, and optimization opportunities, then produces diagnostic reports with prioritized action plans.

**Key Difference from Keyword Plugin:** Audit is *diagnostic* (analyzing what exists) vs keyword research which is *creative* (building something new).

---

## Critical Rules

1. **ALWAYS query MCP RAG before starting** - Use `query_knowledge("audit")`, `get_methodology("audit")`
2. **ALWAYS scrape the client's website first** - Understand the business before interpreting data
3. **NEVER assume GA4 access** - Most audits are Google Ads only
4. **Severity ranking is mandatory** - Every finding must have Critical/High/Medium/Low severity
5. **Context shapes interpretation** - A "high CPA" is only bad if it exceeds the client's targets
6. **Don't "fix" intentional strategies** - Ask about brand campaigns, geographic targeting choices, etc.

---

## Audit Methodology (from Knowledge Base)

### Three Audit Types (Combine All Three)

| Type | Focus | Key Questions |
|------|-------|---------------|
| **Quick Wins** | Egregious errors | Missing conversion tracking? Empty RSAs? No negative keywords? |
| **Strategic** | Goal alignment | Does structure match business objectives? Scaling potential? |
| **Optimization** | Day-to-day | What should be done daily/weekly/monthly to improve? |

### The Three Tentpoles

1. **Business Understanding** - Website, competitors, goals
2. **Conversion Tracking** - Is it set up correctly?
3. **Search Term Report** - Where is spend being wasted?

### 12-Step Audit Process

1. Website analysis (1 hour minimum)
2. Competitor research
3. Conversion tracking check
4. Search term report analysis
5. Ad copy review (RSA quality, extensions)
6. Asset analysis (sitelinks, callouts, snippets)
7. Bid strategy review (targets vs actuals)
8. Quality Score analysis
9. Budget analysis (limited by budget?)
10. Landing page URL verification
11. N-gram analysis
12. Best practice checklist

---

## Discovery Phase

### Required Information

**From Website Scrape:**
- Business type (e-commerce, lead gen, local service, B2B, SaaS)
- Products/services offered
- Landing pages available
- Conversion paths (forms, phone, chat, purchase)
- Geographic focus

**From Interview (11 Questions):**
1. Primary business goals (Leads, Sales, Brand)
2. Most important campaigns/services
3. What's working well (don't break it)
4. Current concerns about the account
5. How conversions are tracked
6. Recent significant changes
7. Seasonal patterns
8. Brand vs non-brand strategy
9. Profit margin / customer LTV
10. Competitors to watch
11. Desired audit outcome

**Inferred from Account Data:**
- Target CPA/ROAS (from conversion goals and historical performance)
- Budget constraints
- Current performance baseline

---

## Data Extraction Requirements

### From Google Ads API

**Account Level:**
- Account settings
- Conversion actions (all)
- Linked accounts

**Campaign Level:**
- All campaigns with metrics (30/90/180 day windows)
- Budget status (limited by budget?)
- Bid strategies and targets
- Location targeting
- Network settings

**Ad Group Level:**
- Ad groups with metrics
- Audience targeting

**Keyword Level:**
- Keywords with Quality Score components
- Search terms report
- Negative keywords (campaign and account level)

**Ad Level:**
- All ads with strength ratings
- RSA headlines/descriptions
- Asset groups (Performance Max)

**Asset Level:**
- Sitelinks with metrics
- Callouts
- Structured snippets
- Call extensions
- Other extensions

**Audience Level:**
- Audience segments
- Demographics performance
- Device performance
- Geographic performance

**Competition:**
- Auction Insights
- Impression share data

---

## Severity Scoring System

| Level | Criteria | Example |
|-------|----------|---------|
| **CRITICAL** | Blocking optimization, major spend waste | No conversion tracking, 50%+ spend on zero conversions |
| **HIGH** | Significant impact, needs attention | Poor Quality Score keywords consuming 20%+ budget |
| **MEDIUM** | Improvement opportunity | Missing ad extensions, suboptimal bid strategy |
| **LOW** | Best practice, nice to have | Ad copy could be stronger, additional negative keywords |

### Quantification Required

Every severity rating should include estimated impact:
- Wasted spend (DKK/month)
- Missed opportunity (estimated conversions)
- Efficiency gain potential (% improvement)

---

## Output Format

### Executive Summary
```markdown
## Executive Summary

### Critical Finding: [Title]
[Brief description of most important finding]

### Key Metrics ([Period])
| Metric | Value | Assessment |
|--------|-------|------------|
| Total Cost | X DKK | - |
| Conversions | X | [Assessment] |
| CPA | X DKK | [vs target] |
| ROAS | X% | [vs target] |

### Severity Matrix
| Issue | Severity | Impact | Est. Wasted Spend |
|-------|----------|--------|-------------------|
| [Issue 1] | CRITICAL | [Impact] | X DKK |
| [Issue 2] | HIGH | [Impact] | X DKK |
```

### Section Structure
Each analysis section follows:
1. Current State (data/metrics)
2. Analysis (what this means)
3. Diagnosis (root cause)
4. Recommendation (specific fix)
5. Priority (P0/P1/P2)

### Action Plan Format
```markdown
## Priority Action Plan

### Immediate (Week 1) - P0
| # | Action | Owner | Impact |
|---|--------|-------|--------|
| 1 | [Action] | [Who] | [Impact emoji + description] |

### Short-Term (Month 1) - P1
...

### Medium-Term (Months 2-3) - P2
...
```

---

## Available Services

### From Google Ads - Monday Brew Project

```python
# Add to Python path
import sys
sys.path.insert(0, "/path/to/Google Ads - mondaybrew")

from backend.services.ads_connector import GoogleAdsConnector
from backend.scripts.audit_account import audit_account

# Full audit data fetch
audit_data = audit_account(customer_id="123-456-7890", days=180)
```

### MCP RAG Tools

```
query_knowledge("audit checklist", n_results=10)
get_methodology("audit")
get_example("nmd_law")  # if available
```

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

---

## Reference Examples

- `nmd_audit_6month_20251201.md` - Comprehensive 6-month audit example
- `karim_design_audit.md` - Shorter audit example
- `audit_account.py` - Data extraction script

---

## Plugin Status

**Current Phase:** Design/Brainstorming
**Version:** 0.1.0 (pre-release)

See `README.md` for full design documentation and next steps.
