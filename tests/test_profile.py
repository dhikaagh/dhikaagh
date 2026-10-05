"""Public-profile checks. Run: python3 -B -m unittest discover -s tests -v."""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, urlparse
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class ProfileMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.sources = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))
        elif tag == "source":
            self.sources.append(dict(attrs))

    def handle_data(self, data):
        self.text.append(data)


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
        self.assertRegex(readme, r'src="img/profile-banner\.svg(?:\?[^\"]*)?"')
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

    def test_looping_banner_can_be_hidden_without_hiding_identity(self):
        banner = ET.parse(ROOT / "img/profile-banner.svg").getroot()
        styles = " ".join(element.text or "" for element in banner.iter()
                          if element.tag.endswith("style"))
        self.assertRegex(styles, r"animation:\s*[^;{}]*\binfinite\b")
        for element in banner.iter():
            if element.text in ("DHIKA", "Full-Stack Software Engineer"):
                self.assertNotIn("flow-marker", element.get("class", "").split())
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("<details open>", readme)
        self.assertIn("<summary>Banner animation", readme)
        self.assertIn("Full-Stack Software Engineer", readme.split("</details>", 1)[1])

    def test_tech_stack_has_icons_and_visible_names(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Tech stack", readme)
        stack = readme.split("## Tech stack", 1)[1].split("\n## ", 1)[0]
        markup = ProfileMarkup()
        markup.feed(stack)
        names = (
            "React", "Next.js", "Tailwind CSS", "Node.js", "Hono", "Laravel",
            "JavaScript", "TypeScript", "PHP", "MySQL", "PostgreSQL", "RabbitMQ",
            "GitHub Actions", "GitLab CI/CD", "Docker (basics)", "Linux", "Git",
        )
        self.assertEqual(len(markup.images), len(names))
        visible = " ".join(markup.text)
        for name in names:
            self.assertIn(name, visible, "Technology names must not be only image alt text")

    def test_four_stats_cards_use_own_account_and_theme_variants(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## 📊 GitHub Stats", readme)
        stats = readme.split("## 📊 GitHub Stats", 1)[1].split("\n## ", 1)[0]
        markup = ProfileMarkup()
        markup.feed(stats)
        self.assertEqual(len(markup.images), 4)
        self.assertEqual(len(markup.sources), 4)
        self.assertIn("Languages by repository count", " ".join(markup.text))
        kinds = set()
        for image in markup.images:
            self.assertTrue(image.get("alt"))
        for source in markup.sources:
            self.assertEqual(source.get("media"), "(prefers-color-scheme: dark)")
        for asset in markup.images + markup.sources:
            url = urlparse(asset.get("src") or asset["srcset"])
            self.assertEqual(url.scheme, "https")
            self.assertIn(url.netloc, {
                "github-profile-summary-cards.vercel.app", "streak-stats.demolab.com",
            })
            params = parse_qs(url.query)
            self.assertEqual(params.get("username") or params.get("user"), ["dhikaagh"])
            kinds.add("streak" if "demolab" in url.netloc else url.path.rsplit("/", 1)[1])
        self.assertEqual(kinds, {"profile-details", "stats", "repos-per-language", "streak"})

    def test_profile_has_no_retired_decoration_or_generator(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for retired in (
            "readme-typing-svg", "github-contribution-grid-snake",
            "giphy.com", "komarev.com", "Coming_Soon",
        ):
            self.assertNotIn(retired, readme)
        self.assertFalse((ROOT / ".github/workflows/snake.yml").exists())


if __name__ == "__main__":
    unittest.main()
