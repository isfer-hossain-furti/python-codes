import pyautogui
import time
time.sleep(10)
f = open("movie.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
# make sure you have pyautogui installed
