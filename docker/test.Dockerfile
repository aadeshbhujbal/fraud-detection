FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install test dependencies
RUN pip install pytest pytest-cov pytest-watch

# Copy application code
COPY . .

# Default command (can be overridden)
CMD ["pytest"] 