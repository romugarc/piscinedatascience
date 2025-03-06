from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    try:
        if array is None:
            raise ValueError("array should not be None")
        if len(array) == 0:
            raise ValueError("array is empty")
        if len(set(map(len, array))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")

        invert_img = np.copy(array)
        R = np.array(invert_img[:, :, 0])
        G = np.array(invert_img[:, :, 1])
        B = np.array(invert_img[:, :, 2])
        invert_img[:, :, 0] = 255 - R
        invert_img[:, :, 1] = 255 - G
        invert_img[:, :, 2] = 255 - B

        plt.imshow(invert_img)
        plt.show()
        return invert_img
    
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {str(e)}")
        return []

def ft_red(array) -> np.array:
    """Reds the color of the image received."""
    try:
        if array is None:
            raise ValueError("array should not be None")
        if len(array) == 0:
            raise ValueError("array is empty")
        if len(set(map(len, array))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")
        
        red_img = np.copy(array)
        R = np.array(red_img[:, :, 0])
        G = np.array(red_img[:, :, 1])
        B = np.array(red_img[:, :, 2])
        red_img[:, :, 0] = R
        red_img[:, :, 1] = G * 0
        red_img[:, :, 2] = B * 0

        plt.imshow(red_img)
        plt.show()
        return red_img
    
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {str(e)}")
        return []

def ft_green(array) -> np.array:
    """Greens the color of the image received."""
    
    try:
        if array is None:
            raise ValueError("array should not be None")
        if len(array) == 0:
            raise ValueError("array is empty")
        if len(set(map(len, array))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")

        green_img = np.copy(array)
        R = np.array(green_img[:, :, 0])
        G = np.array(green_img[:, :, 1])
        B = np.array(green_img[:, :, 2])
        green_img[:, :, 0] = R - R
        green_img[:, :, 1] = G
        green_img[:, :, 2] = B - B

        plt.imshow(green_img)
        plt.show()
        return green_img
    
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {str(e)}")
        return []

def ft_blue(array) -> np.array:
    """Blues the color of the image received."""
    try:
        if array is None:
            raise ValueError("array should not be None")
        if len(array) == 0:
            raise ValueError("array is empty")
        if len(set(map(len, array))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")
        
        blue_img = np.copy(array)
        R = np.array(blue_img[:, :, 0])
        G = np.array(blue_img[:, :, 1])
        B = np.array(blue_img[:, :, 2])
        blue_img[:, :, 0] = 0
        blue_img[:, :, 1] = 0
        blue_img[:, :, 2] = B

        plt.imshow(blue_img)
        plt.show()
        return blue_img
    
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {str(e)}")
        return []

def ft_grey(array) -> np.array:
    """Greys the color of the image received."""
    try:
        if array is None:
            raise ValueError("array should not be None")
        if len(array) == 0:
            raise ValueError("array is empty")
        if len(set(map(len, array))) not in (0, 1):
            raise ValueError("incorrect data in image")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image has too many channels, should be strictly RGB")
        
        grey_img = np.copy(array)
        grey_img = np.mean(grey_img, axis=2, dtype=int)

        plt.imshow(grey_img, cmap="gray")
        plt.show()
        return grey_img
    
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {str(e)}")
        return []