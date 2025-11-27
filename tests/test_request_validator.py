import unittest
from flask import Flask
from utils.request_validator import validate_webhook_payload


class TestRequestValidator(unittest.TestCase):

    def setUp(self):
        # Flask context is required since the validator may call abort()
        self.app = Flask(__name__)
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_valid_payload(self):
        payload = {"tracking_url": "https://example.com/track/123"}
        result = validate_webhook_payload(payload)
        self.assertEqual(result, payload["tracking_url"])

    def test_missing_tracking_url(self):
        payload = {}
        with self.assertRaises(Exception):
            validate_webhook_payload(payload)

    def test_non_dict_payload(self):
        with self.assertRaises(Exception):
            validate_webhook_payload("invalid")

    def test_empty_string(self):
        payload = {"tracking_url": ""}
        with self.assertRaises(Exception):
            validate_webhook_payload(payload)

    def test_non_http_url(self):
        payload = {"tracking_url": "ftp://example.com"}
        with self.assertRaises(Exception):
            validate_webhook_payload(payload)


if __name__ == "__main__":
    unittest.main()
