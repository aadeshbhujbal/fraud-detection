import pytest
import requests
from prometheus_client import CollectorRegistry, Counter, push_to_gateway

def test_prometheus_metrics(test_config):
    registry = CollectorRegistry()
    counter = Counter('transaction_count', 'Number of transactions processed',
                     registry=registry)
    counter.inc()
    
    # Test pushing metrics to Prometheus
    push_to_gateway('localhost:9091', job='fraud_detection_test', registry=registry)
    
    # Verify metrics in Prometheus
    response = requests.get('http://localhost:9090/api/v1/query',
                          params={'query': 'transaction_count'})
    assert response.status_code == 200
    assert float(response.json()['data']['result'][0]['value'][1]) == 1.0

def test_grafana_dashboard(test_config):
    # Test Grafana API health
    response = requests.get('http://localhost:3000/api/health')
    assert response.status_code == 200
    assert response.json()['database'] == 'ok' 