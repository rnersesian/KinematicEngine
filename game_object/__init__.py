from pyray import *
from utils import ScreenLogger
from abc import ABC, abstractmethod
import math

class GameObject(ScreenLogger, ABC):
    def __init__(self, position: Vector2 = Vector2(0, 0), rotation: float = 0, parent = None):
        self.children: list[GameObject] = []
        self.position: Vector2 = position
        self.rotation: float = rotation # TODO: Make it a property if clamping value is needed
        self.scale = Vector2(1,1)
        self.parent = parent
        self.is_selected = False
        self.rect: Rectangle = Rectangle(-20, -20, 40, 40)

    def Draw(self) -> None:
        if self.is_selected is True:
             draw_rectangle_lines(
                int(self.position.x + self.rect.x),
                int(self.position.y + self.rect.y),
                int(self.rect.width),
                int(self.rect.height),
                BLUE
            )

    def Update(self) -> None:
        """GameObject's behaviour each frame"""
        pass
    
    def Translate(self, vec2: Vector2) -> None:
        """Add vector to position"""
        self.position = vector2_add(self.position, vec2)
        
    def Rotate(self, amount: float) -> None:
        """Add amount to rotation"""
        self.rotation += amount

    def Scale(self, amount: Vector2) -> None:
        """Multiply gameobject's scale"""
        self.scale.x *= amount.x
        self.scale.y *= amount.y

    def LogOnScreen(self) -> str:
        """By default, shows gameobject's position, scale and rotation"""
        return f'GameObject - Pos({int(self.position.x)}; {int(self.position.y)})\t - Scale({self.scale.x:.2f}; {self.scale.y:.2f})\t - Rot({self.rotation:.2f})'

    def UpdateRect(self, x: float, y: float, w: float, h: float) -> None:
        """Update gameobject rect (used mainly for selection)"""
        self.rect.x = x
        self.rect.y = y
        self.rect.width = w
        self.rect.height = h
        
from .kinematic_node import KinematicNode
from .infinite_grid2d import InfiniteGrid2D

__all__ = ["GameObject", "KinematicNode", "InfiniteGrid2D"]
Vector2