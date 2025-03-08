class calculator:
    """calculator class"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        """calculator add method"""
        print([item + object if item else item for item in self.vector])
        return

    def __mul__(self, object) -> None:
        """calculator multiply method"""
        print([item * object if item else item for item in self.vector])
        return

    def __sub__(self, object) -> None:
        """calculator subtract method"""
        print([item - object if item else item for item in self.vector])
        return

    def __truediv__(self, object) -> None:
        """calculator true division method"""
        print([item / object if item > 0 else item for item in self.vector])
        return
