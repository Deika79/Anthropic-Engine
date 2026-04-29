class HabitabilityModel:
    """
    Aggregates different factors into a continuous habitability score.
    """

    @staticmethod
    def evaluate(
        stars_exist: bool,
        heavy_elements: bool,
        chemistry_score: float
    ) -> float:
        """
        Returns a continuous habitability score between 0 and 1.
        """

        # 🔥 Base: química (normalizada)
        base = chemistry_score / 2.0  # asumimos rango aprox 0–2

        # 🌟 Penalización si no hay estrellas
        if not stars_exist:
            base *= 0.2  # casi inhabitable pero no cero absoluto

        # ⚛️ Penalización si no hay elementos pesados
        if not heavy_elements:
            base *= 0.5

        # 📌 Clamp final
        return max(0.0, min(1.0, base))