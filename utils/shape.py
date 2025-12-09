from pyray import *
import math

def draw_rotated_ellipse(center_x: float, center_y: float, radius_h: float, radius_v: float, rotation_degrees: float, color: Color):
    """Draw a rotated ellipse using rlPushMatrix"""
    rl_push_matrix()
    
    # Translate to center
    rl_translatef(center_x, center_y, 0)
    
    # Rotate
    rl_rotatef(math.degrees(rotation_degrees), 0, 0, 1)
    
    # Draw ellipse at origin (it's now rotated)
    draw_ellipse(0, 0, radius_h, radius_v, color)
    
    
    rl_pop_matrix()