#!/bin/bash

# Start test environment
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to start..."
sleep 30

# Run tests
if [ "$1" = "--unit" ]; then
    make test-unit
elif [ "$1" = "--integration" ]; then
    make test-integration
elif [ "$1" = "--e2e" ]; then
    make test-e2e
else
    make test
fi

# Cleanup
docker-compose down 