#Make sure to pip install pyautogui before running

import pyautogui, time

time.sleep(1)

#the "beemovie" can be changed to the "masspinger" 

f = open("beemovie", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
