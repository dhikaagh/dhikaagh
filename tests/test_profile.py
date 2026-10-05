"""Public-profile checks. Run: python3 -B -m unittest discover -s tests -v."""

from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class ProfileTests(unittest.TestCase):
    def test_profile_presents_approved_role_and_public_projects(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Full-Stack Software Engineer", readme)
        projects = set(re.findall(r"https://github\.com/dhikaagh/([\w.-]+)", readme))
        self.assertEqual(projects, {"paymentkit", "Messaging-Bridge-"})

    def test_selected_work_includes_personal_contributions(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(readme.count("**My contribution:**"), 2)

    def test_banner_is_accessible_and_self_contained(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('src="img/profile-banner.svg"', readme)
        banner = ET.parse(ROOT / "img/profile-banner.svg").getroot()
        self.assertEqual(banner.get("role"), "img")
        self.assertIn("viewBox", banner.attrib)
        ids = {element.get("id") for element in banner.iter()}
        self.assertTrue(set(banner.attrib["aria-labelledby"].split()) <= ids)
        text = " ".join(banner.itertext())
        self.assertIn("Full-Stack Software Engineer", text)
        self.assertIn("prefers-reduced-motion: reduce", text)
        for element in banner.iter():
            self.assertNotEqual(element.tag.split("}")[-1], "script")
            for key, value in element.attrib.items():
                if key.endswith("href"):
                    self.assertTrue(value.startswith("#"), "External SVG dependency")

    def test_profile_has_no_retired_decoration_or_generator(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for retired in (
            "readme-typing-svg", "streak-stats", "github-contribution-grid-snake",
            "giphy.com", "komarev.com", "Coming_Soon",
        ):
            self.assertNotIn(retired, readme)
        self.assertFalse((ROOT / ".github/workflows/snake.yml").exists())


if __name__ == "__main__":
    unittest.main()
