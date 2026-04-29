from app.models.universe import UniverseParameters
from app.models.result import SimulationResult

from app.models.stellar.stellar_model import StellarModel
from app.models.nucleosynthesis.nucleosynthesis_model import NucleosynthesisModel
from app.models.chemistry.chemistry_model import ChemistryModel
from app.models.habitability.habitability_model import HabitabilityModel

from app.services.explanation_service import ExplanationService


class SimulationEngine:

    @staticmethod
    def run(params: UniverseParameters) -> SimulationResult:

        stars_exist = StellarModel.evaluate(params)

        heavy_elements = NucleosynthesisModel.evaluate(params, stars_exist)

        chemistry_score = ChemistryModel.evaluate(params)

        habitability = HabitabilityModel.evaluate(
            stars_exist,
            heavy_elements,
            chemistry_score
        )

        explanation = ExplanationService.generate(
            params,
            stars_exist,
            heavy_elements,
            chemistry_score,
            habitability
        )

        return SimulationResult(
            star_stability=stars_exist,
            heavy_elements=heavy_elements,
            chemistry_score=chemistry_score,
            habitability_score=habitability,
            explanation=explanation
        )