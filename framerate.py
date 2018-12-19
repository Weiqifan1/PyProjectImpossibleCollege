import cv2
import library.translation_and_speech.translate as translate
import library.translation_and_speech.text_to_speech as text_to_speech
import library.translation_and_speech.audio as audio
import library.processing.find_subtitles as find_subtitles
from pathlib import Path


def speak(all_subtitles_list, translation_language):
    """ 
    Translate subtitles and calls audio.speak that read the text.
     """
    translate.run_translate(all_subtitles_list[-1], translation_language)
    text_to_speech.run_translate(len(all_subtitles_list), translation_language)
    audio.speak(len(all_subtitles_list))


def speak_from_frame(frame, count_frames, translation_language):
    """ 
    Is checking if there are text in a frame and if there is then it translate and read it.
     """
    find_possible_subtitles_list = find_subtitles.search_for_white_texts(frame)
    longest_string = find_subtitles.get_longest_string(find_possible_subtitles_list)
    longest_string = longest_string.replace('\n', ' ') # Removes newline and make a space so we get all the subtitles.
    last_subtitle = find_subtitles.get_last_subtitle()
    
    # if the line is not empty and there are new letters then it read the new letters.
    if len(longest_string.strip()) > 0 and find_subtitles.compare_strings(longest_string, last_subtitle):  
        find_subtitles.save_subtitles(longest_string, count_frames)

        all_subtitles = find_subtitles.get_all_subtitles()
        speak(all_subtitles, translation_language)


def capture_video(translation_language, max_frame):
    """ 
    Capture the video and show every 50. frame.
     """
    print("press q to quit the program")

    cap = cv2.VideoCapture('data/movies/videoplayback.webm')
    count_frames = 0 

    while(cap.isOpened()):
        _, frame = cap.read()
        '''
        if (count_frames % 50 == 0):
            cv2.imshow('frame', frame) # Show the fram on the screen.

            speak_from_frame(frame, count_frames, translation_language) 

            if (count_frames > max_frame):
                break
        '''
        if cv2.waitKey(1) == ord('q'):
            break
        count_frames += 1  
    cap.release()
    cv2.destroyAllWindows()

capture_video("english", 2000)

#end