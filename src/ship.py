# src/ship.py

from dataclasses import dataclass
from wsim_dataclasses import ShipStats, CubeCoordinate
from wsim_enums import ShipClass, CrewQuality, DamageType, WindDirection, HitResult
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

    def fire_at(self, target_ship: 'Ship', range_in_hexes: int, dice_roll: int) -> None:
        """
        Handle firing at a target ship. This method uses hit tables and dice rolls to determine
        the result of the attack and applies damage to the target.
        :param target_ship: The target ship being fired upon.
        :param range_in_hexes: The distance between the ships in hexes.
        :param dice_roll: The result of the dice roll that will be used to consult the hit table.
        """
        # Simplified range check
        if range_in_hexes > 5:
            self.log_action(f"Attempted to fire at {target_ship.name}, but target is out of range.")
            return

        # Get the hit result based on the range, dice roll, and target ship stats
        hit_result = self.consult_hit_table(range_in_hexes, dice_roll)

        # Log the result
        self.log_action(
            f"Fired at {target_ship.name} at range {range_in_hexes} with a roll of {dice_roll}. Result: {hit_result.name}")

        # Apply the damage to the target ship based on the hit result
        self.apply_damage_to_target(target_ship, hit_result)

    def consult_hit_table(self, range_in_hexes: int, dice_roll: int) -> HitResult:
        """
        Consult the hit table based on the range and dice roll to determine the result.
        :param range_in_hexes: The distance between the ships in hexes.
        :param dice_roll: The result of the dice roll.
        :return: A HitResult enum describing the hit result.
        """
        # Placeholder for hit table logic. This should reference the actual hit tables.
        if dice_roll > 10:  # Example threshold for a hit
            return HitResult.HULL_HIT
        elif dice_roll > 5:
            return HitResult.RIGGING_HIT
        else:
            return HitResult.MISS

    def apply_damage_to_target(self, target_ship: 'Ship', hit_result: HitResult) -> None:
        """
        Apply damage to the target ship based on the hit result.
        :param target_ship: The ship that is being fired upon.
        :param hit_result: The result of the hit (as a HitResult enum).
        """
        if hit_result == HitResult.HULL_HIT:
            target_ship.take_damage(DamageType.HULL, 2)  # Apply hull damage
        elif hit_result == HitResult.RIGGING_HIT:
            target_ship.take_damage(DamageType.RIGGING, 1)  # Apply rigging damage
        else:
            self.log_action(f"Attack on {target_ship.name} missed.")

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
