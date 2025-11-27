import unittest
from services.eta_parser import normalize_eta


class TestEtaParser(unittest.TestCase):

    def test_unavailable(self):
        self.assertEqual(normalize_eta(0), "Unavailable")
        self.assertEqual(normalize_eta(-5), "Unavailable")

    def test_eta_15_or_less(self):
        self.assertEqual(normalize_eta(10), "20-30 mins")
        self.assertEqual(normalize_eta(15), "20-30 mins")

    def test_eta_up_to_20(self):
        self.assertEqual(normalize_eta(20), "20-30 mins")

    def test_eta_up_to_30(self):
        self.assertEqual(normalize_eta(25), "25-35 mins")
        self.assertEqual(normalize_eta(30), "25-35 mins")

    def test_eta_up_to_45(self):
        self.assertEqual(normalize_eta(35), "30-45 mins")
        self.assertEqual(normalize_eta(45), "30-45 mins")

    def test_eta_up_to_60(self):
        self.assertEqual(normalize_eta(50), "45-60 mins")
        self.assertEqual(normalize_eta(60), "45-60 mins")

    def test_eta_up_to_90(self):
        self.assertEqual(normalize_eta(75), "60-90 mins")
        self.assertEqual(normalize_eta(90), "60-90 mins")

    def test_eta_above_90(self):
        self.assertEqual(normalize_eta(95), "90-120 mins")
        self.assertEqual(normalize_eta(150), "90-120 mins")


if __name__ == "__main__":
    unittest.main()
