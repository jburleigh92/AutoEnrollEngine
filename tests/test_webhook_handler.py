import unittest
from unittest.mock import patch

from app import app


class TestWebhookHandler(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch("webhook_handler.extract_eta_from_tracking_page")
    @patch("webhook_handler.normalize_eta")
    def test_webhook_success(
        self, mock_normalize_eta, mock_extract_eta
    ):
        mock_extract_eta.return_value = 32
        mock_normalize_eta.return_value = "25-35 mins"

        payload = {"tracking_url": "https://example.com/track/123"}

        response = self.client.post("/webhook", json=payload)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["tracking_url"], payload["tracking_url"])
        self.assertEqual(data["eta_minutes"], 32)
        self.assertEqual(data["eta_window"], "25-35 mins")

    def test_missing_tracking_url(self):
        payload = {}

        response = self.client.post("/webhook", json=payload)

        # Flask abort generates HTML response; only check status code
        self.assertEqual(response.status_code, 400)

    def test_invalid_payload_type(self):
        response = self.client.post("/webhook", data="not-json")
        self.assertTrue(response.status_code in [400, 415])


if __name__ == "__main__":
    unittest.main()
