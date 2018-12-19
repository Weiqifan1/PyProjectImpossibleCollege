from google.cloud import texttospeech


def run_translate(numOfSubLines, translation_language):
    """ 
    Synthesizes speech from the input string of text.
     """
    # Instantiates a client.
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized.
    readf = open('data/output/subtitles/translated_subtitles.txt', mode='r', encoding='utf-8')
    translated_subtitles = readf.readlines()

    readf.close()

    synthesis_input = texttospeech.types.SynthesisInput(
        text=translated_subtitles[-1])

    # Build the voice request, select the language code (eks. "en-US") and the ssml.
    # voice gender ("neutral").
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=translation_language, 
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned.
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type.
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('data/output/audio/output'+str(numOfSubLines)+'.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output'+str(numOfSubLines)+'.mp3"')
