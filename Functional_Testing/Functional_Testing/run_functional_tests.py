#!/usr/bin/env python3
"""Offline functional smoke tests for the Student Engagement Detection UI."""
from pathlib import Path
import unittest
import py_compile

ROOT = Path(__file__).resolve().parents[1]
TEST_DIR = Path(__file__).resolve().parent
VIDEO = TEST_DIR / "test_inputs" / "synthetic_test_video.mp4"

class ProjectAssetTests(unittest.TestCase):
    def test_frontend_assets_exist(self):
        for name in ("index.html", "style.css", "script.js"):
            with self.subTest(asset=name):
                self.assertTrue((ROOT / name).is_file(), f"Missing required asset: {name}")

    def test_video_fixture_exists_and_nonempty(self):
        self.assertTrue(VIDEO.is_file(), f"Missing video fixture: {VIDEO}")
        self.assertGreater(VIDEO.stat().st_size, 1000, "Video fixture looks unexpectedly small")

    def test_frontend_has_expected_hooks(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        js = (ROOT / "script.js").read_text(encoding="utf-8")
        for token in ("id=\"videoInput\"", "id=\"startCamera\"", "id=\"stopCamera\"", "id=\"downloadReport\""):
            with self.subTest(token=token):
                self.assertIn(token, html)
        for token in ("getUserMedia", "downloadReport", "showSection"):
            with self.subTest(token=token):
                self.assertIn(token, js)

    def test_report_generator_syntax(self):
        report_script = ROOT / "generate_report.py"
        self.assertTrue(report_script.is_file(), "generate_report.py is missing")
        # py_compile validates syntax without executing the report generator.
        py_compile.compile(str(report_script), doraise=True)

class VideoDecodeTests(unittest.TestCase):
    def test_mp4_opens_and_decodes(self):
        try:
            import cv2
        except ImportError:
            self.skipTest("OpenCV is not installed; install with: python -m pip install opencv-python")
        capture = cv2.VideoCapture(str(VIDEO))
        try:
            self.assertTrue(capture.isOpened(), "OpenCV could not open the MP4 fixture")
            ok, frame = capture.read()
            self.assertTrue(ok, "OpenCV could not decode the first frame")
            self.assertIsNotNone(frame)
            self.assertGreater(frame.shape[0], 0)
            self.assertGreater(frame.shape[1], 0)
        finally:
            capture.release()

if __name__ == "__main__":
    unittest.main(verbosity=2)
