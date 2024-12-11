from fastapi import APIRouter

router = APIRouter()

@router.get("/readiness")
def readiness_check():
    return {"status": "ready"}
