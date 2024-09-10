# main.py

from ship import Ship
from wsim_dataclasses import ShipStats, Guns, Carronades, Crew
from wsim_enums import DamageType, CrewQuality

# Example of creating a ship instance
stats = ShipStats(
    hull=16,
    rigging=12,
    guns=Guns(left=20, right=20),
    carronades=Carronades(left=4, right=4),
    crew=Crew(total=200, sections=[67, 67, 66])
)
constellation = Ship(name="USS Constellation", ship_class="Frigate", crew_quality=CrewQuality.ELITE, stats=stats)

# Simulate combat using the DamageType enum
constellation.take_damage(DamageType.HULL, 3)  # Hull takes 3 damage
constellation.take_damage(DamageType.RIGGING, 2)  # Rigging takes 2 damage
constellation.take_damage(DamageType.CREW, 5)  # Crew takes 5 damage

# Log some actions
constellation.log_action("Moved to hex (4, 5)")
constellation.log_action("Engaged enemy ship")

# Output the state of the ship
print(constellation)
