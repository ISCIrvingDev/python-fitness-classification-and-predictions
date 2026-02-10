"""
Docstring for services.rate_limit
"""

from slowapi import Limiter
# from slowapi.util import get_remote_address
from fastapi import Request

def api_key_rate_limit(request: Request):
    """
    Docstring for api_key_rate_limit

    :param request: Description
    :type request: Request
    """
    return request.headers.get("X-API-Key", "anonymous")

limiter = Limiter(
    # key_func=get_remote_address,  # IP por defecto
    key_func=api_key_rate_limit,  # IP por defecto
    default_limits=["10/minute"] # Limite general (todos los endpoints)
)
