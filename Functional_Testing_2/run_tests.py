#!/usr/bin/env python3
"""Portable smoke tests for the SKIT student-engagement frontend project."""
from __future__ import annotations
import ast
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS: list[tuple[str, str, str]] = []


def record(name: str, status: str, detail: str = "") -> None:
    RESULTS.append((name, status, detail))
    suffix = f" — {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def test_required_files() -> None:
    required = ["index.html", "style.css", "script.js", "README.md", "generate_report.py"]
    missing = [name for name in required if not (ROOT / name).is_file()]
    if missing:
        record("Required project files", "FAIL", "Missing: " + ", ".join(missing))
    else:
        record("Required project files", "PASS", f"Found {len(required)} core files")


def test_html_hooks() -> None:
    path = ROOT / "index.html"
    if not path.is_file():
        record("HTML interface hooks", "FAIL", "index.html is missing")
        return
    content = path.read_text(encoding="utf-8", errors="replace").lower()
    checks = {
        "HTML document marker": "<!doctype html" in content or "<html" in content,
        "Stylesheet reference": "style.css" in content,
        "JavaScript reference": "script.js" in content,
        "Video-related UI wording or input": any(s in content for s in ("video", "upload", "type=\"file\"", "type='file'")),
    }
    failed = [label for label, ok in checks.items() if not ok]
    if failed:
        record("HTML interface hooks", "FAIL", "Missing checks: " + ", ".join(failed))
    else:
        record("HTML interface hooks", "PASS", f"Passed {len(checks)} static checks")


def test_js_file() -> None:
    path = ROOT / "script.js"
    if not path.is_file() or not path.read_text(encoding="utf-8", errors="replace").strip():
        record("JavaScript asset", "FAIL", "script.js missing or empty")
        return
    node = shutil.which("node")
    if not node:
        record("JavaScript syntax (Node.js)", "SKIP", "Node.js is not installed; run node --check script.js when available")
        return
    proc = subprocess.run([node, "--check", str(path)], capture_output=True, text=True)
    if proc.returncode == 0:
        record("JavaScript syntax (Node.js)", "PASS", "node --check succeeded")
    else:
        record("JavaScript syntax (Node.js)", "FAIL", (proc.stderr or proc.stdout).strip()[:500])


def test_python_syntax() -> None:
    path = ROOT / "generate_report.py"
    if not path.is_file():
        record("Report generator syntax", "FAIL", "generate_report.py is missing")
        return
    try:
        ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
        record("Report generator syntax", "PASS", "Python AST parsed successfully")
    except SyntaxError as exc:
        record("Report generator syntax", "FAIL", f"Line {exc.lineno}: {exc.msg}")


def test_test_video() -> None:
    path = HERE / "test_inputs" / "synthetic_test_video.mp4"
    if not path.is_file() or path.stat().st_size < 1024:
        record("Synthetic MP4 input", "FAIL", "Video is missing or unexpectedly small")
        return
    record("Synthetic MP4 input", "PASS", f"Present ({path.stat().st_size:,} bytes)")
    try:
        import cv2  # type: ignore
    except ImportError:
        record("MP4 frame decoding (OpenCV)", "SKIP", "Install optional dependency: python3 -m pip install opencv-python")
        return
    cap = cv2.VideoCapture(str(path))
    try:
        ok, frame = cap.read()
        if ok and frame is not None and getattr(frame, "size", 0) > 0:
            record("MP4 frame decoding (OpenCV)", "PASS", f"Decoded first frame: {frame.shape[1]}x{frame.shape[0]}")
        else:
            record("MP4 frame decoding (OpenCV)", "FAIL", "OpenCV could not decode a frame")
    finally:
        cap.release()


def main() -> int:
    print("Student Engagement Detection System — Functional Testing Pack 2")
    print(f"Project root: {ROOT}\n")
    test_required_files()
    test_html_hooks()
    test_js_file()
    test_python_syntax()
    test_test_video()
    passed = sum(status == "PASS" for _, status, _ in RESULTS)
    failed = sum(status == "FAIL" for _, status, _ in RESULTS)
    skipped = sum(status == "SKIP" for _, status, _ in RESULTS)
    print("\nSummary")
    print(f"  Passed:  {passed}")
    print(f"  Failed:  {failed}")
    print(f"  Skipped: {skipped}")
    print("\nNote: these are smoke checks, not proof of real AI inference accuracy.")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
