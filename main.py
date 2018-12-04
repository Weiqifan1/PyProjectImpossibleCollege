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

cv2.waitKey(0)

cv2.imshow("image", image)

mage = cv2.imread("pic/pic2W.jpg")
basic = get_still_filter.basic_color_mask(image, [[0,0,255],[255,255,255]])
cv2.imshow("1. Find white", basic)

contour = get_still_filter.white_contours("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("2. Finder Kontour og udvider kontour", contour)

non = get_still_filter.non_contours_to_dark("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("3. Non Contours To Dark", non)

mytext = get_still_filter.text_image_black_white("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
cv2.imshow("The Last Process", mytext)

cv2.waitKey(0)
