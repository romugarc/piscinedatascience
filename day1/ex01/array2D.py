import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based
    on the provided start and end arguments.
    """
    try:
        if type(family) is not list or \
                any(type(item) is not list for item in family):
            raise ValueError("2D array is None or some lists are None")
        if len(set(map(len, family))) not in (0, 1):
            raise ValueError("not all lists have the same length")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("start and/or end aren't ints")
        npfamily = np.array(family)
        newlist = npfamily[start:end]
        print("My shape is :", npfamily.shape)
        print("My new shape is :", newlist.shape)
        return newlist
    except ValueError as e:
        print(f"ValueError: {(str(e))}")
        return []
