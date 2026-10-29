# System Validation Plan

## 1. Objective
Verify that the repository's browser-based Student Engagement AI dashboard has the expected structure and that its static assets and client-side navigation hooks are present.

## 2. Scope
**Included:** HTML structure and metadata, navigation/section mapping, local asset references, dashboard controls, accessibility basics, JavaScript wiring markers, responsive stylesheet markers.

**Not included:** actual emotion recognition accuracy, gaze estimation accuracy, camera-device compatibility, inference latency, model loading, Python backend integration, privacy/security certification, or clinical/educational validity.

## 3. Test environment
- Python 3.9 or newer
- Repository root containing `index.html`, `style.css`, and `script.js`
- No third-party Python packages required
- Browser checks should additionally be performed in current Chrome, Firefox, and Safari for release validation.

## 4. Method
1. Run `python3 System_Validation/run_validation.py`.
2. Inspect terminal results and `reports/latest_report.json`.
3. Open `index.html` in a browser and manually verify each navigation section, responsive layout, and controls.
4. For full system validation, separately test the actual ML pipeline using approved sample videos and camera access, documenting device, OS, model versions, and expected/observed outputs.

## 5. Acceptance criteria
- All automated checks pass.
- No referenced local CSS/JavaScript asset is missing.
- Every dashboard navigation target has a corresponding section.
- Report JSON is created and records pass/fail counts.
- Any failure is documented with reproduction steps and severity.

## 6. Risk and limitations
Static source checks can confirm that elements and event-handler patterns exist, but cannot prove that browser behavior or model predictions are correct. Do not report ML accuracy or performance unless measured on a documented dataset. Use consent-based sample data, minimize stored video, and avoid using automated engagement estimates as the sole basis for decisions about students.

## 7. Evidence to retain
Keep the generated JSON report, browser/version details, screenshots where appropriate, sample-input identifiers (not personal video), and linked bug reports with each project milestone.
