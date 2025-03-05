import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    This function loads an image
    and prints its format and its pixels content in RGB format
    """
    if type(path) is not str:
        raise ValueError("path is not a string")
    try:
        im = Image.open(path)
        img = np.array(im)
        print("The shape of image is :", img.shape)
        return img
    except FileNotFoundError as e:
        print(f"FileNotFoundError:{(str(e))}")
        return None
