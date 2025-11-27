# AutoEnrollEngine

AutoEnrollEngine is a webhook-driven automation service that extracts real-time delivery ETAs from tracking pages using Selenium and headless Chrome. Incoming webhook requests contain a tracking URL, and the service returns both the raw ETA value and a normalized delivery window.

The system is built with Flask for routing, Selenium for scraping, and a modular architecture designed for clarity, reliability, and future extension.

---

## Features

- Webhook endpoint for real-time processing  
- Automated tracking-page scraping using Selenium  
- Headless Chrome execution for server environments  
- ETA extraction from dynamic UI elements  
- Normalized delivery windows (e.g., *“25–35 mins”*)  
- Clean, testable, fully modular Python architecture  
- Docker support for deterministic deployments  
- Extensible notification layer

---

## Architecture Overview

```
AutoEnrollEngine/
│
├── src/
│   ├── app.py                      # Flask application and routing
│   ├── main.py                     # Application entrypoint
│   ├── webhook_handler.py          # Request validation and processing
│   ├── scraper/
│   │   ├── driver.py               # Selenium WebDriver configuration
│   │   ├── tracker_scraper.py      # ETA scraping logic
│   │   └── __init__.py
│   ├── services/
│   │   ├── eta_parser.py           # ETA normalization rules
│   │   ├── notifier.py             # Optional notifications
│   │   └── __init__.py
│   ├── utils/
│   │   ├── logging_utils.py        # Basic logging utilities
│   │   ├── request_validator.py    # Webhook payload validation
│   │   └── __init__.py
│   └── __init__.py
│
├── tests/                          # Unit tests for all components
│   ├── test_webhook_handler.py
│   ├── test_eta_parser.py
│   ├── test_request_validator.py
│   ├── test_tracker_scraper.py
│   └── __init__.py
│
├── docker/
│   ├── Dockerfile                   # Chrome + Python environment
│   └── start.sh                     # Container startup script
│
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
└── LICENSE                          # MIT License
```

---

## Webhook Workflow

1. A POST request is sent to `/webhook` with JSON containing a `tracking_url`.
2. The payload is validated.
3. Selenium loads the tracking page in headless Chrome.
4. The ETA element is located and parsed.
5. The ETA (in minutes) is normalized into a delivery window.
6. The API returns structured JSON:

```json
{
  "tracking_url": "https://example.com/track/123",
  "eta_minutes": 32,
  "eta_window": "25-35 mins"
}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/AutoEnrollEngine.git
cd AutoEnrollEngine
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

To start the service locally:

```bash
python src/main.py
```

The webhook endpoint will be available at:

```
POST http://localhost:5002/webhook
```

---

## Docker Deployment

Build the Docker image:

```bash
docker build -t auto-enroll-engine ./docker
```

Run the service:

```bash
docker run -p 5002:5002 auto-enroll-engine
```

---

## Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Then update values such as:

- `FLASK_PORT`  
- `SELENIUM_HEADLESS`  
- `NOTIFIER_ENABLED`  

---

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

---

## License

AutoEnrollEngine is released under the MIT License.
