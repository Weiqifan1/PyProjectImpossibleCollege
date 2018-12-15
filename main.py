import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import library.preparetion.empty_folders as empty_folders
import library.preparetion.create_files as create
import library.processing.saveImToBook as save

#2018-12-10 - i saveImToBook - linje 93+94: 
#   crop ikke conturer der er for langt fro normale succefulde conturer.

empty_folders.empty_folders_before_run()
create.create_files_for_subtitles()
save.capture_video()
