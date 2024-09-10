# tests/test_ship.py

import pytest
from ship import Ship
from wsim_enums import CrewQuality, DamageType
from wsim_dataclasses import ShipStats, Guns, Carronades, Crew


@pytest.fixture
def create_constellation():
    """
    Fixture to create a USS Constellation ship instance.
    """
    stats = ShipStats(
        hull=16,
        rigging=12,
        guns=Guns(left=20, right=20),
        carronades=Carronades(left=4, right=4),
        crew=Crew(total=200, sections=[67, 67, 66])
    )
    return Ship(name="USS Constellation", ship_class="Frigate", crew_quality=CrewQuality.ELITE, stats=stats)


def test_take_hull_damage(create_constellation):
    """
    Test that hull damage is correctly applied to the ship.
    """
    # Arrange
    constellation = create_constellation

    # Act
    constellation.take_damage(DamageType.HULL, 3)

    # Assert
    assert constellation.stats.hull == 13, "Hull damage not applied correctly"


def test_take_rigging_damage(create_constellation):
    """
    Test that rigging damage is correctly applied to the ship.
    """
    # Arrange
    constellation = create_constellation

    # Act
    constellation.take_damage(DamageType.RIGGING, 2)

    # Assert
    assert constellation.stats.rigging == 10, "Rigging damage not applied correctly"


def test_take_crew_damage(create_constellation):
    """
    Test that crew damage is correctly distributed across sections.
    """
    # Arrange
    constellation = create_constellation

    # Act
    constellation.take_damage(DamageType.CREW, 5)

    # Assert
    assert constellation.stats.crew.sections == [62, 67, 66], "Crew damage not applied correctly"


def test_log_actions(create_constellation):
    """
    Test that actions are correctly logged.
    """
    # Arrange
    constellation = create_constellation

    # Act
    constellation.log_action("Moved to hex (4, 5)")
    constellation.log_action("Engaged enemy ship")

    # Assert
    assert constellation.log == ["Moved to hex (4, 5)", "Engaged enemy ship"], "Log not updating correctly"
