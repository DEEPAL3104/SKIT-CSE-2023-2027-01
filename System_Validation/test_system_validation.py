"""Static system validation tests for the Student Engagement AI dashboard."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATION_DIR = Path(__file__).resolve().parent


def read_text(path):
    candidate = ROOT / path
    if not candidate.is_file():
        return ""
    return candidate.read_text(encoding="utf-8", errors="replace")


class ProjectAssetTests(unittest.TestCase):
    def test_required_dashboard_assets_exist(self):
        for relative in ("index.html", "style.css", "script.js"):
            with self.subTest(asset=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file(), f"Missing project asset: {relative}")
                self.assertGreater(path.stat().st_size, 0, f"Empty asset: {relative}")

    def test_html_metadata_is_present(self):
        html = read_text("index.html")
        self.assertRegex(html, r'<html[^>]+lang=["\']en["\']')
        self.assertRegex(html, r'<meta[^>]+charset=["\']UTF-8["\']')
        self.assertRegex(html, r'<meta[^>]+name=["\']viewport["\']')
        self.assertRegex(html, r'<title>\s*[^<]+\s*</title>')

    def test_local_css_reference_resolves(self):
        html = read_text("index.html")
        refs = re.findall(r'<link\b[^>]*href=["\']([^"\']+\.css)["\']', html, re.I)
        local_refs = [ref for ref in refs if not ref.startswith(("http://", "https://", "//"))]
        self.assertIn("style.css", local_refs)
        for ref in local_refs:
            self.assertTrue((ROOT / ref).is_file(), f"Missing local stylesheet: {ref}")

    def test_local_javascript_reference_resolves(self):
        html = read_text("index.html")
        refs = re.findall(r'<script\b[^>]*src=["\']([^"\']+\.js)["\']', html, re.I)
        local_refs = [ref for ref in refs if not ref.startswith(("http://", "https://", "//"))]
        self.assertIn("script.js", local_refs)
        for ref in local_refs:
            self.assertTrue((ROOT / ref).is_file(), f"Missing local script: {ref}")


class DashboardStructureTests(unittest.TestCase):
    def test_required_sections_exist(self):
        html = read_text("index.html")
        ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', html))
        for section in ("dashboard", "live", "video", "reports"):
            with self.subTest(section=section):
                self.assertIn(section, ids)

    def test_navigation_destinations_have_matching_sections(self):
        html = read_text("index.html")
        nav_targets = set(re.findall(r'class=["\'][^"\']*\bnav-item\b[^"\']*["\'][^>]*data-section=["\']([^"\']+)["\']', html))
        # Also support attribute ordering where data-section appears before class.
        nav_targets.update(re.findall(r'<button\b(?=[^>]*\bnav-item\b)[^>]*data-section=["\']([^"\']+)["\']', html))
        ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', html))
        self.assertTrue(nav_targets, "No navigation items with data-section were found")
        self.assertTrue(nav_targets.issubset(ids), f"Navigation targets without matching IDs: {nav_targets - ids}")

    def test_navigation_script_wiring_exists(self):
        js = read_text("script.js")
        self.assertIn("querySelectorAll('.page-section')", js)
        self.assertIn("querySelectorAll('.nav-item')", js)
        self.assertIn("addEventListener('click'", js)
        self.assertIn("showSection", js)

    def test_chart_canvas_has_script_hook(self):
        html = read_text("index.html")
        js = read_text("script.js")
        self.assertRegex(html, r'<canvas\b[^>]*id=["\']trendChart["\']')
        self.assertIn("getElementById('trendChart')", js)
        self.assertIn("getContext('2d')", js)

    def test_video_and_report_controls_exist(self):
        html = read_text("index.html")
        for control_id in ("videoInput", "downloadReport", "startCamera", "stopCamera"):
            with self.subTest(control=control_id):
                self.assertRegex(html, rf'\bid=["\']{re.escape(control_id)}["\']')

    def test_canvas_accessibility_name_exists(self):
        html = read_text("index.html")
        canvas = re.search(r'<canvas\b[^>]*>', html, re.I)
        self.assertIsNotNone(canvas, "No canvas element found")
        self.assertRegex(canvas.group(0), r'\b(aria-label|role|title)=["\'][^"\']+["\']',
                         "Canvas should have an accessible label, role, or title")

    def test_responsive_stylesheet_marker_exists(self):
        css = read_text("style.css")
        self.assertRegex(css, r'@media\s*\(', "No responsive media query found")

    def test_test_plan_and_catalog_are_present(self):
        self.assertTrue((VALIDATION_DIR / "VALIDATION_PLAN.md").is_file())
        self.assertTrue((VALIDATION_DIR / "test_cases.csv").is_file())
        self.assertTrue((VALIDATION_DIR / "BUG_REPORT_TEMPLATE.md").is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
