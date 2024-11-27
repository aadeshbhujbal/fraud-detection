import pytest
import yaml
from pyspark.sql import SparkSession
from kafka import KafkaProducer, KafkaConsumer
from elasticsearch import Elasticsearch
import os
import json

@pytest.fixture(scope="session")
def test_config():
    with open("tests/config/test-config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def spark(test_config):
    """Spark session with Delta Lake support"""
    spark = (SparkSession.builder
            .master(test_config["spark"]["master"])
            .appName(test_config["spark"]["app_name"])
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate())
    yield spark
    spark.stop()

@pytest.fixture(scope="function")
def kafka_producer(test_config):
    producer = KafkaProducer(
        bootstrap_servers=test_config["kafka"]["bootstrap_servers"],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    yield producer
    producer.close()

@pytest.fixture(scope="function")
def es_client(test_config):
    client = Elasticsearch(
        f"http://{test_config['elasticsearch']['host']}:{test_config['elasticsearch']['port']}"
    )
    yield client
    client.close()

@pytest.fixture(scope="session")
def test_data():
    """Provide test transaction data."""
    return [
        {
            "transaction_id": 1234567,
            "user_id": 1,
            "amount": 100.00,
            "merchant": "Amazon",
            "category": "Electronics"
        },
        {
            "transaction_id": 1234568,
            "user_id": 2,
            "amount": 500.00,
            "merchant": "Walmart",
            "category": "Groceries"
        }
    ] 