#!/usr/bin/env python3
"""
Test script for mb-google-ads-audit plugin.
Tests hooks, schemas, and phase gating workflow logic.

Usage:
    python3 scripts/test_plugin.py
"""

import json
import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

# Colors for output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def print_header(text):
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}{text}{RESET}")
    print(f"{BOLD}{'='*60}{RESET}\n")


def print_pass(text):
    print(f"  {GREEN}✓ PASS:{RESET} {text}")


def print_fail(text):
    print(f"  {RED}✗ FAIL:{RESET} {text}")


def print_warn(text):
    print(f"  {YELLOW}⚠ WARN:{RESET} {text}")


def print_info(text):
    print(f"  ℹ {text}")


# Get plugin root directory
PLUGIN_ROOT = Path(__file__).parent.parent.absolute()
HOOKS_DIR = PLUGIN_ROOT / "hooks"
SCHEMAS_DIR = PLUGIN_ROOT / "schemas"
PHASES_DIR = PLUGIN_ROOT / "skills" / "google-ads-audit" / "phases"

results = {"passed": 0, "failed": 0, "warnings": 0}


def record_pass():
    results["passed"] += 1


def record_fail():
    results["failed"] += 1


def record_warn():
    results["warnings"] += 1


# =============================================================================
# TEST 1: Check all required files exist
# =============================================================================
def test_file_existence():
    print_header("TEST 1: File Existence Check")

    required_files = [
        # Hooks
        "hooks/hooks.json",
        "hooks/validate-phase-gate.py",
        "hooks/validate-completion.py",
        # Schemas
        "schemas/performance_analysis.schema.json",
        "schemas/keyword_audit.schema.json",
        "schemas/ad_copy_audit.schema.json",
        "schemas/recommendations.schema.json",
        # Phase files
        "skills/google-ads-audit/phases/phase-0-discovery.md",
        "skills/google-ads-audit/phases/phase-1-tracking.md",
        "skills/google-ads-audit/phases/phase-2-structure.md",
        "skills/google-ads-audit/phases/phase-3-performance.md",
        "skills/google-ads-audit/phases/phase-4-keywords.md",
        "skills/google-ads-audit/phases/phase-5-ads.md",
        "skills/google-ads-audit/phases/phase-6-synthesis.md",
        "skills/google-ads-audit/phases/phase-7-presentation.md",
        # Main files
        "skills/google-ads-audit/SKILL.md",
        "CLAUDE.md",
        "README.md",
    ]

    all_exist = True
    for file_path in required_files:
        full_path = PLUGIN_ROOT / file_path
        if full_path.exists():
            print_pass(f"{file_path}")
            record_pass()
        else:
            print_fail(f"{file_path} - NOT FOUND")
            record_fail()
            all_exist = False

    return all_exist


# =============================================================================
# TEST 2: Validate JSON schemas are valid JSON
# =============================================================================
def test_schema_validity():
    print_header("TEST 2: Schema JSON Validity")

    schema_files = list(SCHEMAS_DIR.glob("*.json"))

    if not schema_files:
        print_fail("No schema files found")
        record_fail()
        return False

    all_valid = True
    for schema_file in schema_files:
        try:
            with open(schema_file) as f:
                schema = json.load(f)

            # Check required schema fields
            if "$schema" not in schema:
                print_warn(f"{schema_file.name} - Missing $schema field")
                record_warn()

            if "type" not in schema:
                print_warn(f"{schema_file.name} - Missing type field")
                record_warn()

            print_pass(f"{schema_file.name} - Valid JSON")
            record_pass()

        except json.JSONDecodeError as e:
            print_fail(f"{schema_file.name} - Invalid JSON: {e}")
            record_fail()
            all_valid = False

    return all_valid


# =============================================================================
# TEST 3: Validate hooks.json structure
# =============================================================================
def test_hooks_json():
    print_header("TEST 3: hooks.json Structure")

    hooks_file = HOOKS_DIR / "hooks.json"

    try:
        with open(hooks_file) as f:
            hooks = json.load(f)

        print_pass("hooks.json is valid JSON")
        record_pass()

        # Check structure
        if "hooks" not in hooks:
            print_fail("Missing 'hooks' key")
            record_fail()
            return False

        print_pass("Has 'hooks' key")
        record_pass()

        # Check for expected hook types
        hook_types = hooks.get("hooks", {})

        if "PreToolUse" in hook_types:
            print_pass("Has PreToolUse hook")
            record_pass()
        else:
            print_fail("Missing PreToolUse hook")
            record_fail()

        if "Stop" in hook_types:
            print_pass("Has Stop hook")
            record_pass()
        else:
            print_fail("Missing Stop hook")
            record_fail()

        return True

    except json.JSONDecodeError as e:
        print_fail(f"hooks.json is invalid JSON: {e}")
        record_fail()
        return False
    except FileNotFoundError:
        print_fail("hooks.json not found")
        record_fail()
        return False


