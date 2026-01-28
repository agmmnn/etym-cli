import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import os
from etym_cli.cli import req

class TestEtymCli(unittest.TestCase):
    def setUp(self):
        # Determine path to fixture
        base_path = os.path.dirname(os.path.abspath(__file__))
        fixture_path = os.path.join(base_path, "fixtures", "flow.html")
        with open(fixture_path, "r", encoding="utf-8") as f:
            self.html_content = f.read()

    @patch("etym_cli.cli.requests.get")
    def test_scraping_selectors(self, mock_get):
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = self.html_content.encode("utf-8")
        mock_get.return_value = mock_response

        # Call req (which uses requests.get)
        soup = req("word/", "flow")

        # Test selectors used in main
        secs = soup.find_all("section", class_="prose-lg")
        related = soup.select_one("ul.list-none.flex.gap-2.flex-wrap")

        # Assertions
        self.assertEqual(len(secs), 2, "Should find 2 definition sections for 'flow'")

        # Verify content of sections
        # Section 1: flow(v.)
        title1 = secs[0].find(["h1", "h2", "h3"])
        self.assertIn("flow", title1.text)
        self.assertIn("(v.)", title1.text)

        # Section 2: flow(n.)
        title2 = secs[1].find(["h1", "h2", "h3"])
        self.assertIn("flow", title2.text)
        self.assertIn("(n.)", title2.text)

        # Verify related words
        self.assertIsNotNone(related, "Should find related words list")
        related_items = [li.text.strip() for li in related.find_all("li")]
        # From manual inspection of flow page/debug_html: flue, inflow, interflow, outflow, overflow, workflow, *pleu-
        expected_related = ["flue", "inflow", "interflow", "outflow", "overflow", "workflow", "*pleu-"]

        # We can check if expected words are in the found items
        # Note: items might contain extra whitespace or other text, checking containment
        for word in expected_related:
            self.assertTrue(any(word in item for item in related_items), f"Related word {word} not found in {related_items}")

if __name__ == "__main__":
    unittest.main()
