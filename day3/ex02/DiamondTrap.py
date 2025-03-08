from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class DiamondTrap"""
    def __init__(self, first_name, is_alive=True):
        """King constructor"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """King eyes getter"""
        return self._eyes

    def set_eyes(self, color):
        """King eyes setter"""
        self._eyes = color

    def get_hairs(self):
        """King hair property"""
        return self._hair

    def set_hairs(self, color):
        """King hair setter"""
        self._hair = color
    
    eyes = property(get_eyes, set_eyes)
    hair = property(get_hairs, set_hairs)