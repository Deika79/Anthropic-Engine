class ExplanationService:
    """
    Generates human-readable explanations for simulation results.
    """

    @staticmethod
    def generate(
        stars_exist: bool,
        heavy_elements: bool,
        chemistry_score: float,
        habitability_score: float
    ) -> str:

        explanations = []

        if not stars_exist:
            explanations.append("No stable stars can form.")

        if not heavy_elements:
            explanations.append("Heavy elements are unlikely to form.")

        if chemistry_score < 0.5:
            explanations.append("Chemistry is too limited for complexity.")
        elif chemistry_score > 1.2:
            explanations.append("Rich chemistry supports complex structures.")

        if habitability_score > 0.7:
            explanations.append("Conditions are favorable for life.")
        elif habitability_score < 0.3:
            explanations.append("Conditions are hostile to life.")

        return " ".join(explanations) if explanations else "Moderate conditions."