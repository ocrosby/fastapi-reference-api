from fastapi import FastAPI
from app.handlers import root_handler, health_handler, readiness_handler

app = FastAPI()

app.include_router(root_handler.router)
app.include_router(health_handler.router)
app.include_router(readiness_handler.router)