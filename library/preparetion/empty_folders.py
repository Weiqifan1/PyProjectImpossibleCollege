import os

def empty_folders_before_run():

    folder_subtitles = 'library/subtitles'

    # Create a folder if it does not exist.
    create_folder(folder_subtitles)

    for the_file in os.listdir(folder_subtitles):
        file_path = os.path.join(folder_subtitles, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    
    folder_audio = 'library/audio'
    create_folder(folder_audio)

    for the_file in os.listdir(folder_audio):
        file_path = os.path.join(folder_audio, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)  
  