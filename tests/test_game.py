# tests/test_game.py

import pytest
from game import Game
from wsim_dataclasses import CubeCoordinate
from wsim_enums import WindDirection, ShipClass, CrewQuality, DamageType
from ship import Ship
from wsim_dataclasses import ShipStats, Guns, Carronades, Crew
from typing import Generator


@pytest.fixture
def create_game_with_ships() -> Generator[Game, None, None]:
    game = Game(board_size=(10, 10), wind_direction=WindDirection.N)

    stats = ShipStats(
        hull=16,
        rigging=12,
        guns=Guns(left=20, right=20),
        carronades=Carronades(left=4, right=4),
        crew=Crew(total=200, sections=[67, 67, 66])
    )

    ship1 = Ship(name="USS Constellation", ship_class=ShipClass.FRIGATE, crew_quality=CrewQuality.ELITE, stats=stats)
    ship2 = Ship(name="HMS Victory", ship_class=ShipClass.SHIP_OF_THE_LINE, crew_quality=CrewQuality.CRACK, stats=stats)

    game.add_ship(ship1, CubeCoordinate(0, 1, -1))
    game.add_ship(ship2, CubeCoordinate(1, 0, -1))

    yield game


def test_ship_positions(create_game_with_ships: Game) -> None:
    game = create_game_with_ships

    assert game.get_ship_position("USS Constellation") == CubeCoordinate(0, 1, -1)
    assert game.get_ship_position("HMS Victory") == CubeCoordinate(1, 0, -1)


def test_move_ship(create_game_with_ships: Game) -> None:
    game = create_game_with_ships

    game.move_ship("USS Constellation", CubeCoordinate(1, -1, 0))
    assert game.get_ship_position("USS Constellation") == CubeCoordinate(1, -1, 0)
