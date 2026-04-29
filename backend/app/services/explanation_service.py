from app.models.universe import UniverseParameters


class ExplanationService:
    """
    Generates human-readable scientific explanations
    based on simulation results.
    """

    @staticmethod
    def generate(
        params: UniverseParameters,
        stars_exist: bool,
        heavy_elements: bool,
        chemistry_score: float,
        habitability: float
    ) -> str:

        explanations = []

        # Stellar explanation
        if not stars_exist:
            if params.alpha > 1.5:
                explanations.append(
                    "Electromagnetic interaction is too strong, preventing stable nuclear fusion in stars."
                )
            elif params.alpha < 0.3:
                explanations.append(
                    "Electromagnetic interaction is too weak to sustain stable atomic structures."
                )
            elif params.strong_force < 0.5:
                explanations.append(
                    "The strong nuclear force is too weak to form stable nuclei."
                )
            elif params.strong_force > 1.5:
                explanations.append(
                    "The strong nuclear force is too strong, leading to unstable stellar behavior."
                )
            else:
                explanations.append(
                    "Stars cannot form under these physical conditions."
                )

        else:
            explanations.append(
                "Stable stars can form, enabling long-term energy sources."
            )

        # Heavy elements
        if not heavy_elements:
            explanations.append(
                "Heavy element formation (such as carbon and oxygen) is not viable."
            )
        else:
            explanations.append(
                "Heavy elements can form through stellar nucleosynthesis."
            )

        # Chemistry
        if chemistry_score < 0.5:
            explanations.append(
                "Chemical complexity is severely limited."
            )
        elif chemistry_score < 1.0:
            explanations.append(
                "Chemical systems are possible but less stable or diverse."
            )
        else:
            explanations.append(
                "Rich chemical complexity is possible."
            )

        # Habitability summary
        if habitability == 0:
            explanations.append(
                "Overall, this universe is not compatible with complex life."
            )
        elif habitability < 0.5:
            explanations.append(
                "This universe marginally supports simple forms of complexity."
            )
        else:
            explanations.append(
                "This universe is broadly compatible with complex structures and potentially life."
            )

        return " ".join(explanations)