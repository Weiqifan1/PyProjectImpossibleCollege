import pytesseract
import re
import cv2
import library.processing.simpel_video_filter as simpel_video_filter
import library.processing.create_contours as create_contours

def get_all_subtitles():
    readf = open('data/output/subtitles/subtitle_from_movie.txt', mode='r', encoding='utf-8')
    linesFromF = readf.readlines()
    readf.close()
    return linesFromF

def get_text_from_frame(contours, original_frame):
    """ 
    Tager konturer og original frame fjerner støj og kalder tesseract.
    Returner en liste a strings, der kan være subtitles(eller fejllæsninger).
     """
    img = None
    contCount = 0
    x = y = w = h = None
    possible_subs = []
    for contour in contours:
        contCount = contCount+1
        x, y, w, h = cv2.boundingRect(contour)
        crop_img = original_frame[y:y+h, x:x+w]
        img = simpel_video_filter.clean_image(crop_img)
        text = pytesseract.image_to_string(img, lang="dan")
        possible_subs.append(text)
    return possible_subs

def save_subtitles(longest_str, count_frames):
    """ 
    Gemmer undertekster.
     """
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
    """ 
    Leder efter hvis tekst og læser teksten.
     """
    test_frame = frame.copy()
    original_frame = frame.copy()
    basic = simpel_video_filter.basic_color_mask(test_frame, [[0, 0, 255], [255, 255, 255]])
    cont = create_contours.white_contours(basic)
    contours = create_contours.create_large_contoures(cont) # Sætter konturer om hvis tekst.
    possible_subs = get_text_from_frame(contours, original_frame) # Tager konturer og læser tekst fra de steder.
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
    Alt der ikke er stort eller lille bogstav gøres til whitespace. Samme string hvis der er 2 bindestreger.
     """
    new_sub_1 = re.sub('[^A-Za-z]+', ' ', subtitle_1).lstrip() # lstrip fjerner whitespace.
    new_sub_2 = re.sub('[^A-Za-z]+', ' ', subtitle_2).lstrip()
    
    return new_sub_1 != new_sub_2
