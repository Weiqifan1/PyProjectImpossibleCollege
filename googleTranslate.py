""" 
Install enviroment variable to Googles API.
https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python

In the GCP Console, go to the Create service account key page.
"GO TO THE CREATE SERVICE ACCOUNT KEY PAGE" (Click the above link and click on the link on top of the page.)

From the Service account drop-down list, select New service account.
In the Service account name field, enter a name .
From the Role drop-down list, select Project > Owner.
Click Create. A JSON file that contains your key downloads to your computer.


SEND FEEDBACK
Documentation   Authentication
Getting Started with Authentication
This article shows the recommended way to authenticate to a Cloud API.

Authentication refers to the process of determining a client's identity. 
Authorization refers to the process of determining what permissions 
an authenticated client has for a set of resources. 
That is, authentication refers to who you are, and 
authorization refers to what you can do.

For authentication, we recommend using a service account: 
a Google account that is associated with your GCP project, 
as opposed to a specific user. Service accounts can be 
used for authentication regardless of where your code 
runs (locally, Compute Engine, App Engine, on premises, etc.). 
For more information about other authentication types, see authentication overview.

Windows
With PowerShell
$env: GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

For example
Wite the example from the above link.

With command prompt:
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]

Linux/Mac
Write the example here!

Setting the environment variable allows you to provide credentials separately from your application, 
without making changes to application code when you deploy. 
Alternately, you can explicitly specify the path to the service account key file in your code. 
For more information, see the https://cloud.google.com/docs/authentication/production#obtaining_and_providing_service_account_credentials_manually

After setting the environment variable, you don't need to explicitly specify your credentials in code when 
using a Google Cloud Client Library. The client library can determine your credentials implicitly.

pip install --upgrade google-cloud-translate
pip install --upgrade google-cloud-storage
pip install --upgrade google-cloud-texttospeech

Enable Translate API
https://www.youtube.com/redirect?q=https%3A%2F%2Fcloud.google.com%2Ftranslate%2Fdocs%2Freference%2Flibraries%23client-libraries-usage-python&v=WH7EQFbuIrI&event=video_description&redir_token=xsDR7eKRFP3fIhSngWFFrYToNLF8MTU0NDUyMDc1NUAxNTQ0NDM0MzU1

Create bucket
https://cloud.google.com/storage/docs/moving-buckets#storage-create-bucket-console

https://googleapis.github.io/google-cloud-python/latest/translate/usage.html
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/translate/cloud-client
https://cloud.google.com/translate/docs/translating-text
https://cloud.google.com/text-to-speech/docs/basics
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/texttospeech/cloud-client
 """

def run_quickstart():
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'ru'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]


        # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text="Hello, World!")

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    # [END tts_quickstart]


if __name__ == '__main__':
    run_quickstart()
