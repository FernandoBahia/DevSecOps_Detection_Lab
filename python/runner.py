from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
SIGMA_DIR = ROOT / "detections" / "sigma"
YARA_DIR = ROOT / "detections" / "yara"


def run_command(command, label):
    print(f"[+] {label}")

    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        print(f"[FAIL] {label}")
        return False

    print(f"[PASS] {label}")
    return True


def main():
    print("=" * 50)
    print("       DEVSECOPS DETECTION LAB")
    print("=" * 50)

    checks = []

    checks.append(
        run_command(
            ["sigma", "check", *map(str, SIGMA_DIR.glob("*.yml"))],
            "Sigma validation",
        )
    )

    checks.append(
        run_command(
            [sys.executable, "python/validators/validate_sigma.py"],
            "Detection structure validation",
        )
    )

    checks.append(
        run_command(
            [sys.executable, "-m", "pytest", "-q"],
            "Python detection tests",
        )
    )

    yara_rules = list(YARA_DIR.glob("*.yar"))

    if yara_rules:
        sample = ROOT / ".yara-test-sample.ps1"
        sample.write_text(
            "powershell.exe -EncodedCommand AAAABBBB\n"
            "Invoke-Expression $payload\n",
            encoding="utf-8",
        )

        try:
            for rule in yara_rules:
                checks.append(
                    run_command(
                        ["yara", str(rule), str(sample)],
                        f"YARA validation: {rule.name}",
                    )
                )
        finally:
            sample.unlink(missing_ok=True)

    print()
    print("=" * 50)

    if all(checks):
        print("Detection Pipeline: PASS")
        print("=" * 50)
        return 0

    print("Detection Pipeline: FAIL")
    print("=" * 50)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
