
import numpy as np
from PIL import Image
import pytesseract
import cv2
import os

'''
denne fil er til omskrivning af get_still_filter
til brug for 
saveImToBook.py (arbejde med en simpel video hvor 
underteksterne altdi er p[ samme sted og altid er hvide paa sort baggrund])
'''

def basic_color_mask(image, color_range_hsv):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return mask

def white_contours(basic_color_mask):
    mask = basic_color_mask.copy()
    # "127,255" might have to be changed if we choose a color other than white
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        cv2.rectangle(basic_color_mask, (x-5, y-5), (x+w+10, y+h+10), (255, 255, 255), 2)
    return basic_color_mask

def non_contours_to_dark(white_contours, color_range_hsv):
    #image = white_contours(image, color_range_hsv)
    image = white_contours
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color_range = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_color_range = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(image, lower_color_range, upper_color_range)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    return mask




#end