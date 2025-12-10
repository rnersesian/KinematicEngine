from game_object import GameObject
from abc import ABC, abstractmethod

class Component(ABC):
    """Base class component"""
    def __init__(self, gameobject: GameObject):
        self.gameobject: GameObject = gameobject
        self.enabled = True

    @abstractmethod
    def update(self, delta: float) -> None:
        pass

__all__ = ["Component"]