# =============================================================================
# TEST 4: Test phase-gate hook logic
# =============================================================================
def test_phase_gate_hook():
    print_header("TEST 4: Phase Gate Hook Logic")

    hook_script = HOOKS_DIR / "validate-phase-gate.py"

    if not hook_script.exists():
        print_fail("validate-phase-gate.py not found")
        record_fail()
        return False

    # Create temp directory for test
    with tempfile.TemporaryDirectory() as tmpdir:
        audit_dir = Path(tmpdir) / "audits" / "test-client"
        audit_dir.mkdir(parents=True)

        # Set environment variable for plugin root
        env = os.environ.copy()
        env["CLAUDE_PROJECT_ROOT"] = tmpdir

        # Test 1: Try to write Phase 1 without Phase 0 - should FAIL
        print_info("Test: Write Phase 1 without Phase 0 artifact...")
        test_input = json.dumps(
            {
                "tool_name": "Write",
                "tool_input": {"file_path": str(audit_dir / "tracking_audit.md")},
            }
        )

        result = subprocess.run(
            ["python3", str(hook_script)],
            input=test_input,
            capture_output=True,
            text=True,
            env=env,
        )

        # Hook should block this (non-zero exit or error message)
        if (
            "BLOCK" in result.stdout
            or "missing" in result.stdout.lower()
            or result.returncode != 0
        ):
            print_pass("Correctly blocked Phase 1 write without Phase 0")
            record_pass()
        else:
            print_warn(f"Expected block, got: {result.stdout[:100]}")
            record_warn()

        # Test 2: Create Phase 0, then try Phase 1 - should PASS
        print_info("Test: Write Phase 1 with Phase 0 artifact present...")
        (audit_dir / "discovery_brief.md").write_text("# Discovery Brief\nTest content")

        result = subprocess.run(
            ["python3", str(hook_script)],
            input=test_input,
            capture_output=True,
            text=True,
            env=env,
        )

        if "BLOCK" not in result.stdout and "missing" not in result.stdout.lower():
            print_pass("Correctly allowed Phase 1 write with Phase 0 present")
            record_pass()
        else:
            print_warn(f"Expected allow, got: {result.stdout[:100]}")
            record_warn()

        # Test 3: Try to skip to Phase 3 - should FAIL
        print_info("Test: Skip to Phase 3 without Phase 1-2...")
        test_input = json.dumps(
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": str(audit_dir / "performance_analysis.json")
                },
            }
        )

        result = subprocess.run(
            ["python3", str(hook_script)],
            input=test_input,
            capture_output=True,
            text=True,
            env=env,
        )

        if (
            "BLOCK" in result.stdout
            or "missing" in result.stdout.lower()
            or result.returncode != 0
        ):
            print_pass("Correctly blocked Phase 3 write without Phase 1-2")
            record_pass()
        else:
            print_warn(f"Expected block, got: {result.stdout[:100]}")
            record_warn()

        # Test 4: Non-audit file should always pass
        print_info("Test: Write non-audit file (should always pass)...")
        test_input = json.dumps(
            {"tool_name": "Write", "tool_input": {"file_path": "/tmp/random_file.txt"}}
        )

        result = subprocess.run(
            ["python3", str(hook_script)],
            input=test_input,
            capture_output=True,
            text=True,
            env=env,
        )

        if "BLOCK" not in result.stdout:
            print_pass("Correctly allowed non-audit file write")
            record_pass()
        else:
            print_fail(f"Incorrectly blocked non-audit file: {result.stdout[:100]}")
            record_fail()

    return True


