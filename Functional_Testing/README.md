# Functional Testing — Student Engagement Detection System

**Milestone from the project tracker:** Prepare functional test cases and a test-video input.

This folder provides a practical, repeatable test pack for the repository's current web dashboard and video-input workflow. It includes a test-case register, an offline synthetic MP4 fixture, a video-fixture generator, and automated smoke tests.

## Contents

- `test_cases.csv` — test cases with IDs, preconditions, steps, expected results, and execution status.
- `test_cases.md` — readable test plan and manual test procedure.
- `test_inputs/synthetic_test_video.mp4` — generated 8-second, 640×360 MP4 containing colored frames and labels.
- `generate_test_video.py` — regenerates the synthetic video using OpenCV.
- `run_functional_tests.py` — standard-library unittest smoke tests; OpenCV checks run when OpenCV is installed.
- `test_results_template.csv` — blank execution-results template.

## Quick start (macOS / Linux)

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install opencv-python
python Functional_Testing/run_functional_tests.py
```

Open `index.html` in a browser to manually check the dashboard, or start a local static server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. Camera access is normally allowed on `localhost`; allow permission in the browser.

## Test the video input

Use `Functional_Testing/test_inputs/synthetic_test_video.mp4` to verify that a video can be selected, opened, decoded, and played. It contains **no real person or face**. It is a safe input-validation fixture, not a valid benchmark for face detection, emotion classification, or eye-gaze accuracy. To test AI predictions, use a consented, appropriately licensed video with a clearly visible face and follow the model's supported input format.

The existing dashboard currently contains demo metrics and its camera view is a browser preview; it is not automatically connected to the Python inference scripts. Therefore the automated tests check assets and video readability, not real AI prediction correctness.

## Recording results

1. Read `test_cases.md`.
2. Execute each manual case and mark Pass/Fail/Blocked in a copy of `test_cases.csv` or `test_results_template.csv`.
3. Record browser, OS, date, tester, and screenshots/logs for failures.
4. Do not mark a case Pass unless the observed result matches its expected result.
