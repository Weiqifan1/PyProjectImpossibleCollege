# PyProjectImpossibleCollege
Dette er eksamensprojektet for team Impossible College - Bo Henriksen, Anders Nissen og Christian Lykke

2018-11-27

Projektet går ud på at læse eksisterende undertekster i videoer.
Første skridt: vi vælger et simpelt undertekst format med dansk eller engelsk tekst, og ser om vi kan skrve et program der kan læse underteksten ud fra videoens pixels.
Til dette skridt har vi foruddefineret hvilket alfabet/sprog programmet skal lede efter, og vi fortæller programmet hvilket format det skal lede efter. Det vil sige at vi f.eks. fortæller programmet at den kan finde underteksten omkrandset af sorte rektangler i bunden af skærmen.

Hvis dette virker, vil vi prøve at udvidde programmet med at lede efter undertekster på samme sprog (stadig dansk eller engelsk) men forskellige undertekst formater.

Hvis dette virker, prøver vi at få programmet til at virke med undertekster på forskellige sprog.

Vi forestiller os at bruge eksisterende projekter på github, som har en licens der tillader andre prorammører at klone og redigere deres kode. Disse projekter vil vi så bygge videre på med vores egen kode.

Vi sørger for at de kodeafsnit vi ikke selv har skrevet nemt kan identificeres.

### 1. iteration genkendelse af tekst på billeder og frames
Genkendelse af tekster og fjernelse af støj fra billede.  
https://github.com/Weiqifan1/PyProjectImpossibleCollege/tree/chr181202b  

Genkendelse af undertekst fra frames og skriv det til en fil.  
https://github.com/Weiqifan1/PyProjectImpossibleCollege/tree/fors%C3%B8g  

### 2. iteration
Fjerne resten af støjen fra et (video)billedet.  
Gem tekstfilen rigtigt.  
Se om de enkelte frames ændrer sig, og genkend kun tekst når framen har ændret sig.  
Refrakturering.  
Oversæt underteksten live.  

Hvis kun hvert 50 frame.  
https://github.com/Weiqifan1/PyProjectImpossibleCollege/tree/chr181210  

Google translate og tekst til tale.  
https://github.com/Weiqifan1/PyProjectImpossibleCollege/tree/googleTranslate  

Har sat de 2 features sammen.  
https://github.com/Weiqifan1/PyProjectImpossibleCollege/tree/liveSpeech  

### 3. iteration  
If speech is behind speed it up.  
Refakturer.  
Dokumentation.  
Gem tekstfilen rigtigt.  



Videoer.  
Hvid tekst på sort baggrund.  
https://www.youtube.com/watch?v=86d7jx2YB0Y  

Hvid tekst på sort baggrund. 2 sprog samtidig.  
https://www.youtube.com/watch?v=ExNTMDsmAMk&vl=da  

Hvis tekst på videoens baggrund.  
https://www.youtube.com/watch?v=8YEM_hn5o78  
https://www.youtube.com/watch?v=nfMSjCeY9UA  

Hvis tekst på grå gennemsigtig baggrund.  
https://www.youtube.com/watch?v=Zw9OKRp2fZQ  

https://docs.opencv.org/3.4/db/d5c/tutorial_py_bg_subtraction.html  
https://stackoverflow.com/questions/46866121/how-to-crop-bottom-part-of-an-imagepart-with-subtitle-in-python  

https://www.kerrickstaley.com/2017/05/29/extracting-chinese-subs-part-1  
https://softwarerecs.stackexchange.com/questions/7521/program-that-can-extract-subtitles-from-hard-subbed-videos  

DEPENDENSIES:
Dependencies der ligger i anaconda:
Numpy, Pillow, opencv.
Herudover: 
tesseract og pytesseract skal være installeret.

### GUIDE TIL INSTALLATION AF TESSERACT OG PYTESSERACT:
Gå til https://github.com/UB-Mannheim/tesseract/wiki
Download og kør: tesseract-ocr-w64-setup-v4.0.0.20181030.exe (hvis man bruger windows 64bit)
Under installation bliver man bedt om at værlge om man vil installere scripts og sprogfiler til andre sprog end engelsk.
Installer gerne sprogfiler (og scriptfiler hvis de er på listen) til sprogene:
Dansk, Fransk, Tysk, Koreansk (horizontal), simplificeret kinesisk (horizontal), traditionel Kinesisk (horizontal).
(hvis det lykkes for os at få programmet til at virke til engelsk, prøver vi på andre sprog).  
Vælge sprog og script.  

### Miljøvariabel
Find stien til tesseract-OCR
Åben viduet til miljøvariabler. windowskey + pause key.
Under system væl PATH og tryk rediger.  
Vælg ny og paste stien til tesseract-OCR ind.  
Luk og command line og start den igen.  

### Dependencies
pip install pytesseract   


