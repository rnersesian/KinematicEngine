from pyray import *
from . import GameObject

class Grid2D(GameObject):
    
    def __init__(self, position = Vector2(0,0), rotation = 0, parent=None):
        super().__init__(position, rotation, parent)
