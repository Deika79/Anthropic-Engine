import numpy as np

from app.models.universe import UniverseParameters
from app.models.result import SimulationResult
from app.core.engine import SimulationEngine


class BatchSimulationService:
    """
    Generates a structured grid of universes for parameter space exploration.
    """

    @staticmethod
    def run_grid(
        alpha_min=0.5,
        alpha_max=1.5,
        strong_min=0.5,
        strong_max=1.5,
        resolution=25
    ) -> list[dict]:

        results = []

        alpha_values = np.linspace(alpha_min, alpha_max, resolution)
        strong_values = np.linspace(strong_min, strong_max, resolution)

        for alpha in alpha_values:
            for strong in strong_values:

                params = UniverseParameters(
                    alpha=float(alpha),
                    strong_force=float(strong),
                    electron_mass=1.0,
                    cosmological_constant=1.0
                )

                sim = SimulationEngine.run(params)

                results.append({
                    "alpha": alpha,
                    "strong_force": strong,
                    "habitability": sim.habitability_score
                })

        return results