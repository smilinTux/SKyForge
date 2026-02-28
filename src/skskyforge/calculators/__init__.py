"""
SKSkyforge calculators.

Copyright (C) 2025 smilinTux
SK = staycuriousANDkeepsmilin 🐧

This file is part of SKSkyforge.
Licensed under AGPL-3.0. See LICENSE for details.
"""

from .numerology import (
    calculate_life_path,
    calculate_personal_year,
    calculate_personal_month,
    calculate_personal_day,
    calculate_universal_day,
    calculate_numerology_for_day,
    reduce_to_single_digit,
)

from .biorhythm import (
    calculate_biorhythm_for_day,
    calculate_cycle_value,
    get_cycle_phase,
    is_critical_day,
    PHYSICAL_CYCLE,
    EMOTIONAL_CYCLE,
    INTELLECTUAL_CYCLE,
)

from .moon import (
    calculate_moon_data,
    get_phase_from_angle,
    get_zodiac_sign_from_longitude,
    ZODIAC_SIGNS,
    SIGN_ELEMENTS,
    SIGN_MODALITIES,
)

from .solar import (
    calculate_sun_position,
    get_sun_sign,
    calculate_house_focus,
    HOUSE_THEMES,
)

from .planets import (
    calculate_planetary_positions,
    calculate_aspects,
    calculate_hd_gates,
    longitude_to_hd_gate,
    PLANET_NAMES,
    MAJOR_ASPECTS,
)

__all__ = [
    # Numerology
    "calculate_life_path",
    "calculate_personal_year",
    "calculate_personal_month",
    "calculate_personal_day",
    "calculate_universal_day",
    "calculate_numerology_for_day",
    "reduce_to_single_digit",
    # Biorhythm
    "calculate_biorhythm_for_day",
    "calculate_cycle_value",
    "get_cycle_phase",
    "is_critical_day",
    "PHYSICAL_CYCLE",
    "EMOTIONAL_CYCLE",
    "INTELLECTUAL_CYCLE",
    # Moon
    "calculate_moon_data",
    "get_phase_from_angle",
    "get_zodiac_sign_from_longitude",
    "ZODIAC_SIGNS",
    "SIGN_ELEMENTS",
    "SIGN_MODALITIES",
    # Solar
    "calculate_sun_position",
    "get_sun_sign",
    "calculate_house_focus",
    "HOUSE_THEMES",
    # Planets
    "calculate_planetary_positions",
    "calculate_aspects",
    "calculate_hd_gates",
    "longitude_to_hd_gate",
    "PLANET_NAMES",
    "MAJOR_ASPECTS",
]
