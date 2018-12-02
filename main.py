
#import sys
#print(sys.version_info)

#import numpy as np
#import matplotlib.pyplot as plt
#import cv2

import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os

#image = cv2.imread("pic/pic1WonB.png")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow('img', image)
#cv2.waitKey(0)

#track white and write to folder

image = cv2.imread("pic/pic1WonB.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#lower_white = np.array([255,0,0], dtype=np.uint8)
#upper_white = np.array([255,255,255], dtype=np.uint8)

lower_white = np.array([0,0,255], dtype=np.uint8)
upper_white = np.array([255,255,255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_white, upper_white)
###res = cv2.bitwise_and(image,image, mask= mask)

ret, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

cv2.imshow('frame',image)
cv2.imshow('mask',mask)
###cv2.imshow('res',res)
cv2.waitKey(0)
filename = "chr.png".format(os.getpid())
cv2.imwrite(filename, mask)
# threshold
#image = cv2.imread("pic/pic1WonB.png")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#ret, chr = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#cv2.imshow('img', chr)
#cv2.waitKey(0)



#text = pytesseract.image_to_string(Image.open("onlytext.png"))
#print(text)


# replace range
#mask[np.where((mask == [0]).all(axis = 1))] = [255]
#http://answers.opencv.org/question/97416/replace-a-range-of-colors-with-a-specific-color-in-python/



# threshold
#image = cv2.imread("pic/pic1WonB.png")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#ret, chr = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#cv2.imshow('img', chr)
#cv2.waitKey(0)


print("hello")


