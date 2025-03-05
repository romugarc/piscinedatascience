import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    This function loads an image
    and prints its format and its pixels content in RGB format
    """
    try:
        if type(path) is not str:
            raise ValueError("path is not a string")
        im = Image.open(path)
        img = np.array(im)
        print("The shape of image is :", img.shape)
        return img
    except ValueError as e:
        print(f"ValueError:{(str(e))}")
        return []
    except FileNotFoundError as e:
        print(f"FileNotFoundError:{(str(e))}")
        return []
