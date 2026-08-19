# Attack Simulation

This directory contains controlled attack simulations used to generate
telemetry for the Detection as Code laboratory.

## Objectives

- Generate representative security telemetry
- Validate detection coverage
- Test Sigma and YARA detections
- Simulate attacker techniques in a controlled environment
- Support detection engineering validation

## Simulation Categories

### PowerShell

Simulations involving:

- Encoded PowerShell
- Suspicious PowerShell execution
- PowerShell download activity
- PowerShell WebClient usage

### Windows LOLBins

Simulations involving:

- certutil
- bitsadmin
- mshta
- regsvr32
- rundll32
- WMIC

### Network

Future simulations will generate network telemetry for:

- Suspicious connections
- DNS activity
- HTTP/HTTPS activity
- Command and control patterns

## Safety

All simulations are intended for controlled laboratory environments.
