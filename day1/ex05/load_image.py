import numpy as np
from PIL import Image
from PIL import UnidentifiedImageError


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
        if len(set(map(len, img))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if img.ndim != 3 or img.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")
        print("The shape of image is :", img.shape)
        print(img)
        return img
    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}:{(str(e))}")
        return []
    except (UnidentifiedImageError, TypeError) as e:
        print(f"{type(e).__name__}:{(str(e))}")
        return []