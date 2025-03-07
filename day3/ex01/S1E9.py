from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class Character"""
    @abstractmethod
    def __init__(self, first_name, is_alive = True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
    @abstractmethod
    def die(self):
        """Character die method"""
        self.is_alive = False

class Stark(Character):
    """Stark Class that inherits from Character"""
    def __init__(self, first_name, is_alive = True):
        """Stark constructor"""
        super().__init__(first_name, is_alive)
    def die(self):
        """Stark die method"""
        self.is_alive = False