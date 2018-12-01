
import sys
print(sys.version_info)


import numpy as np
import matplotlib.pyplot as plt
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

print("hello")

#import pic

# change python path:
# https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode
# files -> preferences -> settings -> Python Configuration(82):
# "python.pythonPath": "C:\\Anaconda3\\envs\\py34\\python.exe"

# https://code.visualstudio.com/docs/python/environments
# Python: Select Interpreter

#img = cv2.imread('pic/pic1WonB.png', cv2.IMREAD_GRAYSCALE)

#vid 1 - ca. 10.00 virker
# https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
#cv2.imshow('graa', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()