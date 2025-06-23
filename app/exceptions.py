from fastapi.responses import JSONResponse
from fastapi.requests import Request

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )
