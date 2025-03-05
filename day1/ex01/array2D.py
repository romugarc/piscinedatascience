import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided start and end arguments.
    """
    if type(family) is not list or any(type(item) is not list for item in family):
        raise ValueError("2D array is None or some lists are None")
    if len(set(map(len, family))) not in (0, 1):
        raise ValueError("not all lists have the same length")
    newlist = family[start:end]
    print("My shape is :", len(family), len(family[0]))
    print("My new shape is :", len(newlist), len(newlist[0]))
    return newlist