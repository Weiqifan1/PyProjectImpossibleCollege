import cv2
from PIL import Image

def white_contours(black_white_frame, count_frames):
    """ 
    puts contours around a picture with black/white contrast.
    Takes the small contours and enlarge the white areas.
     """
    mask = black_white_frame.copy()
    basic2 = black_white_frame.copy()

    # "127,255" might have to be changed if we choose a color other than white.
    # Returns more parameters _ means we dont want to use the first parameter that is returned.
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # imBasic = Image.fromarray(mask)
    # imBasic.save("data/output/frames/02white_contours_threshold/" +str(count_frames)+ "_white_contours_threshold" +".png") 

    # contours - list - Skrives ud i find subtitles.
    # imBasic = Image.fromarray(contours)
    # imBasic.save("data/output/frames/03white_contours_find_contours/" +str(count_frames)+ "_white_contours_find_contours" +".png") 

    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        x = x - 4 
        y = y - 4
        w = w + 8
        h = h + 8
        a = cv2.rectangle(basic2, (x, y), (x + w, y + h), (255, 255, 255), 1) # fill the rectangles with white
        #cv2.imshow("a", a)

        mid_left = (x, round(y + (h/2)))
        mid_right = (x + w, round(y + (h/2)))
        cv2.line(basic2, mid_left, mid_right, (255, 255, 255), h)
        #cv2.imshow("basic2", basic2)

    return basic2


def create_large_contoures(white_contours, count_frames):
    """ 
     Create a large contour around all the white area so we can se that it's a line.
     """
    mask = white_contours.copy()
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # imBasic = Image.fromarray(contours)
    # imBasic.save("data/output/frames/a/" +str(count_frames)+ "_white_contours_find_contours" +".png") 

    return contours 
