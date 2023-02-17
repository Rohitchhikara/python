import pyautogui
import time 
time.sleep(3)
count=0
while count<=10:
    pyautogui.typewrite ("hello bhai "+str(count))
    pyautogui.press("enter")
    count=count+1







