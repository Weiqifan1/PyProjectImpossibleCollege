import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import library.processing.simpel_video_filter as simpel_video_filter
import library.translation_and_speech.translate as translate
import library.translation_and_speech.text_to_speech as text_to_speech
import library.translation_and_speech.audio as audio


def rens2(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.medianBlur(img, 3)
    # img = cv2.bilateralFilter(img,9,75,75)
    # cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # resize2 + DilEro2,2 + threshBinary+Otsu ==
    # resize 3 + kernel2,2DilEro == 2050+2250 + 800fejler
    # GaussianBlur(img, (5, 5), 0) klare 150 men ikke 350
    # resize 3 klare 150 men fejler 350 og 1000
    # resize 2 alene laeser alt undtagen 150 og 350
    return img

def capture_video(translation_language):
    cap = cv2.VideoCapture('data/movies/videoplayback.webm')

    file = open("data/output/subtitles/frames_and_subtitles.txt", "w+")
    file.write("")
    file.close()
    file = open("data/output/subtitles/frames_and_subtitles.txt", "a+", encoding="utf-8")  # "w")
    # note end
    count = 0  # count frames
    oldline = ""
    saved_strings = []
    saved_midY = []
    pure_midY = []
    pure_string = []
    midY_average = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ((count % 50 == 0) and (count > 50)):
            cv2.imshow('frame', frame)

            frame1 = frame.copy()
            frame2 = frame.copy()

            basic = simpel_video_filter.basic_color_mask(frame1, [[0, 0, 255], [255, 255, 255]])
            cont = simpel_video_filter.white_contours(basic)
            con1 = cont.copy()
            # secondIter = simpel_video_filter.big_contours(cont)#simpel_video_filter.non_contours_to_dark(cont, [[0,0,255],[255,255,255]])

            contCount = 0
            contours = simpel_video_filter.get_contour_list(con1)
            x = y = w = h = None
            list_of_texts = []
            list_of_ylevels = []  # y+(0.5*h) == midpoints of the y aksis
            for contour in contours:
                contCount = contCount+1
                x, y, w, h = cv2.boundingRect(contour)
                # if midY_average > 0:
                #    if (abs(midY_average-(y+0.5*h))) < 60:

                crop_img = frame2[y:y+h, x:x+w]

                img = rens2(crop_img)
                text = pytesseract.image_to_string(img, lang="dan")
                list_of_texts.append(text)
                list_of_ylevels.append(int(y+0.5*w))
            # list_of_texts = list(filter(None, list_of_texts))

            # print(count)
            # print(list_of_texts)

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
                f = open("data/output/subtitles/subtitle_from_movie.txt", "a+", encoding="utf-8")
                f.write(list_of_texts[0] + "\n")
                f.close()
                print(list_of_texts[0])
                readf = open('data/output/subtitles/subtitle_from_movie.txt', mode='r', encoding='utf-8')
                linesFromF = readf.readlines()
                print(linesFromF)
                readf.close()
                translate.run_translate(linesFromF[-1], translation_language)
# , 
                text_to_speech.run_translate(len(linesFromF), translation_language)
                audio.speak(len(linesFromF))


            if (count > 700):
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1  # count frame

    file.close()
    cap.release()
    cv2.destroyAllWindows()

