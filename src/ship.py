# src/ship.py

from dataclasses import dataclass
from wsim_dataclasses import ShipStats, CubeCoordinate
from wsim_enums import ShipClass, CrewQuality, DamageType
from typing import List


@dataclass
class Ship:
    name: str
    ship_class: ShipClass
    crew_quality: CrewQuality
    stats: ShipStats
    log: List[str] = None
    position: CubeCoordinate = None  # Ship's position on the hex board
    attitude_to_wind: str = "A"  # Default wind attitude

    def __post_init__(self) -> None:
        if self.log is None:
            self.log = []
        if self.position is None:
            self.position = CubeCoordinate(0, 0, 0)  # Default position

    def set_position(self, position: CubeCoordinate) -> None:
        """
        Set the ship's position on the board.
        """
        self.position = position
        self.log_action(f"Position set to {position}")

    def take_damage(self, damage_type: DamageType, amount: int) -> None:
        """
        Apply damage to the ship.
        """
        if damage_type == DamageType.HULL:
            self.stats.hull = max(self.stats.hull - amount, 0)
        elif damage_type == DamageType.RIGGING:
            self.stats.rigging = max(self.stats.rigging - amount, 0)
        elif damage_type == DamageType.CREW:
            for i in range(amount):
                if self.stats.crew.sections[0] > 0:
                    self.stats.crew.sections[0] -= 1
                elif self.stats.crew.sections[1] > 0:
                    self.stats.crew.sections[1] -= 1
                elif self.stats.crew.sections[2] > 0:
                    self.stats.crew.sections[2] -= 1
        elif damage_type == DamageType.GUNS_LEFT:
            self.stats.guns.left = max(self.stats.guns.left - amount, 0)
        elif damage_type == DamageType.GUNS_RIGHT:
            self.stats.guns.right = max(self.stats.guns.right - amount, 0)
        elif damage_type == DamageType.CARRONADES_LEFT:
            self.stats.carronades.left = max(self.stats.carronades.left - amount, 0)
        elif damage_type == DamageType.CARRONADES_RIGHT:
            self.stats.carronades.right = max(self.stats.carronades.right - amount, 0)

    def log_action(self, action: str) -> None:
        """
        Add an entry to the ship's log for tracking.
        """
        self.log.append(action)

    def __repr__(self) -> str:
        return (f"Ship({self.name}, Class: {self.ship_class.value}, Hull: {self.stats.hull}, "
                f"Rigging: {self.stats.rigging}, Crew: {self.stats.crew.sections}, "
                f"Position: {self.position})")
