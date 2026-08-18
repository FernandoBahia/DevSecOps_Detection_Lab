from pathlib import Path
import sys
import yaml

REQUIRED_FIELDS = {
    "title",
    "id",
    "status",
    "description",
    "author",
    "logsource",
    "detection",
    "falsepositives",
    "level",
    "tags",
}


def validate_rule(path: Path) -> list[str]:
    errors = []

    try:
        with path.open("r", encoding="utf-8") as file:
            rule = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        return [f"Invalid YAML: {exc}"]

    if not isinstance(rule, dict):
        return ["Rule must be a YAML mapping"]

    missing = REQUIRED_FIELDS - rule.keys()

    if missing:
        errors.append(
            f"Missing required fields: {', '.join(sorted(missing))}"
        )

    if "title" in rule and not isinstance(rule["title"], str):
        errors.append("Field 'title' must be a string")

    if "id" in rule and not isinstance(rule["id"], str):
        errors.append("Field 'id' must be a string")

    if "detection" in rule and not isinstance(rule["detection"], dict):
        errors.append("Field 'detection' must be a mapping")

    return errors


def main() -> int:
    sigma_dir = Path("detections/sigma")
    rules = sorted(sigma_dir.glob("*.yml"))

    if not rules:
        print("No Sigma rules found.")
        return 1

    failed = False

    for rule in rules:
        errors = validate_rule(rule)

        if errors:
            failed = True
            print(f"FAIL: {rule}")

            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS: {rule}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
