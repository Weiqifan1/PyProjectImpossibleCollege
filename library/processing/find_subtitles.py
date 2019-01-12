import pytesseract
from pathlib import Path
import re
import cv2
import library.processing.simpel_video_filter as simpel_video_filter
import library.processing.create_contours as create_contours
from PIL import Image

def get_all_subtitles():
    with open(Path('data/output/subtitles/subtitle_from_movie.txt'), mode='r', encoding='utf-8') as file:
        lines_from_subtitle_file_list = file.readlines()
        return lines_from_subtitle_file_list


def get_text_from_frame(contours, original_frame, count_frames):
    """ 
    Takes contour and the origina frame and remove noise and then calls tesseract.
    Return a list with strings, that can be subtitles or error readings.
     """
    img = None
    contCount = 0
    x = y = w = h = None
    possible_subs = []
    
    for contour in contours:
        contCount = contCount+1
        x, y, w, h = cv2.boundingRect(contour)
        crop_img = original_frame[y:y + h, x:x + w]

        
        imBigCont = Image.fromarray(crop_img)
        imBigCont.save("data/output/frames/04crop_image/" +str(count_frames)+ "_00" + str(contCount)+ "_crop_image" +".png") # create_contours.white_contours linje 20


        img = simpel_video_filter.clean_image(crop_img, count_frames)

        img_clean = Image.fromarray(img)
        img_clean.save("data/output/frames/09clean_img_after_threshold/" + str(count_frames)+ "_clean_image_after_threshold" +".png") # create_contours.white_contours linje 20


        text = pytesseract.image_to_string(img, lang="dan")
        possible_subs.append(text)
    
    return possible_subs


def save_subtitles(longest_str, count_frames):
    """ 
    Saves subtitles.
     """
    with open(Path("data/output/subtitles/frames_and_subtitles.txt"), "a+", encoding="utf-8") as file:
        file.write("frame: " + str(count_frames) + "\n")
        file.write(longest_str + "\n")


    with open(Path("data/output/subtitles/subtitle_from_movie.txt"), "a+", encoding="utf-8") as file:
        file.write(longest_str + "\n") 
    

def get_longest_string(list_of_texts):
    try:
        longest_str_idx = max(list_of_texts, key=len)
        idx_of_longest = list_of_texts.index(longest_str_idx)
        longest_str = list_of_texts[idx_of_longest]
    except:
        longest_str = ""

    return longest_str


def search_for_white_texts(frame, count_frames):
    """ 
    Searching for a text and reads the text.
     """
    test_frame = frame.copy()
    original_frame = frame.copy() 

    basic = simpel_video_filter.basic_color_mask(test_frame, [[0, 0, 255], [255, 255, 255]], count_frames)
    imBasic = Image.fromarray(basic)
    imBasic.save("data/output/frames/01c_basic_color_mask_after_inRange/" + str(count_frames)+ "basic_color_mask_after_inRange" +".png") # simpel_video_filter.basic_color_mask linje 13

    cont = create_contours.white_contours(basic, count_frames)

    imCont = Image.fromarray(cont)
    imCont.save("data/output/frames/03white_contours_find_contours/" + str(count_frames)+ "find_contours" +".png") # create_contours.white_contours linje 20

    contours = create_contours.create_large_contoures(cont, count_frames) # if there is a text create a contour arounf it.
    #print(type(contours))
    #img_large_contours = Image(contours)
    #img_large_contours.save("data/output/frames/03white_large_contours" + str(count_frames)+ "white_contours" +".png")
    #cv2.imwrite("data/output/frames/03white_large_contours/" + str(count_frames)+ "white_contours" +".png", img_large_contours)

    possible_subs = get_text_from_frame(contours, original_frame, count_frames) # Takes the contour and read the text from what is inside the contours.
    
    return possible_subs


def get_last_subtitle():
    """ 
    Returns the last subtitle line.
     """
    all_subtitles = get_all_subtitles()
    if len(all_subtitles) > 0:
        return all_subtitles[-1]
    else:
        return ""


def compare_strings(subtitle_1, subtitle_2):
    """ 
    Return true if there is diffrence between strings. 
    If it's not a letter then change it to whitespace. 
    If there are 2 -- then it's the same string.
     """
    new_sub_1 = re.sub('[^A-Za-z]+', ' ', subtitle_1).lstrip() # lstrip removes whitespace.
    new_sub_2 = re.sub('[^A-Za-z]+', ' ', subtitle_2).lstrip()
    
    return new_sub_1 != new_sub_2
