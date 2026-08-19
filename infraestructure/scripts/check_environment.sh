#!/usr/bin/env bash

set -e

echo "=========================================="
echo "   DevSecOps Detection Lab Environment"
echo "=========================================="

commands=(
    git
    python
    pytest
    sigma
    yara
    docker
)

for command in "${commands[@]}"; do
    if command -v "$command" >/dev/null 2>&1; then
        echo "[PASS] $command"
    else
        echo "[FAIL] $command"
    fi
done

echo
echo "Environment check completed."
