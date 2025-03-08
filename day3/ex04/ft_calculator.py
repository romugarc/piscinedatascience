class calculator:
    """calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """calculator dotproduct method"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print("Dot product is:", result)
        return

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """calculator add_vector method"""
        print("Add Vector is:", [float(V1[i] + V2[i]) for i in range(len(V1))])
        return

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """calculator sous_vec method"""
        vlen = len(V1)
        print("Sous Vector is:", [float(V1[i] - V2[i]) for i in range(vlen)])
        return
