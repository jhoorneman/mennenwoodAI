# wsim_enums.py
from enum import Enum


class CrewQuality(Enum):
    ELITE = 5
    CRACK = 4
    AVERAGE = 3
    GREEN = 2
    POOR = 1


class DamageType(Enum):
    HULL = "hull"
    RIGGING = "rigging"
    CREW = "crew"
    GUNS_LEFT = "guns_left"
    GUNS_RIGHT = "guns_right"
    CARRONADES_LEFT = "carronades_left"
    CARRONADES_RIGHT = "carronades_right"
