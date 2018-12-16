

def create_files_for_subtitles():
    """ This function creates 3 empty files for our subtitles."""
    f = open("data/output/subtitles/frames_and_subtitles.txt", "w+", encoding="utf-8")
    f.close()
    f = open("data/output/subtitles/subtitle_from_movie.txt", "w+", encoding="utf-8")
    f.close()
    f = open("data/output/subtitles/translated_subtitles.txt", "w+", encoding="utf-8")
    f.close()
