from pyray import *
from abc import ABC, abstractmethod
import math

class GameObject(ABC):
    def __init__(self, position: Vector2 = Vector2(0, 0), rotation: float = 0, parent = None):
        self.children: list[GameObject] = []
        self.position: Vector2 = position
        self.rotation: float = rotation
        self.scale = Vector2(1,1)
        self.parent = parent
        self.is_selected = False
    
    def Update(self):
        pass
    
    def Translate(self, vec2: Vector2):
        self.position = vector2_add(self.position, vec2)
        
    def Rotate(self, amount):
        self.rotation += amount

    @abstractmethod
    def Draw(self):
        pass

    def Scale(self, amount: Vector2):
        self.scale.x *= amount.x
        self.scale.y *= amount.y

        
from .kinematic_node import KinematicNode

__all__ = ["GameObject", "KinematicNode"]