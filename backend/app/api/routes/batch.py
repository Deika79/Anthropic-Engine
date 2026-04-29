from fastapi import APIRouter
from app.models.batch import BatchSimulationRequest
from app.models.result import SimulationResult
from app.services.batch_service import BatchSimulationService

router = APIRouter()


@router.post("/batch", response_model=list[SimulationResult])
def run_batch_simulation(request: BatchSimulationRequest):
    return BatchSimulationService.run_batch(request)