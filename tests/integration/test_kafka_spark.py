import pytest
from kafka import KafkaProducer, KafkaConsumer
import json
from src.data_generator.generator import generate_transaction

@pytest.fixture
def kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    yield producer
    producer.close()

@pytest.fixture
def kafka_consumer():
    consumer = KafkaConsumer(
        'transactions',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='test-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    yield consumer
    consumer.close()

def test_kafka_producer_consumer(kafka_producer, kafka_consumer):
    # Generate and send test transaction
    test_transaction = generate_transaction()
    kafka_producer.send('transactions', test_transaction)
    kafka_producer.flush()
    
    # Read message from consumer
    message = next(kafka_consumer)
    received_transaction = message.value
    
    # Verify message contents
    assert received_transaction["transaction_id"] == test_transaction["transaction_id"]
    assert received_transaction["amount"] == test_transaction["amount"] 