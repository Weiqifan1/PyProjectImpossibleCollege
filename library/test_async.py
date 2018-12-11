
import os
import time
import asyncio
from library import text_to_speech
from library import speech_out

###############################################
# rens mapperne Book, audio
##########################################
folder = 'book'
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

f = open("book/book3.txt", "w+", encoding="utf-8")
f.write("")
f.close()
f = open("book/translated_subtitles.txt", "w+", encoding="utf-8")
f.write("")
f.close()
###############################################
# rens mapperne Book, audio
##########################################


'''

def start_async():
    print("hello async")
    paragraph_list = text_from_book2()
    
    print_paras(paragraph_list)
    stupid_sum()
    
    


def text_from_book2():
    f = open("book2/async_test.txt", "r", encoding="utf-8")
    #holmes = f.read(50)
    holmes = f.read()
    paragraph = holmes.split("\n\n") #each paragraph in holmes - no empy paragraphs
    f.close()
    return paragraph
    #text_to_speech.save_input_as_audio(paragraph[0], 1)


async def print_paras(listOFParas):
    for para in listOFParas:
        print(para)
        await asyncio.sleep(5)

def stupid_sum():
    time_int = 0
    while time_int < 5:
        time.sleep(1)
        time_int += 1
        print(time_int)
'''
