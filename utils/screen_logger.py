from abc import ABC, abstractmethod

class ScreenLogger(ABC):
    def __init__(self):
        """Initialize the ScreenLogger base class"""
        pass

    @abstractmethod
    def log_on_screen(self) -> str:
        """Return a string to be displayed on screen for debugging"""
        pass