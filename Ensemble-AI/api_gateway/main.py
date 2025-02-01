# File Path: /api_gateway/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from routes import codegen, auth, health
from typing import Annotated
import redis
import os
from prometheus_client import start_http_server, Summary

app = FastAPI(
    title="AI Code Assistant API Gateway",
    description="API Gateway for AI Code Assistant services",
    version="1.0.0",
    openapi_tags=[
        {"name": "Health", "description": "Health check endpoints"},
        {"name": "Authentication", "description": "User authentication endpoints"},
        {"name": "Code Generation", "description": "Code generation endpoints"},
    ]
)

# Redis client setup
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

# Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Authentication Middleware
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    if not token.startswith("ens-"):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

# Include Routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(codegen.router, prefix="/code", tags=["Code Generation"])

# Root Endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the AI Code Assistant API Gateway"}

# Example of caching an endpoint
@app.get("/cached-endpoint")
@REQUEST_TIME.time()
async def cached_endpoint():
    cache_key = "cached_endpoint"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return {"data": cached_data.decode("utf-8")}
    
    # Simulate data fetching
    data = "This is some data that will be cached."
    redis_client.setex(cache_key, 3600, data)  # Cache for 1 hour
    return {"data": data}

# Start Prometheus metrics server
start_http_server(8001)
