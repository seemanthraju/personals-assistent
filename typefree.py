import pyautogul
import time
time.sleep(4)
count=0
while count<=100:
    pyautogul.typewrite("hii vachava"+str(count))
    pyautogul.press("enter")
    count=count+1