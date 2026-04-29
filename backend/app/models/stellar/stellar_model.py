from app.models.universe import UniverseParameters


class StellarModel:
    """
    Simplified stellar stability model.

    Determines whether stable stars can exist based on:
    - electromagnetic force (alpha)
    - strong nuclear force
    """

    @staticmethod
    def evaluate(params: UniverseParameters) -> bool:
        alpha = params.alpha
        strong = params.strong_force

        # Simplified heuristic rules:

        # If electromagnetic force is too strong → fusion suppressed
        if alpha > 1.5:
            return False

        # If electromagnetic force is too weak → atoms unstable
        if alpha < 0.3:
            return False

        # If strong force is too weak → no stable nuclei
        if strong < 0.5:
            return False

        # If strong force is too strong → rapid collapse / no stable stars
        if strong > 1.5:
            return False

        return True