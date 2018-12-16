"""Translate_Subtitles.

Usage:
    main.py
    main.py (-h | --help)
    main.py (-v | --version)
    main.py <language>

Options:
    <language>          Optional name argument. Language that can be used: english, italian, swedish, dutch, japanese, french, german. 
    -h --help           Show this screen.
    -v --version        Show version.

"""

import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import library.preparetion.empty_folders as empty_folders
import library.preparetion.create_files as create
import library.processing.saveImToBook as save
from docopt import docopt
# pip install docopt==0.6.2

#2018-12-10 - i saveImToBook - linje 93+94: 
#   crop ikke conturer der er for langt fro normale succefulde conturer.

def main(translation_language):
    empty_folders.empty_folders_before_run()
    create.create_files_for_subtitles()
    save.capture_video(translation_language)


def check_language(language):
    language_list = {'english': 'en', 'italian': 'it', 'swedish': 'sv', 'dutch': 'nl', 'japanese': 'ja', 'french': 'fr', 'german': 'de'}
    
    # Check to find the language code for choosen language.
    return {main(language_list[language]) if language in language_list else print('Wrong input!')}


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Translate Subtitles 1.0')
    if arguments['<language>']:
        check_language(arguments['<language>'])
    else:
        translation_language = 'en'
        main(translation_language)
