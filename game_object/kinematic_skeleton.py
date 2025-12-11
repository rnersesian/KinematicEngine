from .kinematic_node import KinematicNode
from copy import copy
from . import GameObject
from pyray import *

class KinematicSkeleton(GameObject):
    
    def __init__(self, position = Vector2(0, 0), rotation = 0, parent=None, node_radiuses: list[float] = []):
        super().__init__(position, rotation, parent)
        current_pos = Vector2(position.x, position.y)
        self.nodes: list[KinematicNode] = []
        
        for i, radius in enumerate(node_radiuses):
            if i > 0:
                current_pos.x -= (node_radiuses[i-1] + radius)

            child_to_add: KinematicNode = KinematicNode(position=Vector2(current_pos.x, current_pos.y), radius=radius, rotation=0)
            self.add_child(child_to_add)
            self.nodes.append(child_to_add)

            #TODO: bad code, clean later
            if i > 0:
                child_to_add.front = self.nodes[i - 1]
                self.nodes[i - 1].back = child_to_add
            
    def draw(self):
        """Draw the skeleton nodes and connecting lines"""
        super().draw()
        for i in range(len(self.nodes) - 1):
            draw_line_v(self.nodes[i].position, self.nodes[i + 1].position, WHITE)