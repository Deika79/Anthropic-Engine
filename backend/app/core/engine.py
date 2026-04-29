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

        # 🌟 estrellas
        stars_exist = StellarModel.evaluate(
            params.alpha,
            params.strong_force
        )

        # ⚛️ elementos pesados
        heavy_elements = NucleosynthesisModel.evaluate(
            params.strong_force
        )

        # 🧪 química
        chemistry_score = ChemistryModel.evaluate(
            params.alpha,
            params.electron_mass
        )

        # 🌍 habitabilidad
        habitability_score = HabitabilityModel.evaluate(
            stars_exist,
            heavy_elements,
            chemistry_score
        )

        explanation = ExplanationService.generate(
            stars_exist,
            heavy_elements,
            chemistry_score,
            habitability_score
        )

        return SimulationResult(
            star_stability=stars_exist,
            heavy_elements=heavy_elements,
            chemistry_score=chemistry_score,
            habitability_score=habitability_score,
            explanation=explanation
        )