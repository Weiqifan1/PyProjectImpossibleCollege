

#!/usr/bin/python3

import numpy as np
from PIL import Image
import pytesseract
import cv2
import os
import library.processing.simpel_video_filter as simpel_video_filter
import library.translation_and_speech.translate as translate
import library.translation_and_speech.text_to_speech as text_to_speech
import library.processing.create_contours as create_contoures
import library.translation_and_speech.audio as audio
import library.processing.find_subtitles as find_subtitles
import queue
import threading
import time


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


class myThread_pictures(threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data_pictures(self.name, self.q)
      print ("Exiting " + self.name)

def process_data_pictures(threadName, q):
    #exitFlag = 0
    #while not exitFlag:
    queueLock.acquire()
    if not workQueue.empty():
        data = q.get()
            #max_frame = data[3]
            #if max_frame <= 
        queueLock.release()
                    #speak_from_frame(frame, count_frames, translation_language) 
        speak_from_frame(data[0], data[1], data[2])  #print ("%s processing %s" % (threadName, data))
    else:
        queueLock.release()
            #time.sleep(1)

def capture_video(translation_language, max_frame):
    
    # exitFlag = 0 jeg prøver at undgå at bruge den

    #queueLock = threading.Lock() #jeg proever at laegge dem over i main.
    #workQueue = queue.Queue(10)

    #threads = []

    thread_one = myThread_pictures(1, "Tråd_et", workQueue)
    thread_one.start()
    #threads.append(thread_one)
    
    """ 
    Capture the video and show every 50. frame.
     """
    print("press q to quit the program")
    cap = cv2.VideoCapture('data/movies/videoplayback.webm')
    count_frames = 0 

    while(cap.isOpened()):
        _, frame = cap.read()
        cv2.imshow('frame', frame) #show every frame on screen

        if (count_frames % 50 == 0):
            #cv2.imshow('frame', frame) # Show the fram on the screen.

            queue_item = [frame, count_frames, translation_language]
            queueLock.acquire()
            workQueue.put(queue_item)
            queueLock.release()
            #speak_from_frame(frame, count_frames, translation_language) 

            if (count_frames > max_frame):
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count_frames += 1  # count frames.
    #exitFlag = 1 #tråd ariabel
    thread_one.join()       #vent på at tråd er faerdig

    cap.release()
    cv2.destroyAllWindows()
