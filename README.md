# Live Translation of Movie Subtitles
### Documentation
This is the exam project for 4. semester at CPH Business made by Impossible College.  

The program will be able to get the subtitles from a movie, translate it and read alound the translated language. 
The basic program reads a danish subtitle from a black background by finding the area with most white pixels. 
The words that are found is written to a text file. The text file is translated to english and save in a text file and the translation will be read aloud.  
All this will happen live so the translation that is read aloud will follow the subtitles from the movie.  

### Group
Christian Lykke, Anders Nissen and Bo Henriksen.  

### Dependencies
The project uses the latest version of Pythons Anaconda installation.  

It also uses these dependencies:  
pip install opencv-python  
python -m pip install -U pygame  
pip install docopt==0.6.2  
pip install pytesseract  
pip install --upgrade google-cloud-translate  
pip install --upgrade google-cloud-texttospeech  

### Installation of tesseract and pytesseract  
1. Go to this homepage https://github.com/UB-Mannheim/tesseract/wiki and download tesseract.  
2. For windows users run the .exe file and install the program.  
3. Choose additional script data(download) and additional language data(download).  

#### Environment variables for tesseract
1. Find the path to tesseract-OCR on your operating system and copy it.  
2. Open the window for enviroment variables. On windows press window key + pause key.  
3. In system choose PATH and press edit.  
4. Choose new and paste the path to tesseract-OCR and close the window.  
5. Close your terminal and open it again.  

6. In your terminal write: pip install pytesseract.

### Get a Google API key
1. Open this page https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python  
2. GO TO THE "CREATE SERVICE ACCOUNT KEY PAGE" (Click the above link and click on the link on top of the page.)  
3. From the Service account drop-down list, select New service account.  
4. In the Service account name field, enter a name for the project.  
5. From the Role drop-down list, select Project > Owner.  
6. Click Create. A JSON file that contains your key downloads to your computer.  

#### Enable translation and text-to-speech API (On Google Cloud Homepage)  
1. Click on dashboards in the upper left corner when you have downloaded your json file.  
2. Click Enable APIs.  
3. Click on view all for machine learning.  
4. Enable cloud translation API.  
5. Go to this page https://cloud.google.com/text-to-speech/docs/quickstart-protocol  
6. Below "Before you begin" - click 3 "Enable the Cloud Text-to-Speech API" and choose your project(the project you created above).  

#### Link to your json file for each terminal session  
##### Windows  
##### With PowerShell  
$env: GOOGLE_APPLICATION_CREDENTIALS="[PATH]"  

##### With command prompt:  
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]  

##### For example  
set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\[username]\Downloads\googleApi\[name_of_your_jsonfile.json]  

##### Linux/Mac  
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"  

##### For example:   
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"  

On some operating systems this does not work. It's possible to set up an enviroment variable. The advantages is you dont have to link to your json file each time you open a new terminal.  

After setting the environment variable, you don't need to explicitly specify your credentials in code when  
using a Google Cloud Client Library. The client library can determine your credentials implicitly.  

#### Environment variables for your Google authentication json file.  
1. Find the path to your google authentication json file on your operating system and copy it.  
2. Open the window for enviroment variables. On windows press window key + pause key.  
3. In user choose new enviromental variable. 
4. In name write: GOOGLE_APPLICATION_CREDENTIALS  
5. In value write: [PATH TO JSON FILE WITH CREDENTIALS]  
6. Click ok and exit. 
7. Close your terminal and open it again. 

8. pip install --upgrade google-cloud-translate  
9. pip install --upgrade google-cloud-texttospeech  

### How to run the project
1. Clone the project  
2. Cd into the directory of the project  
3. Example of how to run the project  
4. `python main.py <language>`  
5. `python main.py` or `python main.py japanese` 
6. If you need help or want to see which countries you can translate to write: `python main.py -h` or `python main.py --help`  
