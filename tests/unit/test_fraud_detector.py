import pytest
from src.models.fraud_detector import FraudDetector

def test_fraud_detection_rules():
    detector = FraudDetector()
    
    # Test high amount transaction
    high_amount_transaction = {
        "amount": 10000.0,
        "user_id": "user-123"
    }
    assert detector.is_suspicious(high_amount_transaction)
    
    # Test normal transaction
    normal_transaction = {
        "amount": 100.0,
        "user_id": "user-123"
    }
    assert not detector.is_suspicious(normal_transaction) 