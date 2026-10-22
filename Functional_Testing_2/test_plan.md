# Functional Test Plan

## 1. Objective

Verify that the project frontend files are present and readable, key UI controls and expected interface sections exist, report-generation source is syntactically valid, and the supplied video input can be located and optionally decoded.

## 2. Scope

**Included:** dashboard shell, navigation labels, video input control, webcam permission messaging/hooks, report/download controls, chart containers, Python report-generator syntax, test video file checks, optional JavaScript syntax and optional MP4 decoding.

**Not established by these smoke tests:** real emotion classification, gaze accuracy, attendance correctness, model performance, browser-to-Python inference connectivity, security testing, or performance under load.

## 3. Environment

- macOS, Windows, or Linux
- Python 3.9+ recommended (core runner uses only the standard library)
- Optional: Node.js for JavaScript syntax checking
- Optional: `opencv-python` for MP4 decoding
- A modern browser for manual UI checks

## 4. Preconditions

1. Extract the repository archive.
2. Keep `index.html`, `style.css`, `script.js`, and `generate_report.py` in the repository root.
3. Keep `Functional_Testing_2/test_inputs/synthetic_test_video.mp4` at its supplied path.
4. Run the test script from the repository root or invoke it by its relative path.

## 5. Execution

Run `python3 Functional_Testing_2/run_tests.py`. Record each manual case in `test_results/TEST_EXECUTION_TEMPLATE.csv`. For browser checks, open `index.html` in a modern browser, exercise the relevant control, and record the observed result rather than marking a case passed by assumption.

## 6. Exit criteria

- All required automated smoke checks pass.
- Optional checks are either passed or clearly marked skipped with the dependency reason.
- Manual test results and any defects are recorded.
- No test is marked passed unless the expected result was actually observed.

## 7. Manual checks

1. Open the dashboard and verify layout at desktop and narrow viewport widths.
2. Navigate each sidebar item and confirm the correct section is shown or a clear action occurs.
3. Select the supplied MP4 and verify the interface accepts/displays the selected filename or preview.
4. Select an unsupported file type and verify the UI gives a clear response.
5. Deny webcam permission and verify the UI does not crash and provides a helpful message.
6. Grant webcam permission and verify preview behavior; do not assume AI inference is active.
7. Trigger report download and verify the downloaded file opens and contains expected headings/data.
8. Reload the page and verify there are no uncaught console errors.
