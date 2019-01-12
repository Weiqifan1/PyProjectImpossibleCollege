# Live Translation of Movie Subtitles
### Presentation

##### Demo

##### Presentation Bo and Christian

### Overblik af programmet
##### Konturer
Hvor er der mulighed for at være tekst i en frame.  

##### Når teksten er fundet
Gør teksen mere tydelig.  
Oversæt teksten.  
Læs teksten højt.  

### Eksempler af dele af processen
```
def basic_color_mask(image, color_range_hsv, count_frames):
    """ 
    Create contrast between white and what is not white in a picture.
     """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_white = np.array(color_range_hsv[0], dtype=np.uint8)
    upper_white = np.array(color_range_hsv[1], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)

    return mask
 ```   
  ##### hsv
  ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/01basic_color_mask_COLOR_BGR2HSV/600basic_color_mask_COLOR_BGR2HSV.png)  
  
 ##### Resultet af basic_color_white
 ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/01c_basic_color_mask_after_inRange/600basic_color_mask_after_inRange.png)   
 
 
