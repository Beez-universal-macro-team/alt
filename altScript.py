import socket
from fontTools.misc.textTools import tobytes
from searchNightServer import findNightServer, detectNight
from randomServer import joinRandomServer
from functions import sendMessage, readFile, click, offsetDims, sendScreenshot
import time

class Alt:
    def __init__(self, ip, port, maxLoadTime):
        self.maxLoadTime = maxLoadTime
        self.ip = ip
        self.port = port
        self.tcpsocket = 0

    def connectToMain(self, delay=0):
        time.sleep(delay)
        tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcpsocket.connect((self.ip, self.port))

        self.tcpsocket = tcpsocket

    def sendToMain(self, url):
        self.tcpsocket.send(tobytes(url))

    def searchForNight(self):
        mode = readFile("guiFiles/mode.txt")

        if mode == "night searcher":
            while True:
                url = findNightServer(maxWaitTime=int(readFile("guiFiles/maxLoadTime.txt")), alt=True)

                sendScreenshot("Night found on alt!")

                try:
                    self.sendToMain(url)
                    sendMessage("message sent!")

                except:
                    sendMessage("Alt disconnected. Reconnecting...")

                    self.connectToMain(delay=10)

        else:
            url = joinRandomServer(1537690962)

            night = False

            while True:
                click(offsetDims((1000, 500), "list"))

                if not detectNight():
                    night = False

                    continue

                if night:
                    continue

                night = True

                print("Night found!")

                sendScreenshot("Night found on alt!")

                try:
                    self.sendToMain(url)

                except:
                    sendMessage("Alt disconnected. Reconnecting...")

                    self.connectToMain(delay=10)

            time.sleep(1)
