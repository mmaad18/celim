import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def load_image(path: str):
    return plt.imread(path)


def load_image_gray(path: str):
    image_array = plt.imread(path)
    return np.mean(image_array, axis=2)


def show_image_gray(image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


def save_image_gray(image, path: str):
    plt.imsave(path, image, cmap='gray')


def edge_detection_x(image):
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    return convolution2D(image, kernel)


def edge_detection_y(image):
    kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    return convolution2D(image, kernel)


def image_smoothing(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    return convolution2D(image, kernel)


def convolution2D(image, kernel):
    return signal.convolve2d(image, kernel, mode='valid')


def thresholding(image, threshold=(0.1, 0.2), new_value=1.0):
    image_height, image_width = image.shape
    output = np.zeros((image_height, image_width))

    for i in range(image_height):
        for j in range(image_width):
            if threshold[0] < image[i, j] < threshold[1]:
                output[i, j] = new_value

    return output
