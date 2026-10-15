# Functional Test Plan

## Objective
Verify the visible dashboard navigation, camera-permission workflow, video-file selection, report-download action, and basic integrity of the test-video fixture. This is a functional smoke-test plan; it does not claim model accuracy.

## Environment
- macOS, Windows, or Linux; current Chrome, Firefox, or Safari
- Python 3.9+ recommended for the test runner; OpenCV is required for MP4 metadata/decode checks
- Repository root containing `index.html`, `style.css`, and `script.js`

## Test cases

| ID | Test | Steps | Expected result |
|---|---|---|---|
| FT-001 | Dashboard loads | Open `index.html` or local server URL | Dashboard renders without a blank page; stylesheet and script load |
| FT-002 | Navigation: Live Analysis | Click Live Analysis | Live section becomes visible and page title updates |
| FT-003 | Navigation: Video Analysis | Click Video Analysis | Video section becomes visible and title updates |
| FT-004 | Navigation: Reports | Click Reports | Reports section becomes visible and title updates |
| FT-005 | Return to Dashboard | Click Dashboard | Dashboard section becomes visible |
| FT-006 | Video chooser accepts MP4 | Open Video Analysis and choose `test_inputs/synthetic_test_video.mp4` | Selected filename is shown; browser does not crash |
| FT-007 | Video chooser cancellation | Open chooser and cancel | UI remains usable; no selected file is reported |
| FT-008 | Camera permission granted | Click Start Camera and allow permission | Browser preview starts and status says active |
| FT-009 | Camera permission denied | Deny camera permission, then click Start Camera | A helpful error/permission message is shown; page remains usable |
| FT-010 | Stop camera | Start camera, then click Stop Camera | Video tracks stop, preview hides, status says inactive |
| FT-011 | Report download | Click Download Report | A text report downloads and contains the demo disclaimer |
| FT-012 | Test fixture exists | Run automated test runner | MP4 fixture is present and non-empty |
| FT-013 | MP4 can be decoded | Run automated test runner with OpenCV installed | Video opens and at least one frame can be read |
| FT-014 | Required frontend assets exist | Run automated test runner | `index.html`, `style.css`, and `script.js` exist |
| FT-015 | JavaScript hooks are present | Run automated test runner | Key navigation, camera, video-input, and report hooks are found |
| FT-016 | Report generator syntax | Run automated test runner | `generate_report.py` compiles without syntax errors |
| FT-017 | Invalid/unsupported video | Select a text file renamed to `.mp4` (if UI permits) | Browser/player reports it cannot play; page remains usable |
| FT-018 | Responsive layout | Resize browser to narrow/mobile width | Content remains usable without overlapping critical controls |

## Automated run

From the repository root run:

```bash
python3 Functional_Testing/run_functional_tests.py
```

The script uses Python's built-in `unittest`. If OpenCV is installed, it additionally checks MP4 readability and frame decoding. A successful smoke test only verifies these checks; manual browser cases still need to be executed.

## Important limitation
The current dashboard uses hard-coded demonstration values. The browser camera feature previews the camera but does not stream frames into the Python AI model. Functional UI success must not be described as proof that emotion or gaze inference works.
