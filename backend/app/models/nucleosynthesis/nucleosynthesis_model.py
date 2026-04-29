class NucleosynthesisModel:
    """
    Determines whether heavy elements can form.
    """

    @staticmethod
    def evaluate(strong_force: float) -> bool:
        """
        Smooth transition instead of hard cutoff.
        """

        return 0.7 < strong_force < 1.3