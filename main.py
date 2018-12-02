
import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter

image = cv2.imread("pic/pic2W.jpg")

#crop = get_still_filter.text_image_black_white("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
#chrsave = get_still_filter.read_pic_save_text(crop,"test_results/mypic.png" ,"test_results/mynew.txt")



#cv2.imshow("contour", crop)
cv2.imshow("image", image)

cv2.waitKey(0)

print("hello")