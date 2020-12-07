import pyautogui, time

time.sleep(1)

f = open("beemovie", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
