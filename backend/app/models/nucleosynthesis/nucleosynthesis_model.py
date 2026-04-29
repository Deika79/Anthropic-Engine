from app.models.universe import UniverseParameters


class NucleosynthesisModel:
    """
    Simplified model for heavy element formation.

    Focuses on carbon and oxygen production viability.
    """

    @staticmethod
    def evaluate(params: UniverseParameters, stars_exist: bool) -> bool:
        if not stars_exist:
            return False

        strong = params.strong_force

        # Narrow window for carbon formation (triple-alpha sensitivity)
        if 0.8 <= strong <= 1.2:
            return True

        return False