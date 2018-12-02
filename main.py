
import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os

#image = cv2.imread("pic/pic1WonB.png")
image = cv2.imread("pic/pic2W.jpg")

imagecopy1 = image.copy()
imagecopy2 = image.copy()

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
    rect = cv2.boundingRect(contour)
    x,y,w,h = rect
    cv2.rectangle(image,(x-5,y-5),(x+w+10,y+h+10),(255,255,255),2)
    #area = cv2.contourArea(contour)
    #cv2.drawContours(image, contour, -1, (100, 255, 100), 3)

#cv2.imshow('frame',imagecopy)
#cv2.imshow('mask',image)  #imagecopy er nu en hvid plamage
#cv2.waitKey(0)
#filename = "chr.png".format(os.getpid())
#cv2.imwrite(filename, mask)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,255], dtype=np.uint8)
upper_white = np.array([255,255,255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_white, upper_white)
###res = cv2.bitwise_and(image,image, mask= mask)
ret, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)


# tegner en groen boks omkring alle fundne conturer. 
# nu skal den bare kun goere det for den stoerste kontur
_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#for contour in contours:
#    rect = cv2.boundingRect(contour)
#    x,y,w,h = rect
#    cv2.rectangle(image,(x,y),(x+w,y+h),(100,255,100),2)

x = y = w = h = None
if len(contours) != 0:
    # draw in blue the contours that were founded
    cv2.drawContours(image, contours, -1, 255, 3)
    #find the biggest area
    c = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(image,(x,y),(x+w,y+h),(100,100,100),2)

# the coordinates x,y,w,h now have the info for the wanted area
# crop an image>
#import cv2
#img = cv2.imread("lenna.png")
#crop_img = img[y:y+h, x:x+w]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)

crop_img = imagecopy1[y:y+h, x:x+w]
gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
#gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU)[1]

#pytesseract delen
filename = "test_results/tess.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))

#os.remove(filename)
print(text)
file = open("test_results/textfile.txt","w") 
file.write(text) 
file.close() 

cv2.imshow('imagecopy1',imagecopy1)
cv2.imshow('cropped image',gray)

#cv2.imshow('mask',mask) 
cv2.waitKey(0)
filename = "test_results/chr.png".format(os.getpid())
cv2.imwrite(filename, mask)









print("hello")


