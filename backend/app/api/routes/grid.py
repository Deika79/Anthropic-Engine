from fastapi import APIRouter
from app.services.batch_service import BatchSimulationService

router = APIRouter()


@router.get("/grid")
def get_universe_grid():
    return BatchSimulationService.run_grid()