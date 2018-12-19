# Imports the Google Cloud client library
from google.cloud import translate
from pathlib import Path


def run_translate(subtitle_from_movie, translation_language):
    """ 
    Translate a text file from one language to another.
     """
    # Instantiates a client.
    translate_client = translate.Client()

    # The text to translate.
    text = subtitle_from_movie  

    # The target language.
    target = translation_language 

    # Translates some text into target language.
    translation = translate_client.translate(
        text,
        target_language=target)

    # Write translated text to file.
    with open(Path("data/output/subtitles/translated_subtitles.txt"), "a+", encoding="utf-8") as file:
        subtitle_format = format(text)
        translated_subtitle = format(translation['translatedText'])
        file.write(translated_subtitle + "\n")
