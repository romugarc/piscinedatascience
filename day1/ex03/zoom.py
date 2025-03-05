from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
    try:
        img = ft_load("animal.jpeg")
    except ValueError as e:
        print(f"Error:{(str(e))}")
        return
    
    zoomed_img = img[100:500, 420:820]
    zoomed_img = np.mean(zoomed_img, axis=2)
    print("New shape after slicing :", zoomed_img.shape)

    plt.imshow(zoomed_img)
    plt.show()
    return

if __name__ == "__main__":
    main()