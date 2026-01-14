#!/usr/bin/env python3
"""
Stop Hook: Validates all phases are complete before allowing workflow to finish.

This hook BLOCKS completion unless:
1. All phase artifacts exist
2. Key content markers are present in each artifact
3. Presentation was generated (Phase 7)

Exit codes:
- 0: Approve (all phases complete)
- 2: Block (missing phases) - outputs JSON to stderr
"""

import json
import os
import sys
import re
from pathlib import Path


def is_audit_directory(path: Path) -> bool:
    """Check if directory contains audit artifacts (not just any random directory)."""
    # Audit-specific files that indicate an actual audit is in progress
    audit_markers = [
        "discovery_brief.md",
        "tracking_audit.md",
        "structure_analysis.md",
        "performance_analysis.json",
        "keyword_audit.json",
        "ad_copy_audit.json",
        "recommendations.json",
        "audit_presentation.html",
        "audit_config.json",  # If we add a config file
        ".audit-in-progress",  # Explicit marker file
    ]
    return any((path / marker).exists() for marker in audit_markers)


def find_client_dir():
    """Find the active client directory from environment or recent files.

    IMPORTANT: Only returns a directory if it contains actual audit artifacts.
    This prevents the hook from triggering in unrelated projects that happen
    to have a clients/ or audits/ folder.
    """
    # Check environment variable first (explicit override)
    client_dir = os.environ.get("MB_AUDIT_DIR")
    if client_dir and Path(client_dir).exists():
        return Path(client_dir)

    cwd = Path.cwd()

    # Check for audits directory first
    audits_dir = cwd / "audits"
    if audits_dir.exists():
        audit_dirs = [
            d for d in audits_dir.iterdir() if d.is_dir() and is_audit_directory(d)
        ]
        if audit_dirs:
            return max(audit_dirs, key=lambda d: d.stat().st_mtime)

    # Then check for clients directory
    clients_dir = cwd / "clients"
    if clients_dir.exists():
        client_dirs = [
            d for d in clients_dir.iterdir() if d.is_dir() and is_audit_directory(d)
        ]
        if client_dirs:
            return max(client_dirs, key=lambda d: d.stat().st_mtime)

    return None


def check_file_exists(path: Path) -> bool:
    """Check if file exists and is not empty."""
    return path.exists() and path.stat().st_size > 0


def check_file_contains(path: Path, patterns: list[str]) -> tuple[bool, list[str]]:
    """Check if file contains all required patterns."""
    if not path.exists():
        return False, patterns

    content = path.read_text()
    missing = []
    for pattern in patterns:
        if not re.search(pattern, content, re.IGNORECASE):
            missing.append(pattern)

    return len(missing) == 0, missing


def check_json_valid(path: Path) -> tuple[bool, str]:
    """Check if JSON file is valid."""
    if not path.exists():
        return False, "File does not exist"

    try:
        with open(path) as f:
            json.load(f)
        return True, ""
    except json.JSONDecodeError as e:
        return False, str(e)


def check_json_has_keys(path: Path, keys: list[str]) -> tuple[bool, list[str]]:
    """Check if JSON file has required top-level keys."""
    if not path.exists():
        return False, keys

    try:
        with open(path) as f:
            data = json.load(f)

        if isinstance(data, list):
            if len(data) == 0:
                return False, ["empty array"]
            data = data[0] if isinstance(data[0], dict) else {}

        missing = [k for k in keys if k not in data]
        return len(missing) == 0, missing
    except:
        return False, keys


