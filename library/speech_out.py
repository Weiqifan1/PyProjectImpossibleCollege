
#import pyaudio
import wave
import sys
import os
# python -m pip install pyaudio

import pygame
#python -m pip install -U pygame

def speak(numOfSubLines):
    print("this is speek out: " + str(numOfSubLines))

    pygame.mixer.pre_init(22100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init() #turn all of pygame on.
    pygame.mixer.music.load('audio/output'+str(numOfSubLines)+'.mp3')
    pygame.mixer.music.play()
    
    # popen intro til pandas
    # subprocess
    # pipe