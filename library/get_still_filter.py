import numpy as np
from PIL import Image
import pytesseract
import cv2
import os

# functions to get the subtitles in a txt file

def read_image(image_path):
    return cv2.imread(image_path)

def basic_color_mask(image, color_range_hsv):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return mask

def white_contours(image, color_range_hsv):
    mask = basic_color_mask(image, color_range_hsv)
    # "127,255" might have to be changed if we choose a color other than white
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        cv2.rectangle(image, (x-5, y-5), (x+w+10, y+h+10), (255, 255, 255), 2)
    return image

def non_contours_to_dark(image, color_range_hsv):
    image = white_contours(image, color_range_hsv)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color_range = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_color_range = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_color_range, upper_color_range)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    return mask

def text_image_black_white(image, color_range_hsv):
    image2 = image.copy()

    dark_mask = non_contours_to_dark(image, color_range_hsv)
    _, contours, _ = cv2.findContours(dark_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x = y = w = h = None
    cv2.drawContours(image, contours, -1, 255, 3) # draw in white the contours that were founded
    c = max(contours, key=cv2.contourArea)        # find the biggest area
    x, y, w, h = cv2.boundingRect(c)
    #cv2.rectangle(dark_mask, (x, y), (x+w, y+h), (100, 100, 100), 2) # draw the contour

    crop_img = image2[y:y+h, x:x+w]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    return gray

def cleaning_subs(black_white_subtitle):
    clean_cont =  cv2.threshold(black_white_subtitle, 0, 255, cv2.THRESH_OTSU)[1]
    kernel = np.ones((2,2), np.uint8)
    opening = cv2.morphologyEx(clean_cont, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing

def read_pic_save_text(black_white_clean, pic_path, txt_path):
    filename = pic_path.format(os.getpid())
    cv2.imwrite(filename, black_white_clean)
    text = pytesseract.image_to_string(Image.open(filename))
    print(text)  #debugging
    file = open(txt_path, "w")
    file.write(text)
    file.close()

# functions to see the subtitles in a raw (unedited) sub image:

def find_subtitle_coordinates(image, color_range_hsv):
    image2 = image.copy()

    dark_mask = non_contours_to_dark(image, color_range_hsv)
    _, contours, _ = cv2.findContours(dark_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x = y = w = h = None
    cv2.drawContours(image, contours, -1, 255, 3) # draw in white the contours that were founded
    c = max(contours, key=cv2.contourArea)        # find the biggest area
    x, y, w, h = cv2.boundingRect(c)
    #cv2.rectangle(dark_mask, (x, y), (x+w, y+h), (100, 100, 100), 2) # draw the contour

    crop_img = image2[y:y+h, x:x+w]
    #gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    return crop_img#gray







#end