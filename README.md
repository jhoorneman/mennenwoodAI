# MennenwoodAI
Helper tool for the board game Wooden Ships and Iron Men. AI assisted continuation of https://github.com/tlaeven/mennenwood. See for complete rules of the game: https://archive.org/details/wooden-ships-amp-iron-men_compress/page/7/mode/2up

## Installation
This project is managed using poetry. To install:
```bash
pip install poetry
poetry install
```
Dependencies can be added with:
```bash
poetry add <package-name>
```
Or dependencies needed only for development (such as pytest)
```bash
poetry add --dev <package-name>
```
Tests can be run in Pycharm or from the commandline with:
```bash
poetry run pytest
```

## Features

**Ship Management System**
 - Track all relevant ship stats (hull, crew, guns, rigging, etc.).
 - Handle ship movement, position relative to wind, and actions each turn.
 - Keep a log of damage and status changes for each ship, updating automatically after each turn or event.

**Hit Table Integration**
 - Automatically apply hit table results based on user input (such as the dice roll, ship class, crew quality, range, etc.).
 - Modify damage based on factors like raking, crew quality, and ammunition type.

**Combat Resolution**
 - Handle all aspects of combat, from determining if a shot hits, to marking off damage on the appropriate ship (hull, crew, rigging, or guns).
 - Handle melee (boarding) combat, calculating crew strength and tracking casualties.

**Minimal Input**
 - Users will only need to input essential information like ship movement, dice rolls, and targets. The tool will handle calculations and updates.
 - Automate updates to the log pad after each action, reducing the manual input.

## Backend Structure

Core logic to:
 - Track Ships: Each ship will have an object or class to represent its state.
 - Handle Combat: A function for calculating combat results, referencing hit tables automatically.
 - Simulate the Turn System: Simulate a turn-by-turn system that tracks movement and actions.

## Implementation Plan

1. Set Up Data Structure for Ships: Each ship will have properties like hull, crew, rigging, guns, and their current state.
    - Start with basic attributes: name, class, crew quality, and ship-specific stats (guns, hull, rigging).
2. Hit Table Logic: Create functions that simulate the hit tables.
    - Take inputs like number of guns firing, range, crew quality, etc., and return the hit results.
 3. Combat Mechanics: Build out the backend logic for combat, tracking the flow of each engagement and updating the ship state.
