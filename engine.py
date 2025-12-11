from pyray import *
from game_object import *
from utils import *
import math

class GameEngine:
    
    def __init__(self, window_width=1200, window_height=900, window_name="KinematicEngine"):
        """Initialize the game engine with window settings and default game objects."""
        self.root = GameObject()
        
        self.root.add_child(KinematicSkeleton(position=Vector2(500, 700), node_radiuses=[30,40,20,10,5]))

        self.selected: GameObject = None
        self.select_radius: float = 5.
        
        self.delta: float = 1.0 / 60.0
        self.time: float = 0
        
        self.window_width: int = window_width
        self.window_height: int = window_height
        self.window_name: str = window_name

        self.camera: Camera2D = Camera2D()
        self.camera.target = Vector2(0, 0) # TODO: wut ?
        self.camera.offset = Vector2(0, 0)
        self.camera.rotation = 0.0
        self.camera.zoom = 1.0
        
        self.mouse = Mouse()
        
        self.grid: InfiniteGrid2D = InfiniteGrid2D(100, 100)
        
        self.background_color: Color = DARKGRAY
        
        self.DebugList: list[ScreenLogger] = [self.mouse]
        
        self.debug_mode = False
        
        
    def run(self) -> None:
        """Start the main game loop and handle rendering."""
        init_window(self.window_width, self.window_height, self.window_name)
        
        while not window_should_close():
            begin_drawing()
            clear_background(self.background_color)
            
            begin_mode_2d(self.camera)
            
            self.update()
            end_mode_2d()
            
            end_drawing()
        close_window()

        
    def draw_gizmo(self) -> None:
        """Drawing gizmo with X and Y axis"""
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
        

    def update(self) -> None:
        """Where the behaviour of the engine is coded"""
        # Manage time variables
        self.delta = get_frame_time()
        self.time += self.delta
        
        # Mouse inputs
        self.manage_mouse()
        
        self.grid.draw()
        
        for gameobject in self.root.children:
            gameobject.draw()
        
        if self.selected:
            self.selected.draw_rect()
            self.draw_gizmo()
            
        for i in range(len(self.DebugList)):
            draw_text(self.DebugList[i].log_on_screen(), 20 - int(self.camera.offset.x), 20 - int(self.camera.offset.y) + i * 30, 20, WHITE)
        


    def manage_mouse(self) -> None:
        """Handle mouse input for camera movement, object selection, and dragging."""
        mouse = self.mouse
        # Update mouse data
        mouse.position = get_mouse_position()
        mouse.delta = get_mouse_delta()
        mouse.world_position = vector2_subtract(mouse.position, self.camera.offset)
        
        if is_mouse_button_down(0) and self.selected and self.selected.is_in_rect(mouse.world_position):
            mouse.grab = True
        elif is_mouse_button_down(0) is False:
            mouse.grab = False
        
        if is_mouse_button_down(2): 
            # Camera movement with middle click
            self.camera.offset = vector2_add(self.camera.offset, mouse.delta)
            mouse.grab = False
        elif is_mouse_button_released(0) and vector2_length(mouse.delta) < 0.05:
            # Select gameobject if mouse is still
            self.click_select_object()
        
        if is_mouse_button_down(0) and self.selected and mouse.grab is True and vector2_length(mouse.delta) > 0:
            # Move grabbed object
            self.selected.position = vector2_add(self.selected.position, mouse.delta)
        
        
    def click_select_object(self) -> None:
        """Select the nearest game object within selection radius when clicked."""
        try:
            self.selected.is_selected = False
            self.selected = None
        except:
            pass
        selection_distance = math.inf
        temp_selected = None
        
        for g in self.root.list_all_gameobjects():
            distance_to_object = vector2_length(vector2_subtract(self.mouse.world_position, g.position))
            click_in_rect = g.is_in_rect(self.mouse.world_position)
            
            if click_in_rect and distance_to_object < selection_distance:
                temp_selected = g
                
        if temp_selected:
            self.selected = temp_selected
            self.selected.is_selected = True
    



    
def main() -> None:
    """Create and run the game engine instance."""
    engine = GameEngine()
    engine.run()


if __name__ == '__main__':
    main()