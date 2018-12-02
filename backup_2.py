
import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os

image = cv2.imread("pic/pic1WonB.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,255], dtype=np.uint8)
upper_white = np.array([255,255,255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_white, upper_white)
###res = cv2.bitwise_and(image,image, mask= mask)

ret, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

#paint contours green
_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print(contours)
for contour in contours:
    area = cv2.contourArea(contour)
    cv2.drawContours(image, contour, -1, (100, 255, 100), 3)


cv2.imshow('frame',image)
cv2.imshow('mask',mask)

###cv2.imshow('res',res)
cv2.waitKey(0)
filename = "chr.png".format(os.getpid())
cv2.imwrite(filename, mask)

'''
_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print(contours)
#contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 100 or rect[3] < 100: continue
    #print cv2.contourArea(c)
    x,y,w,h = rect
    cv2.rectangle(im,(x,y),(x+w,y+h),(100,255,100),2)
    cv2.putText(im,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))
cv2.imshow("Show",im)
cv2.waitKey()  
'''