import numpy as np
from PIL import Image
import pytesseract
import cv2
import os


def my_function():
    print("Hello from a function")


def basic_color_mask(image, color_range_hsv):
    #image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return mask


def white_contours(image_path, color_range_hsv):
    image = cv2.imread(image_path)
    mask = basic_color_mask(image, color_range_hsv)
    # "127,255" might have to be changed
    ret, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        cv2.rectangle(image, (x-5, y-5), (x+w+10, y+h+10), (255, 255, 255), 2)
    return image


def non_contours_to_dark(image_path, color_range_hsv):
    #image = cv2.imread(image_path)
    image = white_contours(image_path, color_range_hsv)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color_range = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_color_range = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_color_range, upper_color_range)
    ###res = cv2.bitwise_and(image,image, mask= mask)
    # "127,255" might have to be changed
    ret, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    return mask


def text_image_black_white(image_path, color_range_hsv):
    image = cv2.imread(image_path)
    dark_mask = non_contours_to_dark(image_path, color_range_hsv)

    _, contours, _ = cv2.findContours(
        dark_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x = y = w = h = None
    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(image, contours, -1, 255, 3)
        # find the biggest area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(dark_mask, (x, y), (x+w, y+h), (100, 100, 100), 2)

    image2 = cv2.imread(image_path)
    crop_img = image2[y:y+h, x:x+w]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    return gray


def video(image_path, color_range_hsv):
    image = cv2.imread(image_path)
    dark_mask = non_contours_to_dark(image_path, color_range_hsv)

    _, contours, _ = cv2.findContours(
        dark_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x = y = w = h = None
    if len(contours) != 0:
        # draw in white the contours that were founded
        cv2.drawContours(image, contours, -1, 255, 3)
        # find the biggest area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(dark_mask, (x, y), (x+w, y+h), (100, 100, 100), 2)

    image2 = cv2.imread(image_path)
    crop_img = image2[y:y+h, x:x+w]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    return gray


def read_pic_save_text(black_white_text_pic, pic_path, txt_path):
    filename = pic_path.format(os.getpid())
    cv2.imwrite(filename, black_white_text_pic)
    text = pytesseract.image_to_string(Image.open(filename))
    print(text)   ################### debug
    os.remove(filename)

    file = open(txt_path, "w")
    file.write(text)
    file.close()
