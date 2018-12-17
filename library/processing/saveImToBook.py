import numpy as np
from PIL import Image
import pytesseract
import re
import cv2
import os
import library.processing.simpel_video_filter as simpel_video_filter
import library.translation_and_speech.translate as translate
import library.translation_and_speech.text_to_speech as text_to_speech
import library.translation_and_speech.audio as audio


def clean_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

def get_all_subtitles():
    readf = open('data/output/subtitles/subtitle_from_movie.txt', mode='r', encoding='utf-8')
    linesFromF = readf.readlines()
    readf.close()
    return linesFromF

def speak(linesFromF, translation_language):
    translate.run_translate(linesFromF[-1], translation_language)
    text_to_speech.run_translate(len(linesFromF), translation_language)
    audio.speak(len(linesFromF))

def get_text_from_frame(contours, original_frame):
    img = None
    contCount = 0
    x = y = w = h = None
    possible_subs = []
    for contour in contours:
        contCount = contCount+1
        x, y, w, h = cv2.boundingRect(contour)
        crop_img = original_frame[y:y+h, x:x+w]
        img = clean_image(crop_img)
        text = pytesseract.image_to_string(img, lang="dan")
        possible_subs.append(text)
    return possible_subs

def save_possible_subs(longest_str, count_frames):
    file = open("data/output/subtitles/frames_and_subtitles.txt", "a+", encoding="utf-8") 
    file.write("frame: "+str(count_frames)+"\n")
    file.write(longest_str+"\n")
    file.close()
    f = open("data/output/subtitles/subtitle_from_movie.txt", "a+", encoding="utf-8")
    f.write(longest_str+"\n")#list_of_texts[0] + "\n")
    f.close()

def get_longest_string(list_of_texts):
    try:
        longest_str_idx = max(list_of_texts, key=len)
        idx_of_longest = list_of_texts.index(longest_str_idx)
        longest_str = list_of_texts[idx_of_longest]
    except:
        longest_str = ""
    return longest_str

def search_for_white_texts(frame):
    test_frame = frame.copy()
    original_frame = frame.copy()
    basic = simpel_video_filter.basic_color_mask(test_frame, [[0, 0, 255], [255, 255, 255]])
    cont = simpel_video_filter.white_contours(basic)
    contours = simpel_video_filter.get_contour_list(cont)
    possible_subs = get_text_from_frame(contours, original_frame)
    return possible_subs

def handle_texts(longest_str, possible_subs, translation_language):
    all_subtitles = get_all_subtitles()
    speak(all_subtitles, translation_language)
  
def super_get_last_subtitle():
    all_subtitles = get_all_subtitles()
    if len(all_subtitles) > 0:
        return all_subtitles[-1]
    else:
        return ""

def different_alpha(subtitle_1, subtitle_2):
    new_sub_1 = re.sub('[^A-Za-z]+', ' ', subtitle_1).lstrip()
    new_sub_2 = re.sub('[^A-Za-z]+', ' ', subtitle_2).lstrip()
    return new_sub_1 != new_sub_2


def speak_from_frame(frame, count_frames, translation_language):
    possible_subs = search_for_white_texts(frame)
    longest_str = get_longest_string(possible_subs)
    longest_str = longest_str.replace('\n', ' ')
    last_subtitle = super_get_last_subtitle()
    if len(longest_str.strip()) > 0 and different_alpha(longest_str, last_subtitle):  #last_subtitle != longest_str: 
        print("dette virker!: " + str(longest_str) + " XXX " + str(last_subtitle))
        save_possible_subs(longest_str, count_frames)
        handle_texts(longest_str, possible_subs, translation_language)
    
    print("**************************************************************")
    print("frame number: "+str(count_frames))  

def capture_video(translation_language):
    print("press q to quit the program")
    cap = cv2.VideoCapture('data/movies/videoplayback.webm')
    count_frames = 0 

    while(cap.isOpened()):
        _, frame = cap.read()

        if (count_frames % 50 == 0):
            cv2.imshow('frame', frame)

            speak_from_frame(frame, count_frames, translation_language) #list_of_texts = 

            if (count_frames > 700):
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count_frames += 1 
    cap.release()
    cv2.destroyAllWindows()

