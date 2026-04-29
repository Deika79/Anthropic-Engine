from fastapi import APIRouter
from app.models.universe import UniverseParameters
from app.models.result import SimulationResult
from app.core.engine import SimulationEngine

router = APIRouter()


@router.post("/simulate", response_model=SimulationResult)
def simulate_universe(params: UniverseParameters) -> SimulationResult:
    result = SimulationEngine.run(params)
    return result