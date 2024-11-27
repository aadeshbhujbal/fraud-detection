#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 [-p|--python] [-n|--node] [-w|--watch] [-f|--file <test_file>]"
    echo "Options:"
    echo "  -p, --python    Run Python tests"
    echo "  -n, --node      Run Node.js tests"
    echo "  -w, --watch     Run tests in watch mode"
    echo "  -f, --file      Run specific test file"
    exit 1
}

# Parse command line arguments
PYTHON=false
NODE=false
WATCH=false
FILE=""

while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -p|--python)
        PYTHON=true
        shift
        ;;
        -n|--node)
        NODE=true
        shift
        ;;
        -w|--watch)
        WATCH=true
        shift
        ;;
        -f|--file)
        FILE="$2"
        shift
        shift
        ;;
        *)
        usage
        ;;
    esac
done

# Run tests based on arguments
if [ "$PYTHON" = true ]; then
    if [ "$WATCH" = true ]; then
        if [ -n "$FILE" ]; then
            docker-compose run test-python ptw "$FILE"
        else
            docker-compose run test-python ptw
        fi
    else
        if [ -n "$FILE" ]; then
            docker-compose run test-python pytest "$FILE"
        else
            docker-compose run test-python
        fi
    fi
fi

if [ "$NODE" = true ]; then
    if [ "$WATCH" = true ]; then
        if [ -n "$FILE" ]; then
            docker-compose run test-node npm test -- --watch "$FILE"
        else
            docker-compose run test-node npm test -- --watch
        fi
    else
        if [ -n "$FILE" ]; then
            docker-compose run test-node npm test -- "$FILE"
        else
            docker-compose run test-node
        fi
    fi
fi 