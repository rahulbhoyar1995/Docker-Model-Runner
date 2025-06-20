#!/bin/bash

# Get the LLM_MODEL_NAME from .env file
LLM_MODEL_NAME="ai/llama3.2:1B-Q8_0"

# Check if LLM_MODEL_NAME was found
if [ -z "$LLM_MODEL_NAME" ]; then
    echo "Error: LLM_MODEL_NAME not found in .env file or it's commented out."
    exit 1
fi

echo "Using LLM model: $LLM_MODEL_NAME"

# Pull the Docker model
echo "Pulling Docker model..."
docker model pull $LLM_MODEL_NAME

# Build and run Docker container
echo "Running Docker Compose..."
docker compose up --build