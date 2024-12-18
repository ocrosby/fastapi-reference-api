from fastapi import FastAPI

from app.handlers.v1 import health_handler as v1_health
from app.handlers.v1 import readiness_handler as v1_readiness
from app.handlers.v1 import root_handler as v1_root

from app.handlers.v2 import health_handler as v2_health
from app.handlers.v2 import readiness_handler as v2_readiness
from app.handlers.v2 import root_handler as v2_root

app = FastAPI()

# Include routers for version 1
app.include_router(v1_health.router, prefix="/v1")
app.include_router(v1_readiness.router, prefix="/v1")
app.include_router(v1_root.router, prefix="/v1")

# Include routers for version 2
app.include_router(v2_health.router, prefix="/v2")
app.include_router(v2_readiness.router, prefix="/v2")
app.include_router(v2_root.router, prefix="/v2")
