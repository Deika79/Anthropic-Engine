from pydantic import BaseModel


class SimulationResult(BaseModel):
    """
    Output of the universe simulation.
    """

    star_stability: bool
    heavy_elements: bool
    chemistry_score: float
    habitability_score: float
    explanation: str