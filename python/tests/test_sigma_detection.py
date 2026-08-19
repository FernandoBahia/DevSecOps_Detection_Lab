from pathlib import Path
import json


TELEMETRY = Path(
    "telemetry/samples/powershell/encoded_command.json"
)


def load_event():
    with TELEMETRY.open(encoding="utf-8") as file:
        return json.load(file)


def test_encoded_powershell_telemetry_matches_detection():
    event = load_event()

    image = event["process"]["name"].lower()
    command_line = event["process"]["command_line"].lower()

    assert image in {"powershell.exe", "pwsh.exe"}

    assert (
        "-enc " in command_line
        or "-encodedcommand " in command_line
    )


def test_encoded_powershell_simulation_metadata():
    event = load_event()

    assert event["event_type"] == "process_creation"
    assert event["simulation"] == "powershell_encoded_command"


def test_benign_powershell_does_not_match_encoded_detection():
    path = Path(
        "telemetry/samples/powershell/benign_command.json"
    )

    with path.open(encoding="utf-8") as file:
        event = json.load(file)

    command_line = event["process"]["command_line"].lower()

    assert "-enc " not in command_line
    assert "-encodedcommand " not in command_line


def test_powershell_download_telemetry_matches_detection():
    path = Path(
        "telemetry/samples/powershell/download_activity.json"
    )

    with path.open(encoding="utf-8") as file:
        event = json.load(file)

    command_line = event["process"]["command_line"].lower()

    assert event["process"]["name"].lower() == "powershell.exe"
    assert "invoke-webrequest" in command_line
    assert "https://example.invalid" in command_line
    assert event["simulation"] == "powershell_download_activity"
