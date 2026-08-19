from pathlib import Path
import json
import sys
import yaml


ROOT = Path(__file__).resolve().parents[2]
SIGMA_DIR = ROOT / "detections" / "sigma"


def load_event(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def normalize_event(event):
    process = event.get("process", {})

    image = process.get("name", "")
    command_line = process.get("command_line", "")

    if image and "\\" not in image:
        image = rf"C:\Windows\System32\{image}"

    return {
        "Image": image,
        "CommandLine": command_line,
        "User": event.get("user", ""),
        "Computer": event.get("host", ""),
        "EventType": event.get("event_type", ""),
        "Simulation": event.get("simulation", ""),
    }


def match_rule(rule, event):
    detection = rule.get("detection", {})

    selections = {}

    for name, selection in detection.items():
        if name == "condition":
            continue

        matched = True

        for field, expected in selection.items():
            if "|" in field:
                field_name, modifier = field.split("|", 1)
            else:
                field_name = field
                modifier = ""

            actual = event.get(field_name, "")

            if isinstance(actual, str):
                actual = actual.lower()

            values = expected if isinstance(expected, list) else [expected]

            if modifier == "endswith":
                field_match = any(
                    str(actual).endswith(str(value).lower())
                    for value in values
                )

            elif modifier == "contains":
                field_match = any(
                    str(value).lower() in str(actual)
                    for value in values
                )

            else:
                field_match = any(
                    str(actual).lower() == str(value).lower()
                    for value in values
                )

            if not field_match:
                matched = False
                break

        selections[name] = matched

    condition = detection.get("condition", "")

    if condition == "selection":
        return selections.get("selection", False)

    if " and " in condition:
        parts = [part.strip() for part in condition.split(" and ")]
        return all(selections.get(part, False) for part in parts)

    return False


def load_rules():
    rules = []

    for path in sorted(SIGMA_DIR.glob("*.yml")):
        with open(path, encoding="utf-8") as file:
            rule = yaml.safe_load(file)

        rules.append((path, rule))

    return rules


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m python.engine.detection_engine <telemetry.json>")
        return 1

    telemetry_path = Path(sys.argv[1])

    print("=" * 60)
    print("          DEVSECOPS DETECTION ENGINE")
    print("=" * 60)

    event = load_event(telemetry_path)
    normalized = normalize_event(event)

    print(f"[+] Telemetry: {telemetry_path}")
    print(f"[+] Event: {normalized['EventType']}")
    print(f"[+] Process: {normalized['Image']}")
    print(f"[+] Command: {normalized['CommandLine']}")
    print()

    matches = 0

    for path, rule in load_rules():
        if match_rule(rule, normalized):
            matches += 1

            print("[ALERT] DETECTION MATCH")
            print(f"  Rule: {rule.get('title')}")
            print(f"  Severity: {rule.get('level', 'unknown').upper()}")
            print(f"  Rule ID: {rule.get('id')}")
            print(f"  Simulation: {normalized['Simulation']}")
            print()

    if matches == 0:
        print("[INFO] No detection matched.")

    print("=" * 60)
    print(f"Detection matches: {matches}")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
