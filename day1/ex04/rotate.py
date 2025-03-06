from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
    """
    This program 
    """
    try:
        img = ft_load("animal.jpeg")
    except ValueError as e:
        print(f"Error:{(str(e))}")
        return
    if len(img) == 0:
        return
    
    if img.shape[0] < 400 or img.shape[1] < 400:
        print("Error: image size too small, must be at least 400x400")
    
    height, width = img.shape[:2]
    start_top = (height // 2) - 200
    start_left = (width // 2) - 200
    end_top = start_top + 400
    end_left = start_left + 400
    
    zoomed_img = img[start_top:end_top, start_left:end_left]
    zoomed_img = np.mean(zoomed_img, axis=2, dtype=int)
    print("The shape of image is: ", zoomed_img.shape)
    print(zoomed_img[:,:,np.newaxis])
    
    rotated_img = np.array([[zoomed_img[j][i] for j in range(zoomed_img.shape[0])] for i in range(zoomed_img.shape[1])])
    print("New shape after Transpose:", rotated_img.shape)
    print(rotated_img)
    plt.imshow(rotated_img, cmap="gray")
    plt.show()
    return

if __name__ == "__main__":
    main()