def validate_phases(client_dir: Path) -> tuple[bool, list[dict]]:
    """Validate all phases are complete."""
    issues = []

    # Phase 0: discovery_brief.md
    phase0_file = client_dir / "discovery_brief.md"
    if not check_file_exists(phase0_file):
        issues.append(
            {
                "phase": 0,
                "severity": "block",
                "message": "Phase 0 incomplete: discovery_brief.md missing - Discovery interview required",
            }
        )
    else:
        ok, missing = check_file_contains(
            phase0_file,
            ["PRIMARY_GOAL|Business Goals", "WORKING_WELL|Working Well", "TARGET"],
        )
        if not ok:
            issues.append(
                {
                    "phase": 0,
                    "severity": "warn",
                    "message": f"Phase 0 quality: Missing sections in discovery_brief.md: {missing}",
                }
            )

    # Phase 1: tracking_audit.md
    phase1_file = client_dir / "tracking_audit.md"
    if not check_file_exists(phase1_file):
        issues.append(
            {
                "phase": 1,
                "severity": "block",
                "message": "Phase 1 incomplete: tracking_audit.md missing",
            }
        )
    else:
        ok, missing = check_file_contains(
            phase1_file, ["Conversion|tracking", "Attribution"]
        )
        if not ok:
            issues.append(
                {
                    "phase": 1,
                    "severity": "warn",
                    "message": f"Phase 1 quality: Missing sections: {missing}",
                }
            )

    # Phase 2: structure_analysis.md
    phase2_file = client_dir / "structure_analysis.md"
    if not check_file_exists(phase2_file):
        issues.append(
            {
                "phase": 2,
                "severity": "block",
                "message": "Phase 2 incomplete: structure_analysis.md missing",
            }
        )

    # Phase 3: performance_analysis.json
    phase3_file = client_dir / "performance_analysis.json"
    if not check_file_exists(phase3_file):
        issues.append(
            {
                "phase": 3,
                "severity": "block",
                "message": "Phase 3 incomplete: performance_analysis.json missing",
            }
        )
    else:
        ok, err = check_json_valid(phase3_file)
        if not ok:
            issues.append(
                {
                    "phase": 3,
                    "severity": "block",
                    "message": f"Phase 3 error: Invalid JSON - {err}",
                }
            )

    # Phase 4: keyword_audit.json
    phase4_file = client_dir / "keyword_audit.json"
    if not check_file_exists(phase4_file):
        issues.append(
            {
                "phase": 4,
                "severity": "block",
                "message": "Phase 4 incomplete: keyword_audit.json missing",
            }
        )
    else:
        ok, err = check_json_valid(phase4_file)
        if not ok:
            issues.append(
                {
                    "phase": 4,
                    "severity": "block",
                    "message": f"Phase 4 error: Invalid JSON - {err}",
                }
            )
        else:
            # Check for wasted spend calculation
            try:
                with open(phase4_file) as f:
                    data = json.load(f)
                if (
                    "total_wasted_spend" not in data
                    and "wasted_spend" not in str(data).lower()
                ):
                    issues.append(
                        {
                            "phase": 4,
                            "severity": "warn",
                            "message": "Phase 4 quality: Wasted spend calculation may be missing",
                        }
                    )
            except:
                pass

    # Phase 5: ad_copy_audit.json
    phase5_file = client_dir / "ad_copy_audit.json"
    if not check_file_exists(phase5_file):
        issues.append(
            {
                "phase": 5,
                "severity": "block",
                "message": "Phase 5 incomplete: ad_copy_audit.json missing",
            }
        )
    else:
        ok, err = check_json_valid(phase5_file)
        if not ok:
            issues.append(
                {
                    "phase": 5,
                    "severity": "block",
                    "message": f"Phase 5 error: Invalid JSON - {err}",
                }
            )

    # Phase 6: recommendations.json
    phase6_file = client_dir / "recommendations.json"
    if not check_file_exists(phase6_file):
        issues.append(
            {
                "phase": 6,
                "severity": "block",
                "message": "Phase 6 incomplete: recommendations.json missing",
            }
        )
    else:
        ok, err = check_json_valid(phase6_file)
        if not ok:
            issues.append(
                {
                    "phase": 6,
                    "severity": "block",
                    "message": f"Phase 6 error: Invalid JSON - {err}",
                }
            )
        else:
            # Check for action plan
            try:
                with open(phase6_file) as f:
                    data = json.load(f)
                required_keys = ["findings", "action_plan"]
                missing_keys = [k for k in required_keys if k not in data]
                if missing_keys:
                    issues.append(
                        {
                            "phase": 6,
                            "severity": "warn",
                            "message": f"Phase 6 quality: recommendations.json missing keys: {missing_keys}",
                        }
                    )
                # Check for P0, P1, P2 in action_plan
                if "action_plan" in data:
                    action_plan = data["action_plan"]
                    missing_priorities = [
                        p for p in ["P0", "P1", "P2"] if p not in action_plan
                    ]
                    if missing_priorities:
                        issues.append(
                            {
                                "phase": 6,
                                "severity": "warn",
                                "message": f"Phase 6 quality: Action plan missing priorities: {missing_priorities}",
                            }
                        )
            except:
                pass

    # Phase 7: audit_presentation.html
    phase7_file = client_dir / "audit_presentation.html"
    if not check_file_exists(phase7_file):
        issues.append(
            {
                "phase": 7,
                "severity": "block",
                "message": "Phase 7 incomplete: audit_presentation.html missing",
            }
        )

    # Check for blocking issues
    blocking_issues = [i for i in issues if i["severity"] == "block"]
    return len(blocking_issues) == 0, issues


def main():
    """Main entry point for stop hook."""
    # Read stdin (hook input)
    try:
        input_data = json.load(sys.stdin)
    except:
        input_data = {}

    # Find client directory
    client_dir = find_client_dir()

    if not client_dir:
        # No client directory found - might be a different workflow
        print(
            json.dumps(
                {
                    "decision": "approve",
                    "reason": "No audit directory found - not a Google Ads audit workflow",
                }
            )
        )
        sys.exit(0)

    # Validate all phases
    all_complete, issues = validate_phases(client_dir)

    if all_complete:
        warnings = [i for i in issues if i["severity"] == "warn"]
        if warnings:
            warning_msg = "; ".join([w["message"] for w in warnings])
            print(
                json.dumps(
                    {
                        "decision": "approve",
                        "reason": f"All phases complete. Warnings: {warning_msg}",
                    }
                )
            )
        else:
            print(
                json.dumps(
                    {
                        "decision": "approve",
                        "reason": "All audit phases complete and validated",
                    }
                )
            )
        sys.exit(0)
    else:
        blocking = [i for i in issues if i["severity"] == "block"]
        block_msg = "\n".join([f"- {b['message']}" for b in blocking])

        result = {
            "decision": "block",
            "reason": f"Cannot complete: {len(blocking)} phase(s) incomplete",
            "systemMessage": f"The following audit phases must be completed before finishing:\n{block_msg}",
        }
        print(json.dumps(result), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
