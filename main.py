import numpy as np
from PIL import Image
import pytesseract 
import argparse
import cv2
import os
from library import get_still_filter

# download movie from youtube. Just give it the path.
# https://video.genyoutube.net/86d7jx2YB0Y

cap = cv2.VideoCapture('videoplayback.webm')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(
    nmixtures=55, backgroundRatio=0.005, noiseSigma=9)

while(1):
    kernel = np.ones((1, 1), np.uint8)
    kernel_closing = np.ones((2, 2), np.uint8)

    ret, frame = cap.read()

    #cropped = frame[283:600, 100:600]

    # fgmask = fgbg.apply(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    
    # cv2.imshow('original', fgmask)
    cv2.imshow('gray', gray)
    # cv2.imshow('fgmask', fgmask)

    get_still_filter.read_pic_save_text(
       gray, "test_results/mypic.png", "test_results/mynew.txt")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
