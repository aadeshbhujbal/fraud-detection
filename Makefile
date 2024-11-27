.PHONY: test test-unit test-integration test-e2e

test: test-unit test-integration test-e2e

test-unit:
	docker-compose run test-python pytest tests/unit

test-integration:
	docker-compose run test-python pytest tests/integration

test-e2e:
	docker-compose run test-python pytest tests/e2e

test-watch:
	docker-compose run test-python ptw

setup-test-env:
	docker-compose up -d kafka elasticsearch prometheus grafana
	sleep 10  # Wait for services to be ready

clean:
	docker-compose down -v
	docker-compose rm -f 