"""
File: sdkp/constants.py
Framework: FatherTimeSDKP (Size, Density, Kinetic Principle)
Description: Immutable constants, including 3-6-9 scaling parameters, 
             prime terminators, and proprietary reference velocities.
             
NOTICE: Core logic within this framework is protected intellectual property.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class SDKPConstants:
    # SD&N (Shape Dimension Number) Vortex Baselines
    SCALE: float = 3.0
    DENSITY: float = 6.0
    KINETIC: float = 9.0

    # Reference Velocities
    SPEED_OF_LIGHT: float = 299_792_458.0
    EARTH_ORBITAL_SPEED: float = 29_780.0

    # Validation & Equilibrium Parameters
    PRIME_TERMINATOR: int = 13
    DECOHERENCE_BASELINE: float = 1.000000
