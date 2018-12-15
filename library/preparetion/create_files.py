

def create_files_for_subtitles():
    """ This function creates 3 empty files for our subtitles."""
    file = open("book/book.txt", "w+")
    file.write("")
    file.close()
    f = open("book/book3.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()
    f = open("book/translated_subtitles.txt", "w+", encoding="utf-8")
    f.write("")
    f.close()
