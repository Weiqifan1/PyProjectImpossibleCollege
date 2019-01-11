import numpy as np
import cv2
from PIL import Image

def basic_color_mask(image, color_range_hsv, count_frames):
    """ 
    Create contrast between white and what is not white in a picture.
     """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)

    return mask


def clean_image(image, count_frames):
    """ 
    Remove noise from a small part of the picture. In the lower part of the picture where the subtitle is.
     """

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # grey
    grey = Image.fromarray(img)
    grey.save("data/output/frames/05color_bgr2gray/" + str(count_frames) + "_grey_image" +".png")

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize - more pixels to work with.
    resize_image = Image.fromarray(img)
    resize_image.save("data/output/frames/06resize/" + str(count_frames) + "_resize_image" +".png")
    
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    dilate = Image.fromarray(img)
    dilate.save("data/output/frames/07dilate/" + str(count_frames) + "_dilate_image" +".png")
    
    img = cv2.erode(img, kernel, iterations=1)
    erode = Image.fromarray(img)
    erode.save("data/output/frames/08erode/" + str(count_frames) + "_erode_image" +".png")
    
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return img
