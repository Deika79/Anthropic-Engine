class HabitabilityModel:
    """
    Aggregates different factors into a habitability score.
    """

    @staticmethod
    def evaluate(
        stars_exist: bool,
        heavy_elements: bool,
        chemistry_score: float
    ) -> float:

        if not stars_exist:
            return 0.0

        if not heavy_elements:
            return 0.0

        return chemistry_score