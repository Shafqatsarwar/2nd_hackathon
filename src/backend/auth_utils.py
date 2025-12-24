import os
import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# Shared secret between Frontend and Backend
BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET", "default_secret_change_me")

security = HTTPBearer()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Verifies the JWT token from Better Auth.
    Expects 'Authorization: Bearer <token>'
    Allows 'guest_token' for public demo access.
    """
    token = credentials.credentials
    
    # Guest & Admin Access Bypass for Hackathon Demo
    if token == "guest_token":
        return "guest_user"
    if token == "admin_token":
        return "admin"

    try:
        # Better Auth usually issues RS256 or HS256. 
        # For simplicity in this Hackathon project, we assume the shared secret HS256 flow.
        payload = jwt.decode(
            token, 
            BETTER_AUTH_SECRET, 
            algorithms=["HS256"],
            # Better Auth tokens might have specific audience settings, 
            # we keep it flexible for now or skip if verification is purely signature based.
            options={"verify_aud": False}
        )
        user_id = payload.get("sub") # 'sub' is standard for user ID in JWTs
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing user ID ('sub')",
            )
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
