
import numpy as np
from PIL import Image
import pytesseract
import cv2
import os

def basic_color_mask(image, color_range_hsv):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return mask

def white_contours(basic_color_mask):
    mask = basic_color_mask.copy()
    basic2 = basic_color_mask.copy()
    # "127,255" might have to be changed if we choose a color other than white
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        x = x - 4 
        y = y - 4
        w = w + 8
        h = h + 8
        cv2.rectangle(basic2, (x, y), (x+w, y+h), (255, 255, 255), 1) # fill the rectangles with white
        mid_left = (x, round(y+(h/2)))
        mid_right = (x+w, round(y+(h/2)))
        cv2.line(basic2, mid_left, mid_right, (255, 255, 255), h)
    return basic2

def big_contours(white_contours):
    mask = white_contours.copy()
    basic2 = white_contours.copy()
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        cv2.rectangle(basic2, (x-1, y-1), (x+w+2, y+h+2), (100, 100, 100), 2)
    return basic2

def get_contour_list(white_contours):
    mask = white_contours.copy()
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return contours

