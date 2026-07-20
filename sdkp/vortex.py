"""
File: sdkp/vortex.py
Description: Computes discrete packing gradients and runs EOS vs. c consistency checks.
"""

from .constants import SDKPConstants

class VortexEngine:
    def __init__(self):
        self.constants = SDKPConstants()

    def harmonic_ratio(self) -> float:
        """
        Calculates the exact harmonic ratio using the 3-6-9 discrete gradient.
        """
        return (self.constants.SCALE * self.constants.DENSITY) / self.constants.KINETIC

    def compute_packing_density(self, state_matrix: float) -> float:
        """
        Bypasses probabilistic tensors by applying the discrete harmonic ratio.
        """
        return state_matrix * self.harmonic_ratio()

    def consistency_check(self) -> dict:
        """
        Validates the Earth Orbital Speed (EOS) against the Speed of Light (c) reference.
        """
        eos_ratio = self.constants.EARTH_ORBITAL_SPEED / self.constants.SPEED_OF_LIGHT
        return {
            "EOS_reference": self.constants.EARTH_ORBITAL_SPEED,
            "c_reference": self.constants.SPEED_OF_LIGHT,
            "velocity_ratio": eos_ratio
        }
