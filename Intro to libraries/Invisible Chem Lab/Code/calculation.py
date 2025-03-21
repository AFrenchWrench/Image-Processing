# coding: utf-8

import cv2
import numpy as np
def calculation(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_pixels = np.count_nonzero(mask)
    total_tube_area = 3 * 60 * 200
    average_filled_percentage = (blue_pixels / total_tube_area) * 100
    return int(average_filled_percentage)
