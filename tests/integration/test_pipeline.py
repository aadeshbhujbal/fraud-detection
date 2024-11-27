import pytest
from datetime import datetime
from src.spark.processor import process_transaction_stream
from src.models.fraud_detector import FraudDetector
from delta.tables import DeltaTable

def test_end_to_end_pipeline(spark, kafka_producer, test_config, es_client):
    # 1. Generate and send test transaction
    test_transaction = {
        "transaction_id": "test-123",
        "amount": 1000.0,
        "timestamp": datetime.now().isoformat(),
        "user_id": "user-123",
        "merchant": "Test Merchant"
    }
    
    kafka_producer.send(test_config["kafka"]["test_topic"], test_transaction)
    kafka_producer.flush()
    
    # 2. Process with Spark
    df = process_transaction_stream(spark, test_config["kafka"]["test_topic"])
    
    # 3. Write to Delta Lake
    delta_path = test_config["delta"]["test_table_path"]
    df.write.format("delta").mode("overwrite").save(delta_path)
    
    # 4. Verify Delta Lake write
    delta_table = DeltaTable.forPath(spark, delta_path)
    result = delta_table.toDF().collect()
    assert len(result) > 0
    
    # 5. Check Elasticsearch logging
    es_result = es_client.search(
        index="fraud-detection-logs",
        body={"query": {"match": {"transaction_id": "test-123"}}}
    )
    assert es_result["hits"]["total"]["value"] > 0 