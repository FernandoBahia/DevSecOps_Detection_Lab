from pathlib import Path

from python.validators.validate_sigma import validate_rule


SIGMA_RULE = Path("detections/sigma/suspicious_powershell_execution.yml")


def test_sigma_rule_is_valid():
    errors = validate_rule(SIGMA_RULE)

    assert errors == []