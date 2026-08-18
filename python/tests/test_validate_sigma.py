from pathlib import Path

import yaml

from python.validators.validate_sigma import validate_rule


SIGMA_RULE = Path("detections/sigma/suspicious_powershell_execution.yml")


def load_rule():
    with SIGMA_RULE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_sigma_rule_is_valid():
    errors = validate_rule(SIGMA_RULE)

    assert errors == []


def test_sigma_rule_has_powershell_selection():
    rule = load_rule()

    selection = rule["detection"]["selection"]

    assert "Image|endswith" in selection
    assert "CommandLine|contains" in selection


def test_sigma_rule_contains_encoded_command_detection():
    rule = load_rule()

    commands = rule["detection"]["selection"]["CommandLine|contains"]

    assert "-enc" in commands
    assert "-encodedcommand" in commands


def test_sigma_rule_contains_hidden_execution_detection():
    rule = load_rule()

    commands = rule["detection"]["selection"]["CommandLine|contains"]

    assert "-w hidden" in commands
    assert "-windowstyle hidden" in commands


def test_sigma_rule_has_attack_mapping():
    rule = load_rule()

    tags = rule["tags"]

    assert "attack.execution" in tags
    assert "attack.t1059.001" in tags
