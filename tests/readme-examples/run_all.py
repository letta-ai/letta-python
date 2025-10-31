#!/usr/bin/env python3
"""
Script to run all README example tests programmatically.
"""

import os
import sys
import glob
import subprocess
from pathlib import Path

def main():
    print("Running all README example tests...")
    print()

    # Check if LETTA_API_KEY is set
    if not os.environ.get("LETTA_API_KEY"):
        print("Warning: LETTA_API_KEY environment variable is not set")
        print("Some tests may fail without a valid API key")
        print()

    # Get all test files
    test_dir = Path(__file__).parent
    test_files = sorted(glob.glob(str(test_dir / "[0-9]*.py")))

    passed = 0
    failed = 0
    failed_tests = []

    for test_file in test_files:
        test_name = os.path.basename(test_file)
        print("=" * 60)
        print(f"Running: {test_name}")
        print("=" * 60)

        result = subprocess.run([sys.executable, test_file])

        if result.returncode == 0:
            print(f"✓ {test_name} passed")
            passed += 1
        else:
            print(f"✗ {test_name} failed")
            failed += 1
            failed_tests.append(test_name)
        print()

    print("=" * 60)
    print("Test Results")
    print("=" * 60)
    print(f"Total: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed_tests:
        print()
        print("Failed tests:")
        for test in failed_tests:
            print(f"  - {test}")

    print("=" * 60)

    sys.exit(failed)

if __name__ == "__main__":
    main()
