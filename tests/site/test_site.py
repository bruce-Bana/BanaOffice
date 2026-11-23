"""Dependency-free checks for the published BanaOffice project website."""

from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "docs" / "index.html"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.title_text = []
        self.in_title = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title_text.append(data)


class BanaOfficeWebsiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SITE.read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.source)
        cls.parser.close()

    def test_site_exists_and_has_title(self):
        self.assertTrue(SITE.is_file())
        self.assertIn("BanaOffice", "".join(self.parser.title_text))

    def test_all_three_product_sections_are_present(self):
        page_text = " ".join(self.parser.text)
        for app in ("BanaWriter", "BanaSheets", "BanaSlides"):
            with self.subTest(app=app):
                self.assertIn(app, page_text)

    def test_navigation_anchors_resolve(self):
        for href in self.parser.links:
            if href.startswith("#") and href != "#":
                with self.subTest(anchor=href):
                    self.assertIn(href[1:], self.parser.ids)

    def test_repository_and_status_links_exist(self):
        self.assertIn(
            "https://github.com/bruce-Bana/BanaOffice",
            self.parser.links,
        )
        self.assertIn(
            "https://github.com/bruce-Bana/BanaOffice/blob/trunk/docs/BANAOFFICE_STATUS.md",
            self.parser.links,
        )

    def test_mobile_and_accessibility_basics(self):
        self.assertIn('name="viewport"', self.source)
        self.assertIn("prefers-reduced-motion", self.source)
        self.assertIn('aria-label="Main navigation"', self.source)

    def test_no_external_runtime_dependencies(self):
        self.assertNotIn("<script src=", self.source)
        self.assertNotIn("<link rel=\"stylesheet\" href=", self.source)


if __name__ == "__main__":
    unittest.main()
