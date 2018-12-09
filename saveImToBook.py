import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter
from library import simpel_video_filter as filt
import shutil

folder = 'book'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
folder = 'book2'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)


cap = cv2.VideoCapture('videoplayback.webm')

file = open("book/book.txt", "w+")
file.write("")
file.close()
file = open("book/book.txt", "a+", encoding="utf-8")#"w")
### note end
count = 0 #count frames
oldline = ""
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ((count%50 == 0) and (count > 200)):

        frame1 = frame.copy()
        frame2 = frame.copy()
        #try:
        basic = filt.basic_color_mask(frame1, [[0,0,255],[255,255,255]])
        cont = filt.white_contours(basic)
        con1 = cont.copy()
        secondIter = filt.big_contours(cont)#filt.non_contours_to_dark(cont, [[0,0,255],[255,255,255]])
        
        # secondIter fanger fint de store konturer. 
        # nu skal de tilsvarende omraader tages ud og laeses
        contCount = 0
        contours = filt.get_contour_list(con1)
        x = y = w = h = None
        list_of_texts = []
        for contour in contours:
            contCount = contCount+1
            x, y, w, h = cv2.boundingRect(contour)
            crop_img = frame2[y:y+h, x:x+w]

            chr = "book2/contour_"+str(count)+"_"+str(contCount)+".jpg"   #"pic/pic2W.jpg"
            chrfilename = chr.format(os.getpid())
            cv2.imwrite(chrfilename, crop_img)

            #gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            ##############################
            ### write the code to clean an image
            #blaaaa = get_still_filter.text_image_black_white(crop_img, [[0,0,255],[255,255,255]])
            #clean_blaaaa =  get_still_filter.cleaning_subs(crop_img)
            blaaa = get_still_filter.basic_color_mask(crop_img, [[0,0,255],[255,255,255]])
            blaaa2 =  cv2.threshold(blaaa, 0, 255, cv2.THRESH_OTSU)[1]
            text = pytesseract.image_to_string(blaaa, lang="dan")
            ##################################
            #text = pytesseract.image_to_string(gray)
            list_of_texts.append(text)
        print(count)
        print(list_of_texts)
        

        '''
        try:
            cont = get_still_filter.text_image_black_white(frame2, [[0,0,255],[255,255,255]])
            clean_cont =  get_still_filter.cleaning_subs(cont)
            text = pytesseract.image_to_string(cont, lang="dan")
            print(count)
            print(text)
        except:
            pass
        '''
        #hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        #lower_color_range = np.array([0,0,255], dtype=np.uint8)
        #upper_color_range = np.array([255,255,255], dtype=np.uint8)
        #mask = cv2.inRange(hsv, lower_color_range, upper_color_range)
        #_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        


            #cv2.imshow("secondIter", secondIter)
            
            # her er den gamle billedbehandling
            #cont = get_still_filter.text_image_black_white(frame, [[0,0,255],[255,255,255]])
            #clean_cont =  get_still_filter.cleaning_subs(cont)
            #text = pytesseract.image_to_string(cont, lang="dan")

        '''
        line = text+"\n"
        if line == oldline:
            pass
        else:
            oldline = line
            file.write("frame: "+str(count)+"\n")
            file.write(line)
            print("frame: "+str(count))
            print(text)
        '''
        #except:
        #    pass    
        
        pic_path = "book/frame_"+str(count)+".jpg"   #"pic/pic2W.jpg"
        filename = pic_path.format(os.getpid())
        cv2.imwrite(filename, frame)
        '''
        pic_path = "book/frame_"+str(count)+"_basic.jpg"   #"pic/pic2W.jpg"
        filename = pic_path.format(os.getpid())
        cv2.imwrite(filename, basic)
        '''
        pic_path = "book/frame_"+str(count)+"_cont.jpg"   #"pic/pic2W.jpg"
        filename = pic_path.format(os.getpid())
        cv2.imwrite(filename, cont)
        
        pic_path = "book/frame_"+str(count)+"_secondIter.jpg"   #"pic/pic2W.jpg"
        filename = pic_path.format(os.getpid())
        cv2.imwrite(filename, secondIter)
        
        #pic_path = "book/frame_"+str(count)+"_mask.jpg"   #"pic/pic2W.jpg"
        #filename = pic_path.format(os.getpid())
        #cv2.imwrite(filename, mask)

        if (count > 900):
            break


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1 #count frame

### note start      
file.close()
### note end
cap.release()
cv2.destroyAllWindows()


print("end")





######################################
# Chr's foerste videokode
#########################################
'''
#cap = cv2.VideoCapture('pic/girl.webm')
cap = cv2.VideoCapture('videoplayback.webm')
### note start 

file = open("film.txt", "w")
file.write("")
file.close()
file = open("film.txt", "a+", encoding="utf-8")#"w")
### note end
count = 0 #count frames
oldline = ""
while(cap.isOpened()):
    ret, frame = cap.read()

    ######
    #time = cv2.VideoCapture.get(CV_CAP_PROP_POS_AVI_RATIO)
    #print(time)
    #print("\n")
    if (count%50 == 0):
        try:
            cont = get_still_filter.text_image_black_white(frame, [[0,0,255],[255,255,255]])
            clean_cont =  get_still_filter.cleaning_subs(cont)
            text = pytesseract.image_to_string(clean_cont, lang="dan")
            line = text+"\n"
            if line == oldline:
                pass
            else:
                oldline = line
                file.write(line)
                print(text)
        except:
            pass    
    
    #except expression as identifier:
    #    pass
    #######

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1 #count frame

### note start      
file.close()
### note end
cap.release()
cv2.destroyAllWindows()
'''

######################################
# Chr's stillebillede kode
#########################################
'''
"pic1WonB.png"
"pic2W.jpg"
image = cv2.imread("pic/pic2W.jpg")
cont = get_still_filter.text_image_black_white(image, [[0,0,255],[255,255,255]])
clean_cont =  get_still_filter.cleaning_subs(cont)
text = pytesseract.image_to_string(clean_cont)
print(text)  #debugging
file = open("test_results/mynew.txt", "w")
file.write(text)
file.close()
#get_still_filter.read_pic_save_text(clean_cont, "test_results/binary.png" ,"test_results/mynew.txt")

cv2.imshow("image", image)
cv2.imshow("cont", cont)
cv2.imshow("clean_cont", clean_cont)

cv2.waitKey(0)
'''


######################################
# Bo's video kode:
#########################################
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