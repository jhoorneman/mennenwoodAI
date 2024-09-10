# ship.py

from dataclasses import dataclass
from wsim_dataclasses import ShipStats, Guns, Carronades, Crew
from wsim_enums import DamageType, CrewQuality
from typing import List


@dataclass
class Ship:
    name: str
    ship_class: str  # Can expand to Enum later for more detailed ship types
    crew_quality: CrewQuality
    stats: ShipStats
    log: List[str] = None
    position: tuple[int, int] = None  # Hex coordinates on the board
    attitude_to_wind: str = "A"  # Default wind attitude

    def __post_init__(self):
        if self.log is None:
            self.log = []
        if self.position is None:
            self.position = (0, 0)  # Default position on the map

    def set_crew(self, total_crew: int) -> None:
        """
        Set up the total crew and divide them into sections.
        """
        self.stats.crew.total = total_crew
        self.stats.crew.sections = [total_crew // 3] * 3

    def take_damage(self, damage_type: DamageType, amount: int) -> None:
        """
        Apply damage to the ship, either to hull, crew, guns, rigging, or carronades.

        :param damage_type: Type of damage (as defined in the DamageType enum).
        :param amount: The amount of damage taken.
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
        return (f"Ship({self.name}, Class: {self.ship_class}, Hull: {self.stats.hull}, "
                f"Rigging: {self.stats.rigging}, Crew: {self.stats.crew.sections}, "
                f"Guns: Left={self.stats.guns.left}, Right={self.stats.guns.right})")
