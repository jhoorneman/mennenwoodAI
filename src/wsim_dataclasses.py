# wsim_dataclasses.py
from dataclasses import dataclass

@dataclass
class CubeCoordinate:
    """See: https://www.redblobgames.com/grids/hexagons/#coordinates-cube"""
    q: int  # x-coordinate in cube system
    r: int  # y-coordinate in cube system
    s: int  # z-coordinate in cube system

    def __post_init__(self):
        if self.q + self.r + self.s != 0:
            raise ValueError("Invalid cube coordinates. The sum of q, r, and s must be 0.")


@dataclass
class Guns:
    left: int
    right: int


@dataclass
class Carronades:
    left: int
    right: int


@dataclass
class Crew:
    total: int
    sections: list[int]


@dataclass
class ShipStats:
    hull: int
    rigging: int
    guns: Guns
    carronades: Carronades
    crew: Crew
