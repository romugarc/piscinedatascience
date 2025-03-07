from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class that inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

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
    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self):
        """Lannister str method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Lannister repr method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Lannister create_lannister method"""
        return Lannister(first_name, is_alive)

    def die(self):
        """Lannister die method"""
        self.is_alive = False
