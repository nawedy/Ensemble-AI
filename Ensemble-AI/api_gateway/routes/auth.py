from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Annotated

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordBearer, Depends()]):
    # Implement your authentication logic here
    if form_data.username == "test" and form_data.password == "test":
        return {"access_token": "ens-test-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    if not token.startswith("ens-"):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token
