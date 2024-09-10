# src/wsim_enums.py

from enum import Enum


class CrewQuality(Enum):
    ELITE = "Elite"
    CRACK = "Crack"
    AVERAGE = "Average"
    GREEN = "Green"
    POOR = "Poor"


class WindDirection(Enum):
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"


class ShipClass(Enum):
    FRIGATE = "Frigate"
    SHIP_OF_THE_LINE = "Ship of the Line"


class DamageType(Enum):
    HULL = "hull"
    RIGGING = "rigging"
    CREW = "crew"
    GUNS_LEFT = "guns_left"
    GUNS_RIGHT = "guns_right"
    CARRONADES_LEFT = "carronades_left"
    CARRONADES_RIGHT = "carronades_right"
