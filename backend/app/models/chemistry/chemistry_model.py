class ChemistryModel:
    """
    Estimates how suitable the universe is for complex chemistry.
    """

    @staticmethod
    def evaluate(alpha: float, electron_mass: float) -> float:
        """
        Returns a continuous chemistry score.
        """

        # óptimo alrededor de alpha ≈ 1
        alpha_term = max(0.0, 1.0 - abs(alpha - 1.0))

        # penalización por masa del electrón
        mass_term = max(0.0, 1.0 - abs(electron_mass - 1.0))

        return alpha_term * mass_term * 2.0  # escalar a ~0–2