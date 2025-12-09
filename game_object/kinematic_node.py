from pyray import *
from . import GameObject
from utils.shapes import draw_rotated_ellipse

class KinematicNode(GameObject):
    
    def __init__(self, position = Vector2(0, 0), rotation = 0, parent=None, radius = 10):
        super().__init__(position, rotation, parent)
        self.radius = radius
    

    def Draw(self):
        # draw_circle_v(self.position, self.radius, YELLOW)
        draw_rotated_ellipse(
            self.position.x,
            self.position.y,
            self.radius * self.scale.x,
            self.radius * self.scale.y,
            self.rotation,
            YELLOW
        )