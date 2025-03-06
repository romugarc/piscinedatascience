from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """This program loads an image, prints some information about it,
and displays it after zooming"""
    try:
        img = ft_load("animal.jpeg")
    except ValueError as e:
        print(f"Error:{(str(e))}")
        return
    if len(img) == 0:
        return

    if img.shape[0] < 400 or img.shape[1] < 400:
        print("Error: image size too small, must be at least 400x400")
    print(img)

    height, width = img.shape[:2]
    start_top = (height // 2) - 200
    start_left = (width // 2) - 200
    end_top = start_top + 400
    end_left = start_left + 400

    zoomed_img = img[start_top:end_top, start_left:end_left]
    zoomed_img = np.mean(zoomed_img, axis=2, dtype=int)
    print("New shape after slicing :", zoomed_img.shape)
    print(zoomed_img[:, :, np.newaxis])

    plt.imshow(zoomed_img, cmap="gray")
    plt.show()
    return


if __name__ == "__main__":
    main()
