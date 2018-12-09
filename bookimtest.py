
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
# book2 images
"book2/contour_250_1.jpg"
"book2/contour_350_1.jpg"
"book2/contour_400_1.jpg"
"book2/contour_500_1.jpg"
"book2/contour_600_1.jpg"
"book2/contour_650_1.jpg"
"book2/contour_800_1.jpg"
"book2/contour_850_1.jpg"
"book2/contour_900_1.jpg"

goodpic = ["book2/contour_250_1.jpg",
"book2/contour_350_1.jpg","book2/contour_400_1.jpg",
"book2/contour_500_1.jpg",
"book2/contour_600_1.jpg",
"book2/contour_650_1.jpg",
"book2/contour_800_1.jpg",
"book2/contour_850_1.jpg",
"book2/contour_900_1.jpg"]

file = open("test_results/mynew.txt", "w", encoding="utf-8")
file.write("")
file.close()

def rens_friske_subtitles(image):
    cont = get_still_filter.text_image_black_white(image, [[0,0,255],[255,255,255]])
    clean_cont =  get_still_filter.cleaning_subs(cont)
    text = pytesseract.image_to_string(cont, lang="dan")
    return text

def rens2(image):
    cont = get_still_filter.text_image_black_white(image, [[0,0,255],[255,255,255]])
    clean_cont =  get_still_filter.cleaning_subs(cont)
    text = pytesseract.image_to_string(cont, lang="dan")
    return text

for chr in goodpic:
    image = cv2.imread(chr)
    #text = rens_friske_subtitles(image)
    text = rens2(image)

    print("                               "+chr)
    print(text)  #debugging
    file = open("test_results/mynew.txt", "a+")
    file.write(text)
    file.close()

cv2.waitKey(0)


# test
'''
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

image = cv2.imread("book/frame_900.jpg")

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
'''
