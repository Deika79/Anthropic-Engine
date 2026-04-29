from pydantic import BaseModel, Field


class BatchSimulationRequest(BaseModel):
    """
    Request for generating multiple universes.
    """

    num_samples: int = Field(
        default=100,
        gt=0,
        le=5000,
        description="Number of universes to simulate"
    )

    alpha_range: tuple[float, float] = (0.5, 1.5)
    strong_force_range: tuple[float, float] = (0.5, 1.5)
    electron_mass_range: tuple[float, float] = (0.5, 1.5)