
# [START tts_quickstart]
"""Synthesizes speech from the input string of text or ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
from google.cloud import texttospeech


def run_translate(numOfSubLines):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    readf = open('book/translated_subtitles.txt', mode='r', encoding='utf-8')
    translated_subtitles = readf.readlines()
    # print(linesFromF)
    readf.close()

    synthesis_input = texttospeech.types.SynthesisInput(
        text=translated_subtitles[-1])

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',  # en-US de-DE sv-SE
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('audio/output'+str(numOfSubLines)+'.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output'+str(numOfSubLines)+'.mp3"')
        # [END tts_quickstart]


""" if __name__ == '__main__':
    run_quickstart() """


def save_input_as_audio(sentence, videoNumber):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    #readf = open('book/translated_subtitles.txt', mode='r', encoding='utf-8')
    #translated_subtitles = readf.readlines()
    # print(linesFromF)
    #readf.close()

    synthesis_input = texttospeech.types.SynthesisInput(
        text = sentence)#translated_subtitles[-1])

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',  # en-US de-DE sv-SE
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('audio/sentence'+str(videoNumber)+'.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('save_input_as_audio (mp3)')
        # [END tts_quickstart]
