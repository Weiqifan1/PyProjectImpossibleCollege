
import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter

image = cv2.imread("pic/pic2W.jpg")

crop = get_still_filter.text_image_black_white("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
chrsave = get_still_filter.read_pic_save_text(crop,"test_results/mypic.png" ,"test_results/mynew.txt")

print("hey")

cv2.imshow("crop", crop)
cv2.imshow("image", image)

cv2.waitKey(0)

mage = cv2.imread("pic/pic2W.jpg")
basic = get_still_filter.basic_color_mask(image, [[0,0,255],[255,255,255]])
cv2.imshow("basic", basic)

cont = get_still_filter.white_contours("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("cont", cont)

non = get_still_filter.non_contours_to_dark("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("non", non)

mytext = get_still_filter.text_image_black_white("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("mytext", mytext)

cv2.waitKey(0)
