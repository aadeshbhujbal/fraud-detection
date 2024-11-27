import pytest
from pyspark.sql import SparkSession
from src.spark_processor import create_spark_session

def test_spark_session_creation():
    spark = create_spark_session()
    assert isinstance(spark, SparkSession)
    assert spark.version is not None
    spark.stop()

def test_kafka_connection():
    # This is a basic test to ensure Kafka connection works
    from kafka import KafkaProducer
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        assert producer is not None
        producer.close()
    except Exception as e:
        pytest.fail(f"Failed to connect to Kafka: {str(e)}")
