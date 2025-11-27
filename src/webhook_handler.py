from flask import abort
from scraper.tracker_scraper import extract_eta_from_tracking_page
from services.eta_parser import normalize_eta
from utils.request_validator import validate_webhook_payload


def process_webhook(payload: dict) -> dict:
    """
    Process the webhook request payload and return a structured result.
    """

    # Validate input and extract tracking URL
    tracking_url = validate_webhook_payload(payload)

    # Extract ETA minutes using Selenium scraping
    eta_minutes = extract_eta_from_tracking_page(tracking_url)

    # Convert raw ETA minutes into a delivery window
    eta_window = normalize_eta(eta_minutes)

    return {
        "tracking_url": tracking_url,
        "eta_minutes": eta_minutes,
        "eta_window": eta_window
    }
