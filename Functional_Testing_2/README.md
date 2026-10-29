# Functional Testing Pack 2 — Student Engagement Detection System

This is a second, expanded functional-testing package for the existing SKIT-CSE-2023-2027-01 frontend and report generator. It is designed for GitHub and can run without installing third-party Python packages for its core checks.

## Contents

- `test_cases.csv` — expanded manual functional test cases.
- `test_plan.md` — scope, environment, preconditions, execution and exit criteria.
- `run_tests.py` — runnable standard-library test runner for project files, HTML hooks, report generator syntax and test-input presence; it optionally checks JavaScript syntax if Node.js is installed and MP4 decoding if OpenCV is installed.
- `test_inputs/synthetic_test_video.mp4` — synthetic video for upload/playback/input-pipeline checks. It contains graphics, not a real face, and cannot validate AI accuracy.
- `test_results/TEST_EXECUTION_TEMPLATE.csv` — template to record actual outcomes.
- `bug_report_template.md` — issue template for defects found during testing.

## Run

From the repository root:

```bash
python3 Functional_Testing_2/run_tests.py
```

Optional checks:

```bash
# If Node.js is installed, JavaScript syntax is checked automatically.
node --check script.js

# Optional video decode test dependency
python3 -m pip install opencv-python
python3 Functional_Testing_2/run_tests.py
```

The runner prints a summary and returns a non-zero exit code if a required smoke test fails. Optional checks are reported as skipped if their dependencies are not installed.

## Important distinction

These tests verify the local frontend artifacts and basic input-file validity. They do not claim that the browser UI is connected to real TensorFlow inference. Webcam preview, dashboard demo metrics, and AI prediction accuracy need separate end-to-end tests once a backend is integrated.
