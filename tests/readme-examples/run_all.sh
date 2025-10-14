#!/bin/bash

# Script to run all README example tests

echo "Running all README example tests..."
echo ""

# Check if LETTA_API_KEY is set
if [ -z "$LETTA_API_KEY" ]; then
    echo "Warning: LETTA_API_KEY environment variable is not set"
    echo "Some tests may fail without a valid API key"
    echo ""
fi

cd "$(dirname "$0")"

passed=0
failed=0
failed_tests=()

for test_file in [0-9]*.py; do
    echo "============================================================"
    echo "Running: $test_file"
    echo "============================================================"

    python "$test_file"

    if [ $? -eq 0 ]; then
        echo "✓ $test_file passed"
        ((passed++))
    else
        echo "✗ $test_file failed"
        ((failed++))
        failed_tests+=("$test_file")
    fi
    echo ""
done

echo "============================================================"
echo "Test Results"
echo "============================================================"
echo "Total: $((passed + failed))"
echo "Passed: $passed"
echo "Failed: $failed"

if [ ${#failed_tests[@]} -gt 0 ]; then
    echo ""
    echo "Failed tests:"
    for test in "${failed_tests[@]}"; do
        echo "  - $test"
    done
fi

echo "============================================================"

exit $failed
