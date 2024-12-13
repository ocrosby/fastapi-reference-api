from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}
