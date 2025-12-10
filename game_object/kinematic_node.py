from pyray import *
from . import GameObject
from utils.shapes import draw_rotated_ellipse

class KinematicNode(GameObject):
    
    def __init__(self, position = Vector2(0, 0), rotation = 0, parent=None, radius = 10):
        super().__init__(position, rotation, parent)
        self.radius = radius
    

    def Draw(self) -> None:
        draw_circle_v(self.position, self.radius, YELLOW)