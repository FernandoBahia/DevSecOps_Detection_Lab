# DevSecOps Detection Lab

## Overview

This project implements a Detection as Code laboratory focused on security detection engineering, automated validation and CI/CD.

## Architecture

```text
Detection Rules
      |
      +---- Sigma
      |
      +---- YARA
      |
      v
Validation
      |
      +---- Sigma CLI
      +---- Python validators
      +---- YARA
      |
      v
Automated Tests
      |
      +---- Pytest
      +---- Detection test cases
      |
      v
Detection Runner
      |
      v
Docker
      |
      v
Infrastructure
      |
      +---- Kubernetes
      |
      +---- Terraform
      |
      v
Attack Simulation
      |
      v
Telemetry
      |
      v
Detection
```

## Detection as Code

Detection rules are treated as code artifacts and are version controlled, validated, tested and integrated into CI/CD.

## Detection Technologies

- Sigma: portable log-based detection rules
- YARA: file and payload-oriented detection
- Python: validation, testing and pipeline orchestration
- Docker: reproducible detection pipeline
- Kubernetes: containerized detection laboratory
- Terraform: Infrastructure as Code
