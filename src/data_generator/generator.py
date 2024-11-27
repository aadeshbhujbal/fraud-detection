import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

def generate_transaction():
    """Generate a random transaction."""
    return {
        "transaction_id": random.randint(1000000, 9999999),
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(10, 1000), 2),
        "timestamp": datetime.now().isoformat(),
        "merchant": random.choice(["Amazon", "Walmart", "Target", "Best Buy"]),
        "category": random.choice(["Electronics", "Groceries", "Clothing", "Other"])
    }

def main():
    """Main function to generate and send transactions to Kafka."""
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

    while True:
        transaction = generate_transaction()
        producer.send('transactions', transaction)
        print(f"Generated transaction: {transaction}")
        time.sleep(1)

if __name__ == "__main__":
    # Wait for Kafka to be ready
    time.sleep(10)
    main() 