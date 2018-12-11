import numpy as np
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import asyncio
from library import get_still_filter
from library import test_async

# Open Anaconda prompt.
# conda update -n root conda
# conda update --all

#2018-12-10 - i saveImToBook - linje 93+94: 
#   crop ikke conturer der er for langt fro normale succefulde conturer.

#asyncio.run(test_async.start_async())

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())