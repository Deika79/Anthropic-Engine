class StellarModel:
    """
    Determines if stable stars can exist.
    """

    @staticmethod
    def evaluate(alpha: float, strong_force: float) -> bool:
        """
        Stars require balance between EM and strong force.
        """

        balance = abs(alpha - strong_force)

        return balance < 0.7