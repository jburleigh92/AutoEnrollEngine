from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .driver import get_driver


def extract_eta_from_tracking_page(url: str) -> int:
    """
    Load the provided tracking URL, extract the ETA value in minutes,
    and return it as an integer.
    """

    driver = get_driver()

    try:
        driver.get(url)

        # Wait for ETA element to load on the page
        wait = WebDriverWait(driver, 20)
        eta_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='eta-value']")
            )
        )

        # Extract numeric ETA from text such as "25 min" or "30 mins"
        text = eta_element.text.strip().lower()
        eta = _parse_eta_text(text)

        return eta

    finally:
        driver.quit()


def _parse_eta_text(text: str) -> int:
    """
    Extract the numeric ETA value from the ETA text.
    """

    for token in text.split():
        if token.isdigit():
            return int(token)

    # Fallback when no number could be parsed
    return 0
