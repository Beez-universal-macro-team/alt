from pynput.mouse import Button, Controller
import time
from randomServer import joinRandomServer
from functions import isWindowOpen, isColorClose, sendMessage, sendScreenshot, leave, reset, press, screenshot, click, offsetDims, findImg, readFile
import webbrowser
import pyautogui

mouse = Controller()

claimHiveMonitor = {
        "top": offsetDims(62, "y"),
        "left": offsetDims(852, "x"),
        "width": offsetDims(1136 - 852, "x"),
        "height": offsetDims(121 - 62, "y"),
        "mon": 0,
}

def waitForLoading(maxWaitTime=20):
    tm = time.time()

    while True:
        screen = screenshot()

        if isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), (34, 87, 168), 15):
            break

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

    tm = time.time()

    #print("Loading found!")

    while True:
        screen = screenshot()
        
        colors = [(34, 87, 168), (83, 100, 108)]
        
        night = False
        
        for color in colors:
            if isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), color, 15):
                night = True
                
        if night:
            return True

        elif time.time() - tm >= maxWaitTime:
                return False

        time.sleep(0.05)

def detectNight():
    #try:
        #beesmas_enabled = int(readFile("guiFiles/beesmasToggle.txt"))
    #except:
        #beesmas_enabled = 0

    beesmas_enabled = False

    # Load model based on toggle
    if beesmas_enabled:
        target_colors = (86, 100, 107)

    else:
        target_colors = [(24, 76, 28),
                         (0, 77, 31)]


    max_diff = 10  # Adjust this value for color tolerance

    screen_width, screen_height = pyautogui.size()

    # Check multiple points on the screen for better accuracy
    check_points = [
        (screen_width // 2, screen_height // 2),
        (screen_width // 4, screen_height // 4),
        (3 * screen_width // 4, 3 * screen_height // 4)
    ]

    for point in check_points:
        pixel_color = pyautogui.pixel(point[0], point[1])

        print(pixel_color)

        for target_color in target_colors:
            if isColorClose(pixel_color, target_color, max_diff):
                print(f"Night detected at point {point}!")

                return True

    #print("Night not detected.")

    print("")

    return False

def findNightServer(maxWaitTime=10, alt=False):
    serverLoop = 0

    while True:
        serverLoop += 1

        url = joinRandomServer(1537690962)

        if not waitForLoading(maxWaitTime=maxWaitTime):
            continue

        click(offsetDims((1000, 500), "list"))

        time.sleep(1)

        if not detectNight():
            continue

        print("Night found!")

        sendScreenshot(f"Night server found on alt :D (attempts: {serverLoop})")

        click(offsetDims((1000, 500), "list"))

        time.sleep(0.5)

        break

    return url
