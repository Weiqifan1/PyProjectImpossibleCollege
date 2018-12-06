import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter

"pic1WonB.png"
"pic2W.jpg"

image = cv2.imread("pic/pic2W.jpg")
image2 = image.copy()

#####crop = get_still_filter.text_image_black_white("pic/pic2W.jpg", [[0,0,255],[255,255,255]])
######chrsave = get_still_filter.read_pic_save_text(crop,"test_results/mypic.png" ,"test_results/mynew.txt")
#######cont = get_still_filter.white_contours("pic/pic2W.jpg", [[0,0,255],[255,255,255]])

#cont = get_still_filter.text_image_black_white(image, [[0,0,255],[255,255,255]])
#coor_image = get_still_filter.find_subtitle_coordinates(image2, [[0,0,255],[255,255,255]])

#######_, cont = cv2.threshold(cont, 127, 255, cv2.THRESH_BINARY)
########cont = mask

#clean_cont =  cv2.threshold(cont, 0, 255, cv2.THRESH_OTSU)[1]      #get_still_filter.otsu_cleaning(cont)
#get_still_filter.read_pic_save_text(clean_cont, "test_results/binary.png" ,"test_results/mynew.txt")

#########################
#skriv her nogle maader at rense billedet:
#https://www.tutorialspoint.com/dip/optical_character_recognition.htm
#cv2.imshow("cont", cont)

cv2.imshow("grey", cv2.imread("test_results/grey.png"))
#newotsu = cv2.threshold(cv2.imread("test_results/grey.png"), 0, 255, cv2.THRESH_OTSU)[1]
#print(pytesseract.image_to_string(newotsu)

#########################

#cv2.imshow("cont", cont)
#cv2.imshow("sub", coor_image)

cv2.waitKey(0)

print("hello")

'''
import numpy as np
import cv2
# import pytesseract # pip install pytesseract

# opencv and tesser ocr
# https://docs.opencv.org/3.0-beta/modules/text/doc/ocr.html

# download movie from youtube. Just give it the path.
# https://video.genyoutube.net/86d7jx2YB0Y

cap = cv2.VideoCapture('pic/girl.webm')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(
    nmixtures=55, backgroundRatio=0.005, noiseSigma=9)

while(1):
    kernel = np.ones((1, 1), np.uint8)
    kernel_closing = np.ones((2, 2), np.uint8)

    ret, frame = cap.read()

    cropped = frame[283:600, 100:600]

    #fgmask = fgbg.apply(cropped)
    
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    
    cv2.imshow('gray', gray)

    get_still_filter.read_pic_save_text(
        gray, "test_results/mypic.png", "test_results/mynew.txt")

    #erosion = cv2.morphologyEx(fgmask, cv2.MORPH_ERODE, kernel)
    # closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel_closing)
    #erosion = cv2.morphologyEx(closing, cv2.MORPH_ERODE, kernel)

    #thresh = cv2.threshold(erosion, 140, 255, cv2.THRESH_BINARY)[1]

    #dilate = cv2.dilate(fgmask, None, iterations=1)
    #closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

    #dilation = cv2.dilate(fgmask, kernel, iterations=1)
    #closing_stepwise = cv2.erode(dilation, kernel, iterations=1)
    #assert np.array_equal(closing, closing_stepwise)

    # show the frame
    #cv2.imshow('cropped', cropped)
    """ cv2.imshow('fgmask', fgmask)
    cv2.imshow('closing_stepwise', closing_stepwise)
    cv2.imshow('closing', closing)
    cv2.imshow('end', closing_stepwise) """
    # cv2.imshow('threshold', thresh) # Ikke rigtig nogen forskel.
    # cv2.imshow('dilate', dilate) # Hele teksten bliver hvid, og bogstaverne går over i hinanden.
    # print(pytesseract.image_to_string(fgmask))

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


def process_frame(fgmask):
    # compute the absolute difference between the current frame and
    # first frame
    # frame_delta = cv.absdiff(fgmask, gray) * 1 #amp
    thresh = cv2.threshold(fgmask, 40, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)

    return thresh  # , frame_delta
'''


#end