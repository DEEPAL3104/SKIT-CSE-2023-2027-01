# System Validation — Student Engagement Detection System

This folder contains a lightweight, dependency-free validation suite for the repository's **web dashboard** (`index.html`, `style.css`, and `script.js`). It is designed to be committed alongside the final-year project.

## Requirements
- Python 3.9+ (uses only the Python standard library)
- Run from any directory; the runner locates the project root automatically.

## Run validation

From the repository root:

```bash
python3 System_Validation/run_validation.py
```

Or from this folder:

```bash
python3 run_validation.py
```

The command runs automated checks and writes a JSON report to `System_Validation/reports/latest_report.json`. The process exits with code `0` when all checks pass and `1` if any fail.

## What is checked
- Required project files and readable content
- HTML document metadata and key dashboard sections
- Navigation destinations and matching page sections
- Local CSS/JavaScript asset references
- Basic accessibility signals (document language, viewport, canvas label)
- JavaScript features expected by the dashboard
- Responsive CSS rules and basic safety checks against empty files

## Important scope note
These checks validate the static dashboard structure and expected client-side wiring. They do **not** prove that a webcam, machine-learning model, emotion classifier, eye-gaze detector, or video-processing pipeline works end-to-end. Those require runtime integration tests with the actual Python inference modules, model weights, camera permissions, and representative test videos. The dashboard is not treated as a substitute for model-level validation.

## Suggested workflow
1. Run validation before pushing changes.
2. Review `reports/latest_report.json`.
3. Fix failures and rerun.
4. Add real-device/model tests when the inference modules are available in this repository.

## Folder contents
- `run_validation.py` — validation runner and report writer
- `test_system_validation.py` — automated standard-library tests
- `test_cases.csv` — traceable test-case catalogue
- `VALIDATION_PLAN.md` — scope, approach, and acceptance criteria
- `BUG_REPORT_TEMPLATE.md` — reproducible issue template
- `reports/` — latest machine-readable execution report
