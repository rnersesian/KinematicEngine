from abc import ABC, abstractmethod

class ScreenLogger(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def log_on_screen(self) -> str:
        pass