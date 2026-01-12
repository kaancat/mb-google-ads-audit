#!/usr/bin/env python3
"""List all accessible Google Ads accounts."""

import os
import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.services.ads_connector import AdsConnector


def list_accounts(output_format="table", search=None):
    """List all accessible Google Ads accounts.

    Args:
        output_format: 'table' for human-readable, 'json' for machine-readable
        search: Optional search string to filter accounts by name
    """
    connector = AdsConnector()
    accounts = connector.get_accessible_customers()

    if not accounts:
        print("No accessible accounts found.")
        return []

    # Filter by search term if provided
    if search:
        search_lower = search.lower()
        accounts = [a for a in accounts if search_lower in a["name"].lower()]

        if not accounts:
            print(f"No accounts found matching '{search}'")
            return []

    if output_format == "json":
        print(json.dumps(accounts, indent=2))
    else:
        print(f"\n{'Account Name':<50} {'Customer ID':<15}")
        print("-" * 65)
        for account in accounts:
            print(f"{account['name']:<50} {account['id']:<15}")
        print(f"\nTotal: {len(accounts)} account(s)")

    return accounts


if __name__ == "__main__":
    load_dotenv(Path.home() / ".mondaybrew" / ".env")

    parser = argparse.ArgumentParser(description="List accessible Google Ads accounts")
    parser.add_argument(
        "--format",
        choices=["table", "json"],
        default="table",
        help="Output format (default: table)",
    )
    parser.add_argument("--search", "-s", help="Search accounts by name")

    args = parser.parse_args()
    list_accounts(output_format=args.format, search=args.search)
