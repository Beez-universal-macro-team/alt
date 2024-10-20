import tkinter as tk
from functions import offsetDims, screenDims, writeFile, readFile, sendMessage
import pyautogui
import altScript
import os

main_dir = os.path.dirname(os.path.abspath(__file__))

class GUI:
    def __init__(self, font="Courier"):
        self.font = font

        self.connected = False

    def initWindow(self):
        sendMessage("Started alt!")
        
        self.window = tk.Tk()

        self.window.title("Beez Universal Macro - Alt")

        # Set the GUI logo
        logo_path = os.path.join(main_dir, "basicbeeface.ico")
        self.window.iconbitmap(logo_path)
        
        self.window.geometry(f"{offsetDims(700, 'x')}x{offsetDims(350, 'y')}")

        self.window.resizable(False, False) #Locks GUI size

        ###### CREATING TABS ######

        self.tabControl = tk.ttk.Notebook(self.window)

        self.joinSettingsTab = tk.ttk.Frame(self.tabControl)
        self.connectTab = tk.ttk.Frame(self.tabControl)
        self.settingsTab = tk.ttk.Frame(self.tabControl)
        self.privateServersTab = tk.ttk.Frame(self.tabControl)
        self.creditsTab = tk.ttk.Frame(self.tabControl)

        self.tabControl.add(self.joinSettingsTab, text='Join Settings')
        self.tabControl.add(self.connectTab, text='Connecting')
        self.tabControl.add(self.settingsTab, text='Settings')
        self.tabControl.add(self.privateServersTab, text='Private Servers')
        self.tabControl.add(self.creditsTab, text='Credits')

        ###### CREATING TEXT ######

        for i in range(1, 6):
            globals()[f"self.{i}"] = 0

        self.maxLoadTime = tk.StringVar()

        self.joinTitle = tk.Label(self.joinSettingsTab, text="Join Settings")
        self.joinTitle.config(font=(self.font, 17))

        self.maxLoadText = tk.Label(self.joinSettingsTab, text="Maximum load time:")
        self.maxLoadText.config(font=(self.font, 14))

        self.maxLoad = tk.Entry(self.joinSettingsTab, width=3)

        try:
            self.maxLoad.insert(0, readFile("guiFiles/maxLoadTime.txt"))
        except:
            self.maxLoad.insert(0, "10")

        self.start = tk.Button(self.window, text="Start (f1)", command=self.startMacro)
        self.stop = tk.Button(self.window, text="Stop (f2)", command=self.stopMacro)

        self.connectTitle = tk.Label(self.connectTab, text="Connecting")
        self.connectTitle.config(font=(self.font, 17))

        self.ipText = tk.Label(self.connectTab, text="Host name (found in main, settings tab):")
        self.ipText.config(font=(self.font, 14))

        self.ip = tk.Entry(self.connectTab, width=10)

        try:
            self.ip.insert(0, readFile("guiFiles/hostName.txt"))
        except:
            pass

        self.portText = tk.Label(self.connectTab, text="Port:")
        self.portText.config(font=(self.font, 14))

        self.port = tk.Entry(self.connectTab, width=10)

        try:
            self.port.insert(0, readFile("guiFiles/port.txt"))
        except:
            self.port.insert(0, "")

        self.connect = tk.Button(self.connectTab, text="Connect to main", command=self.connectToMain)

        self.settingsTitle = tk.Label(self.settingsTab, text="Settings")
        self.settingsTitle.config(font=(self.font, 17))

        self.webhookText = tk.Label(self.settingsTab, text="Discord webhook:")
        self.webhookText.config(font=(self.font, 14))

        self.webhook = tk.Entry(self.settingsTab, width=10)

        try:
            self.webhook.insert(0, readFile("guiFiles/webhook.txt"))
        except:
            self.webhook.insert(0, "")

        self.mode = tk.StringVar(self.settingsTab)
        self.mode.set("night searcher")

        self.modeText = tk.Label(self.settingsTab, text="Mode:")
        self.modeText.config(font=(self.font, 14))

        self.modeBox = tk.OptionMenu(self.settingsTab, self.mode, *["night searcher", "night waiter"])

        self.privateServersText = tk.Label(self.privateServersTab, text="Private servers")
        self.privateServersText.config(font=(self.font, 14))

        for i in range(1, 6):
            globals()[f"self.{i}"] = tk.Entry(self.privateServersTab)

            try:
                globals()[f"self.{i}"].insert(0, self.getPrivateServer(i - 1))

            except:
                pass

        self.usingPs = tk.IntVar(self.privateServersTab)

        self.usingPsBox = tk.Checkbutton(self.privateServersTab, text="Use private servers", variable=self.usingPs, onvalue=1, offvalue=0)

        try:
            self.usingPs.set(1 if eval(readFile("guiFiles/joinPrivateServers.txt")) else 0)

        except:
            pass

        owner = "Beez131"

        contributors = [
            "Sharkboy1663",
            "Pirosow"
        ]

        specialThanks = [
            "Slymi",
            "_epic",
            "Fire_king66",
        ]

        self.ownerText = tk.Label(self.creditsTab, text="Owner:")
        self.ownerText.config(font=(self.font, 15))

        self.owner = tk.Label(self.creditsTab, text=owner)

        self.contributors = tk.Label(self.creditsTab, text="Developpers:")
        self.contributors.config(font=(self.font, 15))

        for contributor in contributors:
            globals()[f"self.{contributor}"] = tk.Label(self.creditsTab, text=contributor)

        self.specialThanks = tk.Label(self.creditsTab, text="Special Thanks To:")
        self.specialThanks.config(font=(self.font, 15))

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"] = tk.Label(self.creditsTab, text=specialThank)

        ###### DISPLAYING TEXT ######

        self.tabControl.pack(expand=2, fill="both")

        self.joinTitle.pack()

        self.maxLoadText.pack()
        self.maxLoad.pack()

        self.maxLoadText.place(relx=0.5, rely=0.35, anchor="n")
        self.maxLoad.place(relx=0.5, rely=0.5, anchor="n")

        self.start.pack()
        self.start.place(relx=0.35, rely=0.8, anchor="n")

        self.stop.pack()
        self.stop.place(relx=0.65, rely=0.8, anchor="n")

        self.connectTitle.pack()

        self.ipText.pack()
        self.ip.pack()

        self.portText.pack()
        self.port.pack()

        self.connect.pack()

        self.settingsTitle.pack()

        self.webhookText.pack()
        self.webhook.pack()

        self.modeText.pack()
        self.modeBox.pack()

        self.modeText.place(relx="0.5", rely="0.45", anchor="n")
        self.modeBox.place(relx="0.5", rely="0.6", anchor="n")

        self.privateServersText.pack()

        for i in range(5):
            globals()[f"self.{i + 1}"].pack()

        self.usingPsBox.pack()

        self.ownerText.pack()
        self.owner.pack()

        self.contributors.pack()

        for contributor in contributors:
            globals()[f"self.{contributor}"].pack()

        self.specialThanks.pack()

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"].pack()

        self.window.attributes("-topmost", False)

    def maxLoadTimeChange(self):
        tm = self.maxLoad.get()

        if str(tm).isnumeric():
            writeFile("guiFiles/maxLoadTime.txt", tm)

        else:
            pyautogui.alert("Make sure to set max load time to a number!")

    def ipChange(self):
        ip = self.ip.get()

        writeFile("guiFiles/hostName.txt", ip)

    def webhookChange(self):
        webhook = self.webhook.get()

        writeFile("guiFiles/webhook.txt", webhook)

    def portChange(self):
        port = self.port.get()

        writeFile("guiFiles/port.txt", port)

    def modeChange(self):
        mode = self.mode.get()

        writeFile("guiFiles/mode.txt", mode)

    def privateServersChange(self):
        privateServers = []

        for i in range(5):
            privateServer = globals()[f"self.{i + 1}"].get()

            privateServers.append(privateServer)

        writeFile("guiFiles/privateServers.txt", str(privateServers))
        writeFile("guiFiles/joinPrivateServers.txt", True if self.usingPs.get() else False)

    def getPrivateServer(self, n):
        privateServers = eval(readFile("guiFiles/privateServers.txt"))

        return privateServers[n]

    def startMacro(self, main=False):
        self.maxLoadTimeChange()
        self.ipChange()
        self.webhookChange()
        self.portChange()
        self.modeChange()
        self.privateServersChange()

        if self.connected:
            self.Alt.searchForNight()

        elif not main:
            pyautogui.alert("Dont forget to connect to main! (connecting tab)")


    def stopMacro(self):
        quit()

    def connectToMain(self):
        self.Alt = altScript.Alt(self.ip.get(), int(self.port.get()), int(self.maxLoad.get()))

        try:
            self.Alt.connectToMain()

            self.connected = True

        except:
            pyautogui.alert("Make sure to press connect on main first!")
