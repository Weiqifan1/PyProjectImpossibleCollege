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

import library.preparetion.empty_folders as empty_folders
import library.preparetion.create_files as create
import library.processing.play_video as play_video
from docopt import docopt

# For testing. The movie finish at frame...
max_frame = 10000

def main(translation_language):
    empty_folders.empty_folders_before_run()
    create.create_files_for_subtitles()
    play_video.capture_video(translation_language, max_frame)

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
