"""
Docstring for services.security
"""

import os
from dotenv import load_dotenv # pip install python-dotenv

from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

load_dotenv()

API_KEY_NAME = "X-API-Key"
# X_API_KEY = os.getenv("X_API_KEY", "default-secret-key")
X_API_KEY = os.getenv("X_API_KEY")

api_key_header = APIKeyHeader(
    name=API_KEY_NAME,
    auto_error=False
)


def validate_api_key(api_key: str = Security(api_key_header)):
    """
    Docstring for validate_api_key

    :param api_key: Description
    :type api_key: str
    """
    if api_key != X_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return api_key
