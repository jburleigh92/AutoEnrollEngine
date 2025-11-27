import unittest
from unittest.mock import patch, MagicMock

from scraper.tracker_scraper import extract_eta_from_tracking_page, _parse_eta_text


class TestTrackerScraper(unittest.TestCase):

    @patch("scraper.tracker_scraper.get_driver")
    def test_extract_eta_success(self, mock_get_driver):
        # Mock driver and element
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.text = "25 min"

        # WebDriverWait result
        mock_wait = MagicMock()
        mock_wait.until.return_value = mock_element

        # Configure driver mock
        mock_driver.get.return_value = None

        # Mock get_driver to return mock driver
        mock_get_driver.return_value = mock_driver

        # Patch WebDriverWait globally inside tracker_scraper
        with patch("scraper.tracker_scraper.WebDriverWait", return_value=mock_wait):
            eta = extract_eta_from_tracking_page("https://example.com")

        self.assertEqual(eta, 25)
        mock_driver.quit.assert_called_once()

    def test_parse_eta_text(self):
        self.assertEqual(_parse_eta_text("25 min"), 25)
        self.assertEqual(_parse_eta_text("40 mins"), 40)
        self.assertEqual(_parse_eta_text("ETA: 12 minutes"), 12)

    def test_parse_eta_text_no_number(self):
        self.assertEqual(_parse_eta_text("no eta available"), 0)


if __name__ == "__main__":
    unittest.main()