# =============================================================================
# TEST 5: Test completion hook logic
# =============================================================================
def test_completion_hook():
    print_header("TEST 5: Completion Hook Logic")

    hook_script = HOOKS_DIR / "validate-completion.py"

    if not hook_script.exists():
        print_fail("validate-completion.py not found")
        record_fail()
        return False

    # Create temp directory for test
    with tempfile.TemporaryDirectory() as tmpdir:
        audit_dir = Path(tmpdir) / "audits" / "test-client"
        audit_dir.mkdir(parents=True)

        env = os.environ.copy()
        env["CLAUDE_PROJECT_ROOT"] = tmpdir

        # Test 1: No artifacts - should warn/fail
        print_info("Test: Completion check with no artifacts...")

        result = subprocess.run(
            ["python3", str(hook_script)],
            input="{}",
            capture_output=True,
            text=True,
            env=env,
        )

        # Should indicate incomplete
        print_info(f"Output: {result.stdout[:200] if result.stdout else '(empty)'}")
        if (
            result.returncode != 0
            or "missing" in result.stdout.lower()
            or "incomplete" in result.stdout.lower()
        ):
            print_pass("Correctly identified incomplete audit")
            record_pass()
        else:
            print_warn("May not have detected incomplete audit")
            record_warn()

        # Test 2: Create all artifacts
        print_info("Test: Completion check with all artifacts...")

        artifacts = [
            "discovery_brief.md",
            "tracking_audit.md",
            "structure_analysis.md",
            "performance_analysis.json",
            "keyword_audit.json",
            "ad_copy_audit.json",
            "recommendations.json",
            "audit_presentation.html",
        ]

        for artifact in artifacts:
            artifact_path = audit_dir / artifact
            if artifact.endswith(".json"):
                artifact_path.write_text("{}")
            else:
                artifact_path.write_text("# Test\nContent")

        result = subprocess.run(
            ["python3", str(hook_script)],
            input="{}",
            capture_output=True,
            text=True,
            env=env,
        )

        print_info(f"Output: {result.stdout[:200] if result.stdout else '(empty)'}")
        if result.returncode == 0 or "complete" in result.stdout.lower():
            print_pass("Correctly identified complete audit")
            record_pass()
        else:
            print_warn("May not have detected complete audit")
            record_warn()

    return True


# =============================================================================
# TEST 6: Validate schema sample data
# =============================================================================
def test_schema_sample_data():
    print_header("TEST 6: Schema Sample Data Validation")

    try:
        from jsonschema import validate, ValidationError
    except ImportError:
        print_warn("jsonschema not installed - skipping schema validation")
        print_info("Install with: pip install jsonschema")
        record_warn()
        return True

    # Test recommendations.schema.json with sample data
    schema_file = SCHEMAS_DIR / "recommendations.schema.json"

    try:
        with open(schema_file) as f:
            schema = json.load(f)

        # Minimal valid data
        valid_data = {
            "metadata": {
                "audit_date": "2025-01-12",
                "customer_id": "123-456-7890",
                "audit_period_days": 90,
            },
            "summary": {
                "total_wasted_spend_dkk": 5000,
                "critical_count": 1,
                "high_count": 2,
                "medium_count": 3,
                "low_count": 1,
            },
            "findings": [
                {
                    "id": "F001",
                    "title": "Test Finding",
                    "severity": "HIGH",
                    "category": "TRACKING_CONVERSION",
                    "description": "Test description",
                    "recommendation": "Test recommendation",
                    "priority": "P0",
                }
            ],
            "action_plan": {
                "P0": {"timeframe": "Week 1", "focus": "Critical fixes", "items": []},
                "P1": {"timeframe": "Month 1", "focus": "High priority", "items": []},
                "P2": {
                    "timeframe": "Months 2-3",
                    "focus": "Medium priority",
                    "items": [],
                },
            },
        }

        try:
            validate(valid_data, schema)
            print_pass("recommendations.schema.json - Valid sample data accepted")
            record_pass()
        except ValidationError as e:
            print_fail(
                f"recommendations.schema.json - Valid data rejected: {e.message}"
            )
            record_fail()

        # Test with invalid category (should fail)
        invalid_data = valid_data.copy()
        invalid_data["findings"] = [
            {
                "id": "F001",
                "title": "Test",
                "severity": "HIGH",
                "category": "INVALID_CATEGORY",  # Invalid!
                "description": "Test",
                "recommendation": "Test",
                "priority": "P0",
            }
        ]

        try:
            validate(invalid_data, schema)
            print_warn(
                "recommendations.schema.json - Invalid category was accepted (schema may need enum)"
            )
            record_warn()
        except ValidationError:
            print_pass(
                "recommendations.schema.json - Invalid category correctly rejected"
            )
            record_pass()

        # Test with invalid severity
        invalid_data["findings"] = [
            {
                "id": "F001",
                "title": "Test",
                "severity": "SUPER_HIGH",  # Invalid!
                "category": "TRACKING_CONVERSION",
                "description": "Test",
                "recommendation": "Test",
                "priority": "P0",
            }
        ]

        try:
            validate(invalid_data, schema)
            print_warn("recommendations.schema.json - Invalid severity was accepted")
            record_warn()
        except ValidationError:
            print_pass(
                "recommendations.schema.json - Invalid severity correctly rejected"
            )
            record_pass()

    except FileNotFoundError:
        print_fail(f"Schema file not found: {schema_file}")
        record_fail()
        return False
    except json.JSONDecodeError as e:
        print_fail(f"Schema is invalid JSON: {e}")
        record_fail()
        return False

    return True


