def run_translate(book3):
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = book3  # 'Hello, world!'
    # The target language
    target = 'eng'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    # Write translated text to file.
    f = open("book/translated_subtitles.txt", "a+", encoding="utf-8")
    subtitle_format = format(text)
    translated_subtitle = format(translation['translatedText'])
    f.write(translated_subtitle+"\n")
    f.close()

    print('Text: {}'.format(text))
    print('Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]
