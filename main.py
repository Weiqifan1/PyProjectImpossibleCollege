import numpy as np
import cv2 as cv

# download movie from youtube. Just give it the path.
# https://video.genyoutube.net/86d7jx2YB0Y

cap = cv.VideoCapture('videoplayback.webm')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG(nmixtures = 55, backgroundRatio = 0.005, noiseSigma = 9)
# nmixtures = 5 # Det virker ikke til at den giver noget.
# backgroundRatio = 0.005 # Jo lavere jo bedre.
# noiseSigma = 0 # omkring 7-10.

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame', fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
        
cap.release()
cv.destroyAllWindows() 

