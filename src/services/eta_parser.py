def normalize_eta(eta: int) -> str:
    """
    Convert a raw ETA value (in minutes) into a standardized delivery window.
    """

    if eta <= 0:
        return "Unavailable"

    if eta <= 15:
        return "20-30 mins"
    elif eta <= 20:
        return "20-30 mins"
    elif eta <= 30:
        return "25-35 mins"
    elif eta <= 45:
        return "30-45 mins"
    elif eta <= 60:
        return "45-60 mins"
    elif eta <= 90:
        return "60-90 mins"
    else:
        return "90-120 mins"
