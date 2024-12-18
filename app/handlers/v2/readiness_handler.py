from fastapi import APIRouter

router = APIRouter()

@router.get("/readiness")
def readiness_check():
    """
    Readiness check endpoint.
    """
    return {"status": "ready"}
