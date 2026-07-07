# Official image ships the browsers + system deps pre-installed,
# which keeps versions (and so visual tests) consistent everywhere.
FROM mcr.microsoft.com/playwright/python:v1.56.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the suite headless by default.
CMD ["pytest"]
