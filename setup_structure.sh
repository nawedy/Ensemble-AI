#!/bin/bash

# Create directories
mkdir -p Ensemble-AI/docker
mkdir -p Ensemble-AI/api_gateway/routes
mkdir -p Ensemble-AI/api_gateway/services
mkdir -p Ensemble-AI/workspace/sample_project

# Create files in docker directory
touch Ensemble-AI/docker/Dockerfile.vscode
touch Ensemble-AI/docker/Dockerfile.gateway
touch Ensemble-AI/docker/docker-compose.yml

# Create files in api_gateway directory
touch Ensemble-AI/api_gateway/main.py
touch Ensemble-AI/api_gateway/requirements.txt
touch Ensemble-AI/api_gateway/config.py

# Create files in api_gateway/routes directory
touch Ensemble-AI/api_gateway/routes/__init__.py
touch Ensemble-AI/api_gateway/routes/codegen.py
touch Ensemble-AI/api_gateway/routes/auth.py
touch Ensemble-AI/api_gateway/routes/health.py
touch Ensemble-AI/api_gateway/routes/utils.py

# Create files in api_gateway/services directory
touch Ensemble-AI/api_gateway/services/__init__.py
touch Ensemble-AI/api_gateway/services/llm_handler.py
touch Ensemble-AI/api_gateway/services/context_manager.py
touch Ensemble-AI/api_gateway/services/document_processor.py
touch Ensemble-AI/api_gateway/services/code_executor.py

# Create files in workspace directory
touch Ensemble-AI/workspace/README.md

# Create files in the root directory
touch Ensemble-AI/.env
touch Ensemble-AI/.gitignore
touch Ensemble-AI/README.md

echo "Directory structure created successfully."