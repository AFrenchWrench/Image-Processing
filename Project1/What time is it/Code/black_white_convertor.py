# coding: utf-8

import cv2
import numpy as np
import math
def black_white_convertor(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    background_pixel = np.argmax(hist)
    output = np.zeros_like(img, dtype=np.uint8)
    output[img == background_pixel] = 255
    return output
