import wave
import sys
import os
import pygame

def speak(numOfSubLines):
    """ 
    Play the audio file.
     """
    print("this is speek out: " + str(numOfSubLines))

    pygame.mixer.pre_init(22100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init() # turn all of pygame on.
    pygame.mixer.music.load('data/output/audio/output'+str(numOfSubLines)+'.mp3')
    pygame.mixer.music.play()
    