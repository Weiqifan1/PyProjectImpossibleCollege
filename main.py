import numpy as np
import cv2 

# download movie from youtube. Just give it the path.
# https://video.genyoutube.net/86d7jx2YB0Y

cap = cv2.VideoCapture('videoplayback.webm')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(nmixtures = 55, backgroundRatio = 0.005, noiseSigma = 9)

while(1):
    kernel = np.ones((1, 1), np.uint8)
    kernel_closing = np.ones((2, 2), np.uint8)

    ret, frame = cap.read()
    cropped = frame[283:600, 100:600]

    fgmask = fgbg.apply(cropped)
    

    #erosion = cv2.morphologyEx(fgmask, cv2.MORPH_ERODE, kernel)
    # closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel_closing)
    #erosion = cv2.morphologyEx(closing, cv2.MORPH_ERODE, kernel)

    #thresh = cv2.threshold(erosion, 140, 255, cv2.THRESH_BINARY)[1] 

    #dilate = cv2.dilate(fgmask, None, iterations=1)
    closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

    dilation = cv2.dilate(fgmask, kernel, iterations=1)
    closing_stepwise = cv2.erode(dilation, kernel, iterations=1)
    assert np.array_equal(closing, closing_stepwise)

    # show the frame
    #cv2.imshow('cropped', cropped)
    cv2.imshow('fgmask', fgmask)
    cv2.imshow('closing_stepwise', closing_stepwise)
    cv2.imshow('closing', closing)
    cv2.imshow('end', closing_stepwise)
    #cv2.imshow('threshold', thresh) # Ikke rigtig nogen forskel.
    #cv2.imshow('dilate', dilate) # Hele teksten bliver hvid, og bogstaverne går over i hinanden.
    

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows() 

def process_frame(fgmask):
    # compute the absolute difference between the current frame and
    # first frame
    #frame_delta = cv.absdiff(fgmask, gray) * 1 #amp
    thresh = cv2.threshold(fgmask, 40, 255, cv.THRESH_BINARY)[1]
 
    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)

    return thresh #, frame_delta

    