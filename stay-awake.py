# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:31:20 2019

@author: phoenixnitin
"""

import pyautogui
import time
import sys
from datetime import datetime
from pynput import keyboard

pyautogui.FAILSAFE = False
numMin = None
break_program = False
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1
else:
    numMin = int(sys.argv[1])
    
def on_press(key):
    global break_program
    #print(key)
    if key == keyboard.Key.end:
        print('end pressed')
        break_program = True
        return False
    
with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        x=0
        while(x<numMin):
            try:
                time.sleep(60)
                x+=1
                if break_program == False:    
                    for i in range(0,200):
                        pyautogui.moveTo(0,i*4)
                    pyautogui.moveTo(1,1)
                    for i in range(0,3):
                        pyautogui.press("shift")
                    print("Movement made at {}".format(datetime.now().time()))
            except KeyboardInterrupt:
                print('Execution Interrupted')
                exit()
