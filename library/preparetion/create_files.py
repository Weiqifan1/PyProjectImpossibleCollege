from pathlib import Path # Make sure it / or \ depending on os.


def create_files_for_subtitles():
    """ 
    This function creates 3 empty files for our subtitles.
    """
    path_to_empty_file = ['data/output/subtitles/frames_and_subtitles.txt', 'data/output/subtitles/subtitle_from_movie.txt', 'data/output/subtitles/translated_subtitles.txt']
    
    for element in path_to_empty_file:
        with open(Path(element), 'w+', encoding="utf-8") as file:
            file.write('')
