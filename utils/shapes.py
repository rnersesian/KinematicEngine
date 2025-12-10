"""Functions that draws custom shapes"""

from pyray import *
import math

def draw_rotated_ellipse(center_x: float, center_y: float, radius_h: float, radius_v: float, rotation_degrees: float, color: Color) -> None:
    """Draw a rotated ellipse"""
    rl_push_matrix()
    rl_translatef(center_x, center_y, 0)
    rl_rotatef(math.degrees(rotation_degrees), 0, 0, 1)
    draw_ellipse(0, 0, radius_h, radius_v, color)
    rl_pop_matrix()