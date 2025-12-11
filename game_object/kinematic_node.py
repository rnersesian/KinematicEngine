from pyray import *
from . import GameObject
from utils.shapes import draw_rotated_ellipse
import math

class KinematicNode(GameObject):
    
    def __init__(self, position = Vector2(0, 0), rotation = 0, parent=None, radius = 10):
        super().__init__(position, rotation, parent)
        self.radius = radius
        self.front: KinematicNode = None
        self.back: KinematicNode = None
        
        self.update_rect(-radius, -radius, radius * 2, radius * 2)
    
    @property
    def position(self) -> Vector2:
        """Get the position of the KinematicNode"""
        return self._position

    @position.setter
    def position(self, value: Vector2):
        """Set position and propagate changes to connected nodes"""
        self._position = value
        if self.back:
            self.propagate_back()
        if self.front:
            self.propagate_front()
        
        
    def draw(self) -> None:
        """Draw KinematicNode"""
        super().draw()
        draw_circle_lines_v(self.position, self.radius, YELLOW)
        
    def get_angle(self) -> float:
        """Angle with front and back KinematicNone"""
        pass
    
    def propagate_front(self) -> None:
        """Update front node position to maintain connection at tangent"""
        if self.front:
            dx = self.front.position.x - self.position.x
            dy = self.front.position.y - self.position.y
            target_angle = math.atan2(dy, dx)
            target_position = Vector2(
                self.position.x + math.cos(target_angle) * (self.front.radius + self.radius),
                self.position.y + math.sin(target_angle) * (self.front.radius + self.radius))
            self.front.set_position(target_position)
            self.front.propagate_front()

    def propagate_back(self) -> None:
        """Update back node position to maintain connection at tangent"""
        if self.back:
            dx = self.back.position.x - self.position.x
            dy = self.back.position.y - self.position.y
            target_angle = math.atan2(dy, dx)
            target_position = Vector2(
                self.position.x + math.cos(target_angle) * (self.back.radius + self.radius),
                self.position.y + math.sin(target_angle) * (self.back.radius + self.radius))
            self.back.set_position(target_position)
            self.back.propagate_back()