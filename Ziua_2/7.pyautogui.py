# pip install pyautogui

import pyautogui
import time

screen_width, screen_height = pyautogui.size()
print("Width:", screen_width, "Height:", screen_height)


pyautogui.moveTo(829, 747, duration=1)
time.sleep(1)
pyautogui.click()
