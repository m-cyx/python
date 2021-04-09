import pyautogui
import keyboard
from time import sleep

start_key = '1'
stop_key = '2'
i = 0
while True:
    if keyboard.is_pressed( start_key ):
        while not keyboard.is_pressed(stop_key):
            pyautogui.click()
            # i+=1
            # print('test'+str(i))
            sleep(0.8)

    if keyboard.is_pressed( stop_key ):
        break