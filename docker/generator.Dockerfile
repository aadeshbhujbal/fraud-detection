FROM python:3.9-slim

WORKDIR /app

# Combine copy and install in a single layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/data_generator /app/data_generator

CMD ["python", "-m", "data_generator.generator"] 