"""Run system validation tests and save a machine-readable JSON report."""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEST_FILE = HERE / "test_system_validation.py"
REPORT_DIR = HERE / "reports"
REPORT_FILE = REPORT_DIR / "latest_report.json"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    command = [sys.executable, "-m", "unittest", "-v", str(TEST_FILE)]
    result = subprocess.run(command, cwd=str(HERE.parent), text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    finished = datetime.now(timezone.utc)
    output = result.stdout
    # unittest's summary is included in output; retain it for traceability.
    report = {
        "suite": "Student Engagement Detection System - Static Dashboard Validation",
        "started_at_utc": started.isoformat(),
        "finished_at_utc": finished.isoformat(),
        "status": "PASS" if result.returncode == 0 else "FAIL",
        "exit_code": result.returncode,
        "command": command,
        "output": output,
        "scope": "Static dashboard checks only; not ML accuracy or end-to-end inference validation."
    }
    REPORT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(output, end="" if output.endswith("\n") else "\n")
    print(f"Status: {report['status']}")
    print(f"JSON report: {REPORT_FILE.relative_to(HERE.parent)}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
