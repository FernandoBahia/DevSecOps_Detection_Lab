from pathlib import Path
import json
import sys


def normalize_process_event(event):
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


def main():
    if len(sys.argv) != 2:
        print("Usage: python normalize_telemetry.py <json_file>")
        return 1

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"[FAIL] Telemetry file not found: {path}")
        return 1

    with path.open(encoding="utf-8") as file:
        event = json.load(file)

    normalized = normalize_process_event(event)

    print(json.dumps(normalized, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
