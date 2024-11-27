import pytest
from src.data_generator.generator import generate_transaction

def test_generate_transaction_structure():
    transaction = generate_transaction()
    
    # Check required fields
    assert "transaction_id" in transaction
    assert "user_id" in transaction
    assert "amount" in transaction
    assert "timestamp" in transaction
    assert "merchant" in transaction
    assert "category" in transaction

def test_generate_transaction_values():
    transaction = generate_transaction()
    
    # Validate value ranges and types
    assert isinstance(transaction["transaction_id"], int)
    assert 1000000 <= transaction["transaction_id"] <= 9999999
    
    assert isinstance(transaction["amount"], float)
    assert 10 <= transaction["amount"] <= 1000
    
    assert transaction["merchant"] in ["Amazon", "Walmart", "Target", "Best Buy"]
    assert transaction["category"] in ["Electronics", "Groceries", "Clothing", "Other"] 