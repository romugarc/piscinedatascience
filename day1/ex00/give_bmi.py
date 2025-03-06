def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """
    This function takes 2 lists of integers or floats input and
    returns a list of BMI values
"""
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight are not the same size")
        if not all(isinstance(item, (int, float)) for item in height) or \
                not all(isinstance(item, (int, float)) for item in weight):
            raise ValueError("height and weight should be only ints or floats")
        if any(item == 0 for item in height):
            raise ValueError("parameters in height can't be 0")
        newlist = list(map(lambda h, w: w/(h**2), height, weight))
        return newlist
    except ValueError as e:
        print(f"ValueError: {(str(e))}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function accepts a list of integers or floats and an integer
    representing a limit as parameters. It returns a list of booleans.
    (True if above the limit)
"""
    try:
        if not isinstance(limit, int):
            raise ValueError("limit is not an int")
        if not all(isinstance(item, (int, float)) for item in bmi):
            raise ValueError("bmi is not only comprised of ints or floats")
        newlist = [True if x > limit else False for x in bmi]
        return newlist
    except ValueError as e:
        print(f"ValueError: {(str(e))}")
        return []
