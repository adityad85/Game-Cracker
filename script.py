import tesseract
import os

from PIL import ImageGrab,Image
from detect_text import IMAGE_PATH
#from pyhull import qhull
import pytesseract
from pytesseract import image_to_string
#import image_to_string
#from tesseract import image_to_string
import msvcrt as m
import time
from detect_text import launch_web,get_questions_and_answers,detect_text_with_bounds
from screengrab import screenshot
from utils import logit
import builtins
START_FULL=time.time()
original_open=open
#from . import VERSION,PILLOW_VERSION,_plugins
def main():
    while True:
        if raw_input():
           screenshot1(IMAGE_PATH)
           ##img=Image.open(IMAGE_PATH)
    #try:
    #    builtins.open = bin_open
           ##bts = pytesseract.image_to_string(img)
    #finally:
    #    builtins.open = original_open

    #print(str(bts, 'cp1252', 'ignore'))
           ##text = pytesseract.image_to_string(Image.open(IMAGE_PATH))
    #logit(text,START_FULL,time.time())
           text_here=detect_text_with_bounds(IMAGE_PATH)
    #print(text)

           get_questions_and_answers(*text_here,should_launch=True)
           ##launch_web(bts)
           ###launch_web(text_here)

def bin_open(filename, mode='rb'):       # note, the default mode now opens in binary
    return original_open(filename, mode)

def screenshot1(image_path):
    # [x0, y0, x1, y1] - take top left
    #img = ImageGrab.grab(bbo
    screenshot(image_path)


if __name__ == '__main__':
    main()

    END_FULL = time.time()
    logit("FULL", START_FULL, time.time())