from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.simulate import router as simulate_router
from app.api.routes.batch import router as batch_router
from app.api.routes.grid import router as grid_router

app = FastAPI(
    title="Anthropic Engine API",
    description="Simulation engine for exploring anthropic universes",
    version="0.1.0"
)

# ✅ CORS CONFIG (clave)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego lo restringimos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulate_router)
app.include_router(batch_router)
app.include_router(grid_router)


@app.get("/")
def root():
    return {
        "message": "Anthropic Engine API is running"
    }