from scipy import ndimage
from scipy.ndimage.filters import convolve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mp_img
import os
import cv2


class CannyEdgeDetector:
    def __init__(self, images, sigma=1.0, kernel_size=5, weak_pixel=75, strong_pixel=255, low_threshold=0.05,
                 high_threshold=0.15):
        self.images_in = images
        self.images_out = []
        self.img_smoothed = None
        self.gradient_matrix = None
        self.theta_matrix = None
        self.non_max_img = None
        self.threshold_img = None
        self.weak_pixel = weak_pixel
        self.strong_pixel = strong_pixel
        self.sigma = sigma
        self.kernel_size = kernel_size
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        return

    @staticmethod
    def gaussian_kernel(size, sigma=1.0):
        size = int(size) // 2
        x, y = np.mgrid[-size:size + 1, -size:size + 1]
        normal = 1 / (2.0 * np.pi * sigma ** 2)
        g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal
        return g

    @staticmethod
    def sobel_filters(img):
        kx = np.array([[-1, 0], [0, 1]], np.float32)
        ky = np.array([[0, -1], [1, 0]], np.float32)

        ix = ndimage.filters.convolve(img, kx)
        iy = ndimage.filters.convolve(img, ky)

        g = np.hypot(ix, iy)
        g = g / g.max() * 255
        theta = np.arctan2(iy, ix)
        return g, theta

    @staticmethod
    def roberts_filters(img):
        kx = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], np.float32)
        ky = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], np.float32)

        ix = ndimage.filters.convolve(img, kx)
        iy = ndimage.filters.convolve(img, ky)

        g = np.hypot(ix, iy)
        g = g / g.max() * 255
        theta = np.arctan2(iy, ix)
        return g, theta

    @staticmethod
    def previtt_filters(img):
        kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
        ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

        ix = ndimage.filters.convolve(img, kx)
        iy = ndimage.filters.convolve(img, ky)

        g = np.hypot(ix, iy)
        g = g / g.max() * 255
        theta = np.arctan2(iy, ix)
        return g, theta

    @staticmethod
    def non_max_suppression(img, d):
        m, n = img.shape
        z = np.zeros((m, n), dtype=np.int32)
        angle = d * 180. / np.pi
        angle[angle < 0] += 180

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                try:
                    q = 255
                    r = 255

                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                        q = img[i, j + 1]
                        r = img[i, j - 1]
                    # angle 45
                    elif 22.5 <= angle[i, j] < 67.5:
                        q = img[i + 1, j - 1]
                        r = img[i - 1, j + 1]
                    # angle 90
                    elif 67.5 <= angle[i, j] < 112.5:
                        q = img[i + 1, j]
                        r = img[i - 1, j]
                    # angle 135
                    elif 112.5 <= angle[i, j] < 157.5:
                        q = img[i - 1, j - 1]
                        r = img[i + 1, j + 1]

                    if (img[i, j] >= q) and (img[i, j] >= r):
                        z[i, j] = img[i, j]
                    else:
                        z[i, j] = 0

                except IndexError:
                    pass

        return z

    def threshold(self, img):
        high_threshold = img.max() * self.high_threshold
        low_threshold = high_threshold * self.low_threshold

        m, n = img.shape
        res = np.zeros((m, n), dtype=np.int32)

        weak = np.int32(self.weak_pixel)
        strong = np.int32(self.strong_pixel)

        strong_i, strong_j = np.where(img >= high_threshold)

        weak_i, weak_j = np.where((img <= high_threshold) & (img >= low_threshold))

        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak

        return res

    def hysteresis(self, img):
        m, n = img.shape
        weak = self.weak_pixel
        strong = self.strong_pixel

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if img[i, j] == weak:
                    try:
                        if ((img[i + 1, j - 1] == strong) or
                                (img[i + 1, j] == strong) or
                                (img[i + 1, j + 1] == strong) or
                                (img[i, j - 1] == strong) or
                                (img[i, j + 1] == strong) or
                                (img[i - 1, j - 1] == strong) or
                                (img[i - 1, j] == strong) or
                                (img[i - 1, j + 1] == strong)):
                            img[i, j] = strong
                        else:
                            img[i, j] = 0
                    except IndexError:
                        pass

        return img

    def detect(self):
        for i, img in enumerate(self.images_in):
            self.img_smoothed = convolve(img, self.gaussian_kernel(self.kernel_size, self.sigma))

            # self.gradient_matrix, self.theta_matrix = self.roberts_filters(self.img_smoothed)
            self.gradient_matrix, self.theta_matrix = self.previtt_filters(self.img_smoothed)
            # self.gradient_matrix, self.theta_matrix = self.sobel_filters(self.img_smoothed)


            self.non_max_img = self.non_max_suppression(self.gradient_matrix, self.theta_matrix)
            self.threshold_img = self.threshold(self.non_max_img)
            out = self.hysteresis(self.threshold_img)
            self.images_out.append(out)

        return self.images_out


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def load_data(dir_name):
    images = []
    for filename in os.listdir(dir_name):
        if os.path.isfile(dir_name + '/' + filename):
            img = mp_img.imread(dir_name + '/' + filename)
            img = rgb2gray(img)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            images.append(img)
    return images


def visualize(images, mode=None):
    for i, img in enumerate(images):
        if img.shape[0] == 3:
            img = img.transpose(1, 2, 0)
        plt_idx = i + 1
        plt.subplot(1, len(images), plt_idx)
        plt.imshow(img, mode)
    plt.show()


input_images = load_data('C:/Users/Pixel/Documents/python/FuzzyMath_7sem/lab4/input')
detector = CannyEdgeDetector(input_images, sigma=1, kernel_size=3, low_threshold=0.1, high_threshold=0.2, weak_pixel=100)
output_images = detector.detect()
visualize(input_images + output_images, 'gray')
