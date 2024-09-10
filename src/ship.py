# src/ship.py

from dataclasses import dataclass
from wsim_dataclasses import ShipStats, CubeCoordinate
from wsim_enums import ShipClass, CrewQuality, DamageType, WindDirection
from typing import List, Optional


@dataclass
class Ship:
    name: str
    ship_class: ShipClass
    crew_quality: CrewQuality
    stats: ShipStats
    log: List[str] = None
    position: CubeCoordinate = None  # Ship's position on the hex board
    attitude_to_wind: Optional[WindDirection] = None  # Wind relative to the ship's direction

    def __post_init__(self) -> None:
        if self.log is None:
            self.log = []
        if self.position is None:
            self.position = CubeCoordinate(0, 0, 0)  # Default position
        if self.attitude_to_wind is None:
            self.attitude_to_wind = WindDirection.N  # Default wind attitude

    def set_position(self, position: CubeCoordinate) -> None:
        """
        Set the ship's position on the board.
        """
        self.position = position
        self.log_action(f"Position set to {position}")

    def calculate_speed(self, wind_direction: WindDirection) -> int:
        """
        Calculate the ship's movement speed based on its attitude to the wind and rigging damage.
        Full speed = 1 hex, reduced speed = 0.5 hex (rounded to 1), minimal speed = no movement.
        """
        if self.attitude_to_wind == wind_direction:
            # Wind is fully favorable, full speed
            return 1
        elif abs(WindDirection[self.attitude_to_wind.name].value - WindDirection[wind_direction.name].value) == 2:
            # Wind is across, reduced speed
            return max(1, 1 // 2)
        else:
            # Sailing against the wind, minimal speed
            return 0

    def move(self, direction: CubeCoordinate, wind_direction: WindDirection) -> None:
        """
        Move the ship in a specific direction, adjusting based on wind influence.
        :param direction: The cube coordinate direction for movement.
        :param wind_direction: The current wind direction.
        """
        speed = self.calculate_speed(wind_direction)
        if speed > 0:
            # Move the ship based on speed and direction
            self.position = CubeCoordinate(
                self.position.q + direction.q * speed,
                self.position.r + direction.r * speed,
                self.position.s + direction.s * speed
            )
            self.log_action(f"Moved {speed} hexes in direction {direction}")
        else:
            self.log_action("Ship could not move due to wind.")

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
