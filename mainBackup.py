# 2018-12-16
#trods succefuld installation af codopt (# pip install docopt==0.6.2)
#fås fejlen:
#TypeError:__init__() got an unexpected keyword argument  'serialized options'

import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import library.preparetion.empty_folders as empty_folders
import library.preparetion.create_files as create
import library.processing.saveImToBook as save


def main(translation_language):
    empty_folders.empty_folders_before_run()
    create.create_files_for_subtitles()
    save.capture_video(translation_language)

empty_folders.empty_folders_before_run()
create.create_files_for_subtitles()
save.capture_video('en')





#end