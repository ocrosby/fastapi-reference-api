from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    """
    Root endpoint.
    """
    return {"Hello": "World"}
