
import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter

"pic1WonB.png"
"pic2W.jpg"
#billeder med problemer:
"book/frame_850.jpg"
"book/frame_900.jpg"

image = cv2.imread("book/frame_850.jpg")

cont = get_still_filter.text_image_black_white(image, [[0,0,255],[255,255,255]])
clean_cont =  get_still_filter.cleaning_subs(cont)
text = pytesseract.image_to_string(cont, lang="dan")


print(text)  #debugging
file = open("test_results/mynew.txt", "w")
file.write(text)
file.close()
#get_still_filter.read_pic_save_text(clean_cont, "test_results/binary.png" ,"test_results/mynew.txt")

cv2.imshow("image", image)
cv2.imshow("cont", cont)
cv2.imshow("clean_cont", clean_cont)

cv2.waitKey(0)