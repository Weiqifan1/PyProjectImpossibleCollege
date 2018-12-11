import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from library import get_still_filter

#2018-12-10 - i saveImToBook - linje 93+94: 
#   crop ikke conturer der er for langt fro normale succefulde conturer.

print("hello")
print("Hey")
