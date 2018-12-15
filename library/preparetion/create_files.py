

def create_files_for_subtitles():
    """ This function creates 3 empty files for our subtitles."""
    file = open("library/subtitles/frames_and_subtitles.txt", "w+", encoding="utf-8")
    file.close()
    f = open("library/subtitles/subtitle_from_movie.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()
    f = open("library/subtitles/translated_subtitles.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()
