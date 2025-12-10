from abc import ABC, abstractmethod

class ScreenLogger(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def LogOnScreen(self):
        pass