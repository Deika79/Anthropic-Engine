from pydantic import BaseModel, Field


class UniverseParameters(BaseModel):
    """
    Represents a simplified set of fundamental physical constants.
    All values are normalized relative to our universe (1.0 = our universe).
    """

    alpha: float = Field(
        default=1.0,
        gt=0,
        description="Fine-structure constant (electromagnetic interaction strength)"
    )

    strong_force: float = Field(
        default=1.0,
        gt=0,
        description="Strong nuclear force strength"
    )

    electron_mass: float = Field(
        default=1.0,
        gt=0,
        description="Electron mass (relative scale)"
    )

    cosmological_constant: float = Field(
        default=1.0,
        gt=0,
        description="Cosmological constant (vacuum energy density)"
    )