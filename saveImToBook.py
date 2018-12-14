import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter
from library import simpel_video_filter as filt
import shutil
from library import translate
from library import text_to_speech
from library import speech_out
import trio


async def rens2_001(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
async def rens2_002(img):
    return cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
async def rens2_003(img, kernel):
    return cv2.dilate(img, kernel, iterations=1)
async def rens2_004(img, kernel):
    return cv2.erode(img, kernel, iterations=1)
async def rens2_005(img):
    return cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

async def rens2(image):
    img = await rens2_001(image)                                                    #cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = await rens2_002(img)                              #cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((2, 2), np.uint8)
    img = await rens2_003(img, kernel)                      #cv2.dilate(img, kernel, iterations=1)
    img = await rens2_004(img, kernel)                       #cv2.erode(img, kernel, iterations=1)
    img = await rens2_005(img)                                #cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img


async def consumer_001(frame1):
    basic = filt.basic_color_mask(frame1, [[0, 0, 255], [255, 255, 255]])
    return filt.white_contours(basic)        #con1 = filt.white_contours(basic)
async def consumer_002(con1):
    return filt.get_contour_list(con1)#contours = filt.get_contour_list(con1)
async def consumer_003(contour):
    x, y, w, h = cv2.boundingRect(contour)
    return x, y, w, h
async def consumer_004(frame2, x, y, w, h):
    return frame2[y:y+h, x:x+w]   #crop_img = frame2[y:y+h, x:x+w]
async def consumer_005(img):
    return pytesseract.image_to_string(img, lang="dan")#text = pytesseract.image_to_string(img, lang="dan")


async def consumer(receive_channel): #def speak_from_frame(frame):
    async with receive_channel:
        
        file = open("book/book.txt", "a+", encoding="utf-8")  # "w")
        # note end

        oldline = ""
        saved_strings = []
        saved_midY = []
        pure_midY = []
        pure_string = []
        midY_average = 0
        
        async for value in receive_channel: # value == [frame, count]
            frame = value[0]
            count = value[1]

            
            frame1 = frame.copy()
            frame2 = frame.copy()
                                        #basic = filt.basic_color_mask(frame1, [[0, 0, 255], [255, 255, 255]])
            con1 = await consumer_001(frame1)   #filt.white_contours(basic)
            contours = await consumer_002(con1)#filt.get_contour_list(con1)

            contCount = 0
            x = y = w = h = None
            list_of_texts = []
            list_of_ylevels = []  # y+(0.5*h) == midpoints of the y aksis
            for contour in contours:
                contCount = contCount+1
                x, y, w, h = await consumer_003(contour) #cv2.boundingRect(contour)

                crop_img = await consumer_004(frame2, x, y, w, h)  #crop_img = frame2[y:y+h, x:x+w]

                img = await rens2(crop_img)
                
                print("before: " + str(count))
                text = await consumer_005(img)   #text = pytesseract.image_to_string(img, lang="dan")
                print("after: " + str(count))
                
                list_of_texts.append(text)
                list_of_ylevels.append(int(y+0.5*w))
            #return list_of_texts, list_of_ylevels
            
            print("**************************************************************")
            if len(list_of_texts) > 0:
                longest_str_idx = max(list_of_texts, key=len)
                idx_of_longest = list_of_texts.index(longest_str_idx)
                longest_str = list_of_texts[idx_of_longest]
                saved_strings.append(longest_str)
                saved_midY.append(list_of_ylevels[idx_of_longest])

                line = longest_str+"\n"
                if line == oldline:
                    pass
                else:
                    oldline = line
                    file.write("frame: "+str(count)+"\n")
                    file.write(line)
                    print(str(count) + "   " + str(saved_midY[-1]))
                    # print(list_of_texts[0])
                    # print(list_of_ylevels)

                longest_str_idx = max(list_of_texts, key=len)
                if len(longest_str_idx) > 0:
                    idx_of_longest = list_of_texts.index(longest_str_idx)
                    pure_midY.append(list_of_ylevels[idx_of_longest])
                if len(pure_midY) > 0:
                    midY_average = sum(pure_midY) / float(len(pure_midY))
                    print("hero: " + str(pure_midY) + "    " + str(midY_average))
            
            

            if len(list_of_texts) > 0 and len(list_of_texts[0]) > 0:
                f = open("book/book3.txt", "a+", encoding="utf-8")
                f.write(list_of_texts[0] + "\n")
                f.close()
                print(list_of_texts[0])
                readf = open('book/book3.txt', mode='r', encoding='utf-8')
                linesFromF = readf.readlines()
                print(linesFromF)
                readf.close()
                translate.run_translate(linesFromF[-1])

                text_to_speech.run_translate(len(linesFromF))
                speech_out.speak(len(linesFromF))
        file.close()

def empty_folders_before_run():

    folder = 'book'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    folder = 'book2'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    folder = 'audio'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    file = open("book/book.txt", "w+")
    file.write("")
    file.close()
    f = open("book/book3.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()
    f = open("book/translated_subtitles.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()

async def producer(send_channel):
    async with send_channel:
        #for i in range(50):
        #    print(i)
        #    await send_channel.send(i)

        cap = cv2.VideoCapture('videoplayback.webm')

        
        count = 0  # count frames

        while(cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            await trio.sleep(0.02)
            if ((count % 50 == 0) and (count > 50)):
                #cv2.imshow('frame', frame)
                
                #print("before: " + str(count))
                ###############################################################################
                #######################   async funktion skal ind her:   #########################
                #list_of_texts, list_of_ylevels = speak_from_frame(frame)
                await send_channel.send([frame, count])
                ###############################################################################
                ###############################################################################
                #print("after: " + str(count))

                    # print(list_of_ylevels)

                    # lav foelgende beregning:
                    # tag gennemsnittet af de 3 sidste midY der har en string stoerre end 0
                    # hvis result ligger inden for +-60 pixels
                    # last_three_subs

                if (count > 700):
                    break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            count += 1  # count frame

        # note start
        #file.close()
        # note end
        cap.release()
        cv2.destroyAllWindows()


print("end")



async def main():
    empty_folders_before_run()
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(30)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)


trio.run(main)

# end
