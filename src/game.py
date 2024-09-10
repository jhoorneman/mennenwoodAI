# src/game.py

from wsim_dataclasses import CubeCoordinate
from wsim_enums import WindDirection
from ship import Ship
from typing import Dict, Tuple


class Game:
    ships: Dict[str, Ship]
    wind_direction: WindDirection
    board_size: Tuple[int, int]

    def __init__(self, board_size: Tuple[int, int] = (10, 10), wind_direction: WindDirection = WindDirection.N) -> None:
        self.ships: Dict[str, Ship] = {}
        self.wind_direction = wind_direction
        self.board_size = board_size

    def add_ship(self, ship: Ship, position: CubeCoordinate) -> None:
        """
        Adds a ship to the game at the specified cube coordinate on the board.
        """
        ship.set_position(position)
        self.ships[ship.name] = ship

    def get_ship(self, ship_name: str) -> Ship:
        """
        Retrieve a ship by its name. Raises an error if the ship does not exist.
        :param ship_name: The name of the ship.
        :return: The Ship object.
        """
        if ship_name not in self.ships:
            raise ValueError(f"Ship {ship_name} not found.")
        return self.ships[ship_name]

    def move_ship(self, ship_name: str, direction: CubeCoordinate) -> None:
        """
        Moves a ship based on wind direction and movement rules.
        """
        ship = self.get_ship(ship_name)
        ship.move(direction, self.wind_direction)

    def get_ship_position(self, ship_name: str) -> CubeCoordinate:
        """
        Returns the position of a ship.
        """
        return self.get_ship(ship_name).position

    def update_wind(self, new_wind_direction: WindDirection) -> None:
        """
        Updates the wind direction.
        """
        self.wind_direction = new_wind_direction

    def __repr__(self) -> str:
        game_state = f"Game State: Board size {self.board_size}, Wind: {self.wind_direction.name}\n"
        for ship_name, ship in self.ships.items():
            game_state += f"{ship_name} at position {ship.position} | {ship}\n"
        return game_state
