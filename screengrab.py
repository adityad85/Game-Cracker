# Take a screenshot of quicktime where it is set flush at top left
from PIL import ImageGrab
import os
import msvcrt as m
import pytesseract
from pytesseract import image_to_string

# full screen width is 2880 x 1800
SCREENSHOT_WIDTH = 850
SCREENSHOT_HEIGHT = 1150

def screenshot(image_path):
    # [x0, y0, x1, y1] - take top left
    #img = ImageGrab.grab(bbox=[5, 50, SCREENSHOT_WIDTH, SCREENSHOT_HEIGHT])
    img=ImageGrab.grab()
    #HQ coordinates
    box=(20,180,370,330)
    #LOCO coordinates
    #box=(20,280,370,430)
    #LOCO eLIMINATED coordinates
    #box=(20,320,370,430)
    #MOB show left
    #box=(20,450,370,520)
    #BrainBazi
    #box=(20,200,370,370)
    #StupidChat
    #box=(20,280,370,430)
    crop_img=img.crop(box)
    crop_img.save(image_path)

if __name__ == '__main__':
    # test path
    test_image_path = os.path.join(os.path.dirname(__file__), 'check.png')
    screenshot(test_image_path)
