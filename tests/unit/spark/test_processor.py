import pytest
from pyspark.sql import SparkSession
from src.spark.processor import create_spark_session, process_kafka_stream

def test_spark_session_creation():
    spark = create_spark_session()
    try:
        assert isinstance(spark, SparkSession)
        assert spark.version is not None
    finally:
        spark.stop()

def test_process_kafka_stream_schema():
    spark = create_spark_session()
    try:
        # Create test data
        test_data = [
            ('{"transaction_id": "123", "amount": 100}',),
            ('{"transaction_id": "124", "amount": 200}',)
        ]
        test_df = spark.createDataFrame(test_data, ["value"])
        
        # Process the test data
        result_df = process_kafka_stream(test_df)
        
        # Verify schema and data
        assert "transaction_id" in result_df.columns
        assert "amount" in result_df.columns
    finally:
        spark.stop() 