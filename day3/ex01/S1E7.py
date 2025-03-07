from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class that inherits from Character"""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hair="dark"):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hair = hair

    def __str__(self):
        """Baratheon str method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Baratheon repr method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"
    
    def die(self):
        """Baraetheon die method"""
        self.is_alive = False



class Lannister(Character):
    """Lannister Class that inherits from Character"""
    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hair="light"):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hair = hair

    def __str__(self):
        """Lannister str method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Lannister repr method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"
    
    @classmethod
    def create_lannister(first_name, is_alive=True):
        return self.__init__()

    def die(self):
        """Lannister die method"""
        self.is_alive = False
