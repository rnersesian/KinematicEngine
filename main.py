from pyray import *
from game_object import *
import math

init_window(1200, 900, "Hello")


# self.gameobjects: list[GameObject] = [
#     KinematicNode(position=Vector2(200, 200)),
#     KinematicNode(position=Vector2(400, 300)),
#     KinematicNode(position=Vector2(350, 550)),
# ]

# self.gameobjects[0].is_selected = True
# self.selected: GameObject = None

# self.time = 0
# self.delta = 1.0/ 60.0

# select_radius = 5


# def select_on_clic(_gameobjects: list[GameObject]) -> GameObject:
#     temp_selected = None
#     selection_distance = math.inf
#     mouse_position = get_mouse_position()
    
#     for g in _gameobjects:
#         distance_to_object = vector2_length(vector2_subtract(mouse_position, g.position))
#         if distance_to_object < select_radius and distance_to_object < selection_distance:
#             temp_selected = g
#     self.selected = temp_selected
#     self.selected.is_selected = True



# while not window_should_close():
#     begin_drawing()
#     clear_background(DARKGRAY)

#     self.delta = get_frame_time()
#     self.time += self.delta
    
#     if is_key_pressed(KEY_Q): # type: ignore
#         self.gameobjects[self.selected].is_selected = False
#         self.selected = (self.selected - 1) % len(self.gameobjects)
#         self.gameobjects[self.selected].is_selected = True
#     elif is_key_pressed(KEY_E): # type: ignore
#         self.gameobjects[self.selected].is_selected = False
#         self.selected = (self.selected + 1) % len(self.gameobjects)
#         self.gameobjects[self.selected].is_selected = True

#     for gameobject in self.gameobjects:
#         gameobject.Draw()
    
#     mouse_delta = get_mouse_delta()
#     if is_mouse_button_released(0) and vector2_length(mouse_delta) < 0.1:
#         select_on_clic()
#     elif is_mouse_button_down(0):
#         try:
#             self.selected.Translate(get_mouse_delta())
#         except:
#             pass
#     end_drawing()
# close_window()





class GameEngine:
    
    def __init__(self):
        self.gameobjects: list[GameObject] = [
            KinematicNode(position=Vector2(200, 200)),
            KinematicNode(position=Vector2(400, 300)),
            KinematicNode(position=Vector2(350, 550)),
        ]
        self.selected: GameObject = None
        self.select_radius = 5.
        
        self.delta: float = 1.0 / 60.0
        self.time: float = 0
        
        background_color: Color = DARKGRAY
        
        
    def Run(self):
        while not window_should_close():
            begin_drawing()
            clear_background(DARKGRAY)

            self.delta = get_frame_time()
            self.time += self.delta
            
            self.Update()
            self.DrawGizmo()
            
            end_drawing()
        close_window()
        
        
    def DrawGizmo(self):
        if self.selected is None:
            return
        draw_line(
            int(self.selected.position.x),
            int(self.selected.position.y),
            int(self.selected.position.x + math.cos(self.selected.rotation) * 30),
            int(self.selected.position.y + math.sin(self.selected.rotation) * 30),
            GREEN
        )

        draw_line(
            int(self.selected.position.x),
            int(self.selected.position.y),
            int(self.selected.position.x + math.cos(self.selected.rotation - (math.pi / 2)) * 30),
            int(self.selected.position.y + math.sin(self.selected.rotation - (math.pi / 2)) * 30),
            RED
        )

        draw_rectangle(
            int(self.selected.position.x - 3),
            int(self.selected.position.y - 3),
            6,
            6,
            BLUE
        )
        

    def Update(self):

        for gameobject in self.gameobjects:
            gameobject.Draw()
        
        mouse_delta = get_mouse_delta()
        
        if is_mouse_button_released(0) and vector2_length(mouse_delta) < 0.1:
        # Object selection
            self.select_on_clic()
        elif is_mouse_button_down(0):
        # Object Translation
            try:
                self.selected.Translate(get_mouse_delta())
            except:
                pass
            

    def select_on_clic(self) -> GameObject:
        try:
            self.selected.is_selected = False
            self.selected = None
        except:
            pass
        selection_distance = math.inf
        mouse_position = get_mouse_position()
        temp_selected = None
        
        for g in self.gameobjects:
            distance_to_object = vector2_length(vector2_subtract(mouse_position, g.position))
            
            if distance_to_object < self.select_radius and distance_to_object < selection_distance:
                temp_selected = g
        if temp_selected:
            self.selected = temp_selected
            self.selected.is_selected = True
        
    
    
def main():
    engine = GameEngine()
    engine.Run()


if __name__ == '__main__':
    main()