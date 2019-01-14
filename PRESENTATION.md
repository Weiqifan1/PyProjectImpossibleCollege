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
 
 ##### Find hvide kontourer
  ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/03white_contours_find_contours/600find_contours.png)   
  
 ##### Eksempel på flere konturer i en frame
 ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/03white_contours_find_contours/650find_contours.png)  
 
##### Cropper konturene i framen
 ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/04crop_image/600_001_crop_image.png
 )  
 
 ##### Eksempel hvis der er flere konturer i en frame
  ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/04crop_image/650_009_crop_image.png)  

#### Fjern støj
```
def clean_image(image, count_frames):
    """ 
    Remove noise from a small part of the picture. In the lower part of the picture where the subtitle is.
     """
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # grey

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize - more pixels to work with.
    
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return img
```
##### Grey Scale
  ![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/05color_bgr2gray/600_grey_image.png)  
  
##### Resize
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/06resize/600_resize_image.png)  
##### Dilate - Forstørrer hvide områder
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/07dilate/600_dilate_image.png)

##### Erosion - Gør de hvide områder mindre
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/08erode/600_erode_image.png)

##### Treshold - Hvide områder fremstår tydeligere og alt andet sort
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/presentation/data/output/frames/09clean_img_after_threshold/600_clean_image_after_threshold.png)  

### Tekst der læses forkert
##### Læses rigtigt
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/saveframes/data/output/frames/1050_001_6clean.png)

##### Læses forkert
![alt text](https://github.com/Weiqifan1/PyProjectImpossibleCollege/blob/saveframes/data/output/frames/1000_001_6clean.png)

