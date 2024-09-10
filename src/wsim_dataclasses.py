# wsim_dataclasses.py
from dataclasses import dataclass


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
