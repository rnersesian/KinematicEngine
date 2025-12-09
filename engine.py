from pyray import *
from game_object import *
import math

class GameEngine:
    
    def __init__(self, window_width=1200, window_height=900, window_name="KinematicEngine"):
        self.gameobjects: list[GameObject] = [
            KinematicNode(position=Vector2(200, 200)),
            KinematicNode(position=Vector2(400, 300)),
            KinematicNode(position=Vector2(350, 550)),
        ]
        self.selected: GameObject = None
        self.select_radius = 5.
        
        self.delta: float = 1.0 / 60.0
        self.time: float = 0
        
        self.window_width = window_width
        self.window_height = window_height
        self.window_name = window_name

        self.camera: Camera2D = Camera2D()
        self.camera.target = Vector2(0, 0)
        self.camera.offset = Vector2(0, 0) # TODO : check what the fuck it is
        self.camera.rotation = 0.0
        self.camera.zoom = 1.0
        
        background_color: Color = DARKGRAY
        
        
    def Run(self):
        init_window(self.window_width, self.window_height, self.window_name)
        
        while not window_should_close():
            begin_drawing()
            clear_background(DARKGRAY)

            self.delta = get_frame_time()
            self.time += self.delta

            # TODO : Implement camera with mouse button
            begin_mode_2d(self.camera)
            
            self.Update()
            self.DrawGizmo()

            end_mode_2d()

            
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