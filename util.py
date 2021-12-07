import cv2 as cv
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["image.cmap"] = "gray"


def plot_bgr(img):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    _ = plt.imshow(img_rgb)
    plt.show()


def plot_bw(img):
    _ = plt.imshow(img)
