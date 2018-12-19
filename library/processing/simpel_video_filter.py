import numpy as np
import cv2


def basic_color_mask(image, color_range_hsv):
    """ 
    Create contrast between white and what is not white in a picture.
     """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)

    return mask


def clean_image(image):
    """ 
    Remove noise from a small part of the picture. In the lower part of the picture where the subtitle is.
     """
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # grey
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize - more pixels to work with.
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return img
