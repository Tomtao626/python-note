# coding: utf-8
# 截图

from pyautogui import screenshot
from PIL import ImageGrab
import time

def grab_screenshot():
    shot = screenshot()
    shot.save("screenshot.png")

def grab_screenshot_area(area_conf: tuple):
    shot = ImageGrab.grab(area_conf)
    shot.save("screenshot.png")

def grab_screenshot_delay(time_conf: int):
    time.sleep(time_conf)
    shot = screenshot()
    shot.save("screenshot.png")


if __name__ == '__main__':
    grab_screenshot()
