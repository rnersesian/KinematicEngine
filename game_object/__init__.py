from pyray import *
from utils import ScreenLogger
from typing import Generator

class GameObject(ScreenLogger):
    def __init__(self, position: Vector2 = Vector2(0, 0), rotation: float = 0, parent = None):
        self.children: list[GameObject] = []
        self._position: Vector2 = position
        self.rotation: float = rotation # TODO: Make it a property if clamping value is needed
        self.scale = Vector2(1,1)
        self.parent = parent
        self.is_selected = False
        self.rect: Rectangle = Rectangle(0, 0, 0, 0)
        self.name = "" #TODO: take care when gameexplorer is implemented
        
    @property
    def position(self) -> Vector2:
        """Get the position of the GameObject"""
        return self._position

    @position.setter
    def position(self, value: Vector2):
        """Set the position of the GameObject"""
        self._position = value

    def draw(self) -> None:
        """Draw the GameObject and all its children"""
        for child in self.children:
            child.draw()
    
    def draw_debug(self) -> None:
        """What should be displayed when debug mode is on"""
        pass

    def update(self) -> None:
        """GameObject's behaviour each frame"""
        pass
    
    def translate(self, vec2: Vector2) -> None:
        """Add vector to position"""
        self.position = vector2_add(self.position, vec2)
    
    def set_position(self, vec2: Vector2) -> None:
        """Set position directly without triggering property setter"""
        self._position = vec2


    def rotate(self, amount: float) -> None:
        """Add amount to rotation"""
        self.rotation += amount
        

    def scale(self, amount: Vector2) -> None: # TODO make it actually do something
        """Multiply gameobject's scale"""
        self.scale.x *= amount.x
        self.scale.y *= amount.y

    def log_on_screen(self) -> str:
        """By default, shows gameobject's position, scale and rotation"""
        return f'GameObject - Pos({int(self.position.x)}; {int(self.position.y)})\t - Scale({self.scale.x:.2f}; {self.scale.y:.2f})\t - Rot({self.rotation:.2f})'

    def update_rect(self, x: float, y: float, w: float, h: float) -> None:
        """Update gameobject rect (used mainly for selection)"""
        self.rect.x = x
        self.rect.y = y
        self.rect.width = w
        self.rect.height = h
        
    def draw_rect(self):
        """Draw the GameObject's selection rectangle"""
        draw_rectangle_lines(
            int(self.position.x + self.rect.x),
            int(self.position.y + self.rect.y),
            int(self.rect.width),
            int(self.rect.height),
            BLUE
        )
        
    def is_in_rect(self, point: Vector2) -> bool:
        """Check if some point is in rect"""
        return (
            point.x > self.rect.x + self.position.x and
            point.y > self.rect.y + self.position.y and
            point.x < self.rect.x + self.rect.width + self.position.x and
            point.y < self.rect.y + self.rect.height + self.position.y   
        )
    
    def add_child(self, child: GameObject) -> None:
        """Add child to GameObject"""
        self.children.append(child)
        child.parent = self
        
    def list_all_gameobjects(self) -> Generator[GameObject, None, None]:
        """Recursively yield all child GameObjects in the hierarchy"""
        for gameobject in self.children:
            yield gameobject
            if len(gameobject.children) > 0:
                yield from gameobject.list_all_gameobjects()

            
from .kinematic_node import KinematicNode
from .infinite_grid2d import InfiniteGrid2D
from .kinematic_skeleton import KinematicSkeleton

__all__ = ["GameObject", "KinematicNode", "InfiniteGrid2D", "KinematicSkeleton"]