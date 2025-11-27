from flask import abort


def validate_webhook_payload(payload: dict) -> str:
    """
    Validate the incoming webhook payload and return the tracking URL.
    """

    if not isinstance(payload, dict):
        abort(400, "Invalid payload format.")

    if "tracking_url" not in payload:
        abort(400, "Missing 'tracking_url' in payload.")

    tracking_url = payload["tracking_url"]

    if not isinstance(tracking_url, str) or not tracking_url.strip():
        abort(400, "Invalid 'tracking_url' value.")

    if not tracking_url.startswith("http"):
        abort(400, "Tracking URL must begin with http or https.")

    return tracking_url.strip()
