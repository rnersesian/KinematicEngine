from .screen_logger import ScreenLogger
from pyray import Vector2

class Mouse(ScreenLogger):
    def __init__(self):
        """Initialize mouse with default position, world position, delta, and grab state."""
        self.position =  Vector2(0, 0)
        self.world_position = Vector2(0, 0)
        self.delta = Vector2(0, 0)
        self.grab = False
        
    def log_on_screen(self) -> str:
        """Return formatted string with mouse screen and world positions for debug display."""
        return f'Pos({self.position.x:.0f}; {self.position.y:.0f})\t-\tWorldPos({self.world_position.x:.0f}; {self.world_position.y:.0f})'
