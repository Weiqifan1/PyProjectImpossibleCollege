import os
from pathlib import Path


def empty_folders_before_run():
    """ 
    Empty folders and create folders for the subtitles and audio files if it does not exist.
    """

    folder_frames = Path('data/output/frames')
    # Create a folder if it does not exist.
    create_folder(folder_frames)
    for the_file in os.listdir(folder_frames):
        file_path = os.path.join(folder_frames, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


    folder_subtitles = Path('data/output/subtitles')
    # Create a folder if it does not exist.
    create_folder(folder_subtitles)

    for the_file in os.listdir(folder_subtitles):
        file_path = os.path.join(folder_subtitles, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    
    folder_audio = Path('data/output/audio')
    create_folder(folder_audio)

    for the_file in os.listdir(folder_audio):
        file_path = os.path.join(folder_audio, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def create_folder(directory):
    """ 
    Creates a folder.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)  
  