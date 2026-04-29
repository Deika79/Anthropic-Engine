from app.models.universe import UniverseParameters


class ChemistryModel:
    """
    Estimates chemical complexity potential.
    """

    @staticmethod
    def evaluate(params: UniverseParameters) -> float:
        alpha = params.alpha
        electron_mass = params.electron_mass

        # Ideal region around our universe
        alpha_factor = max(0.0, 1.5 - abs(alpha - 1.0))

        # Electron mass affects orbital structure
        mass_factor = max(0.0, 1.5 - abs(electron_mass - 1.0))

        chemistry_score = (alpha_factor + mass_factor) / 2.0

        return chemistry_score