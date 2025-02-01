# File Path: /api_gateway/routes/health.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "API Gateway is running"}
