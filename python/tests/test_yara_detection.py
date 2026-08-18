from pathlib import Path
import subprocess


YARA_RULE = Path("detections/yara/suspicious_powershell_payload.yar")


def run_yara(sample):
    result = subprocess.run(
        ["yara", str(YARA_RULE), str(sample)],
        capture_output=True,
        text=True,
        check=False,
    )
    return result


def test_yara_rule_detects_suspicious_powershell(tmp_path):
    sample = tmp_path / "suspicious.ps1"

    sample.write_text(
        "powershell.exe -EncodedCommand AAAABBBB\n"
        "Invoke-Expression $payload\n",
        encoding="utf-8",
    )

    result = run_yara(sample)

    assert result.returncode == 0
    assert "Suspicious_PowerShell_Payload" in result.stdout


def test_yara_rule_does_not_detect_benign_powershell(tmp_path):
    sample = tmp_path / "benign.ps1"

    sample.write_text(
        "Write-Host 'Hello World'\n",
        encoding="utf-8",
    )

    result = run_yara(sample)

    assert result.returncode == 0
    assert result.stdout == ""
