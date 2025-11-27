FROM python:3.10-slim

# Install system dependencies required for Chrome and Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy application code
COPY ../src ./src
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5002

# Run Flask application
CMD ["python", "src/main.py"]
