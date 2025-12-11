from pyray import *
from . import GameObject

class InfiniteGrid2D:
    # TODO: Not urgent, make it infinite
    
    def __init__(self, cell_wdith: float, cell_height: float, show_grid=True, rotation=0):
        """Initialize the grid with cell dimensions and display settings"""
        self.cell_width: float = cell_wdith
        self.cell_height: float = cell_height
        self.show_grid = show_grid
        self.rotation: float = rotation


    def draw(self) -> None:
        """Draw the grid lines"""
        v1 = Vector2(0,0)
        v2 = Vector2(0,0)
        for x in range(-2000, 3000, self.cell_width):
            v1.x = v2.x = x
            v1.y = -2000
            v2.y = 3000
            draw_line_v(v1, v2, GRAY)
        
        for y in range(-2000, 3000, self.cell_width):
            v1.y = v2.y = y
            v1.x = -2000
            v2.x = 3000
            draw_line_v(v1, v2, GRAY)
