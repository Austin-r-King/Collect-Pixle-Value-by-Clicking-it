import time
import pyautogui
import win32api
import PIL.ImageGrab

global Pixle_Values
Pixle_Values = []

def ListForPixlePlacement():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    i = 0
    while (i==0):
        currentMouseX, currentMouseY = pyautogui.position()
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        if a != state_left:  # Button state changed
            state_left = a
            if a < 0:
                print('Left Button Pressed')
                x=currentMouseX, currentMouseY
                Pixle_Values.append(x)
            else:
                print('Left Button Released')

        if b != state_right:  # Button state changed
            state_right = b
            if b < 0:
                print('Right Button Pressed')
            else:
                print('Right Button Released')
                i=1
        time.sleep(.001)

# Is used to make list of clicked positions
ListForPixlePlacement()

# used to just print the positions of teh pixles you clicked
# print(Pixle_Values)


global RGBValues
RGBValues = []
def CollectingRGBValue():
    x = 0
    while(x != len(Pixle_Values)):
        RGBValues.append(PIL.ImageGrab.grab().load()[Pixle_Values[x]])
        x += 1

# is used to make list of RGB values of clicked positions
CollectingRGBValue()

# prints RGB Values
print(RGBValues)
