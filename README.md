A simple game engine 

## Installation

### Prerequisites

- Developed with python 3.14 but 3.10 or higher should work

### Install Dependencies

It is advised to use a virtual environment
```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python engine.py
```

### Controls

- **Left Click (release)**: Select objects
- **Left Click + Drag**: Select and move kinematic nodes
- **Middle Click + Drag**: Pan the camera

## Project Structure

- `engine.py` - Main game engine and loop
- `game_object/` - GameObject classes including KinematicNode and KinematicSkeleton
- `utils/` - Utility functions and helper classes
