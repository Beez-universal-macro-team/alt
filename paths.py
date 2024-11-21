from functions import *
import time

def PepperVic():
    sendMessage("Searching pepper")

    press("d", 2)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press("s", 0.5)

    ShiftLock()
    
    press("d", 0.2)

    for _ in range(9):
        keyboard.tap(Key.page_down)

        time.sleep(0.025)

    for _ in range(5):
        keyboard.tap(Key.page_up)

        time.sleep(0.025)

    for _ in range(4):
        keyboard.tap("o")

        time.sleep(0.15)

    
def PepperToCannon():
    sendMessage("Moving to cannon")
    press(Key.space, 0.1)
    keyboard.press("d")
    time.sleep(0.50)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(15)
    keyboard.release("s")
    time.sleep(0.10)
    keyboard.press("w")
    Waitspeed(6.3)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.tap(",")
    keyboard.tap(",")
    keyboard.tap(",")
    press(Key.space, 0.1)
    time.sleep(0.1)
    press(Key.space, 0.1)
    time.sleep(2.62)
    keyboard.tap(".")
    time.sleep(0.87)
    press(Key.space, 0.1)
    time.sleep(1.25)

def MountVic():
    sendMessage("Checking mountian")
    keyboard.tap("e")
    time.sleep(1.70)
    press(Key.space, 0.1)
    press(Key.space, 0.1)
    time.sleep(1)
    keyboard.tap(",")
    keyboard.tap(",")
    time.sleep(0.38)

    press(Key.space, 0.1)
    time.sleep(1)

    keyboard.tap(".")
    keyboard.tap(".")
    keyboard.tap(".")
    keyboard.tap(".")

    keyboard.press("d")
    Waitspeed(6.9)
    keyboard.release("d")
    time.sleep(0.10)
    keyboard.press("s")
    Waitspeed(2)
    keyboard.release("s")
    time.sleep(0.10)
    
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down) 
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    time.sleep(0.15)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(1)

def CactusVic():
    sendMessage("Checking cactus")
    keyboard.tap(Key.page_up)
    keyboard.tap(Key.page_up)
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("d")
    keyboard.press("w")
    Waitspeed(27)
    keyboard.release("w")
    Waitspeed(13)
    keyboard.release("d")
    keyboard.press("w")
    Waitspeed(8)
    keyboard.release("w")
    time.sleep(0.05)
    keyboard.press("s")
    Waitspeed(3.6)
    keyboard.release("s")
    keyboard.tap(".")
    press(Key.space, 0.1)
    time.sleep(0.1)
    press(Key.space, 0.1)
    time.sleep(0.5)
    keyboard.tap(".")
    time.sleep(1.85)
    press(Key.space, 0.1)
    time.sleep(1.25)
    keyboard.press("d")
    Waitspeed(6.6)
    keyboard.release("d")
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    keyboard.tap(Key.page_down)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(1)

def RoseVic():
    sendMessage("Checking rose")
    keyboard.press("w")
    Waitspeed(6)
    keyboard.press("a")
    Waitspeed(15)
    keyboard.release("w")
    Waitspeed(24)
    keyboard.release("a")
    press(Key.space, 0.1)
    time.sleep(0.1)
    keyboard.press("a")
    Waitspeed(4)
    keyboard.press("w")
    Waitspeed(17)
    keyboard.release("a")
    time.sleep(1)
    keyboard.press("w")
    Waitspeed(1.5)
    keyboard.release("w")
    time.sleep(0.10)
    keyboard.press("d")
    Waitspeed(10)
    keyboard.release("d")
    keyboard.tap(",")
    keyboard.tap(",")
    keyboard.press("d")
    Waitspeed(1)
    keyboard.release("d")
    time.sleep(0.50)
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("o")
    time.sleep(0.15)
    keyboard.tap("i")
    time.sleep(1)