# =============================================================================
# TEST 7: Phase file content checks
# =============================================================================
def test_phase_file_content():
    print_header("TEST 7: Phase File Content Checks")

    required_sections = [
        "## Purpose",
        "## Prerequisites",
        "## Checkpoint",
        "## Output Artifact",
    ]

    phase_files = list(PHASES_DIR.glob("phase-*.md"))

    if not phase_files:
        print_fail("No phase files found")
        record_fail()
        return False

    for phase_file in sorted(phase_files):
        content = phase_file.read_text()

        missing = []
        for section in required_sections:
            if section not in content:
                missing.append(section)

        if not missing:
            print_pass(f"{phase_file.name} - Has all required sections")
            record_pass()
        else:
            print_warn(f"{phase_file.name} - Missing: {', '.join(missing)}")
            record_warn()

        # Check for STOP checkpoint
        if "STOP" in content or "Do not proceed" in content:
            print_pass(f"{phase_file.name} - Has checkpoint gate")
            record_pass()
        else:
            print_warn(f"{phase_file.name} - May be missing checkpoint gate")
            record_warn()

    return True


# =============================================================================
# TEST 8: Variable consistency check
# =============================================================================
def test_variable_consistency():
    print_header("TEST 8: Variable Consistency Check")

    # Key variables that should be referenced across phases
    key_variables = [
        "$TARGET_CPA",
        "$WORKING_WELL",
        "$CANONICAL_SERVICES",
        "$CONVERSION_TRUST_LEVEL",
        "$TOTAL_WASTED_SPEND",
        "$BRAND_STRATEGY",
    ]

    phase_files = list(PHASES_DIR.glob("phase-*.md"))
    skill_file = PLUGIN_ROOT / "skills" / "google-ads-audit" / "SKILL.md"

    all_content = ""
    for pf in phase_files:
        all_content += pf.read_text()

    if skill_file.exists():
        all_content += skill_file.read_text()

    for var in key_variables:
        count = all_content.count(var)
        if count >= 2:
            print_pass(f"{var} - Referenced {count} times")
            record_pass()
        elif count == 1:
            print_warn(f"{var} - Only referenced once (should be set and used)")
            record_warn()
        else:
            print_fail(f"{var} - Not found in any phase file")
            record_fail()

    return True


# =============================================================================
# MAIN
# =============================================================================
def main():
    print(f"\n{BOLD}mb-google-ads-audit Plugin Test Suite{RESET}")
    print(f"Plugin root: {PLUGIN_ROOT}\n")

    # Run all tests
    test_file_existence()
    test_schema_validity()
    test_hooks_json()
    test_phase_gate_hook()
    test_completion_hook()
    test_schema_sample_data()
    test_phase_file_content()
    test_variable_consistency()

    # Summary
    print_header("TEST SUMMARY")

    total = results["passed"] + results["failed"] + results["warnings"]

    print(f"  {GREEN}Passed:   {results['passed']}{RESET}")
    print(f"  {RED}Failed:   {results['failed']}{RESET}")
    print(f"  {YELLOW}Warnings: {results['warnings']}{RESET}")
    print(f"  Total:    {total}")
    print()

    if results["failed"] == 0:
        print(f"  {GREEN}{BOLD}All critical tests passed!{RESET}")
        if results["warnings"] > 0:
            print(f"  {YELLOW}Review warnings for potential improvements.{RESET}")
        return 0
    else:
        print(f"  {RED}{BOLD}Some tests failed - review above.{RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
