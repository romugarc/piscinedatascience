class calculator:
    """calculator class"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        """calculator add method"""
        self.vector = [item + object for item in self.vector]
        print(self.vector)
        return

    def __mul__(self, object) -> None:
        """calculator multiply method"""
        self.vector = [item * object for item in self.vector]
        print(self.vector)
        return

    def __sub__(self, object) -> None:
        """calculator subtract method"""
        self.vector = [item - object for item in self.vector]
        print(self.vector)
        return

    def __truediv__(self, object) -> None:
        """calculator true division method"""
        if object == 0:
            return
        self.vector = [item / object for item in self.vector]
        print(self.vector)
        return
