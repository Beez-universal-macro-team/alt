import customtkinter as ctk
import tkinter as tk
from functions import offsetDims, screenDims, writeFile, readFile, sendMessage
import pyautogui
import altScript
import os
import time

main_dir = os.path.dirname(os.path.abspath(__file__))

class GUI:
    def __init__(self, font="Courier"):
        self.font = font
        self.connected = False

    def initWindow(self):
        sendMessage("Started alt!")
        
        self.window = ctk.CTk()
        self.window.title("Beez Universal Macro - Alt")
        
        logo_path = os.path.join(main_dir, "basicbeeface.ico")
        self.window.iconbitmap(logo_path)
        
        self.window.geometry(f"{offsetDims(700, 'x')}x{offsetDims(350, 'y')}")
        self.window.resizable(False, False)

        self.tabControl = ctk.CTkTabview(self.window)
        self.tabControl.add(name='Join Settings')
        self.tabControl.add(name='Connecting')
        self.tabControl.add(name='Settings')
        self.tabControl.add(name='Private Servers')
        self.tabControl.add(name='Credits')

        for i in range(1, 6):
            globals()[f"self.{i}"] = 0

        self.maxLoadTime = tk.StringVar()

        self.joinTitle = ctk.CTkLabel(self.tabControl.tab('Join Settings'), text="Join Settings")
        self.joinTitle.configure(font=(self.font, 24))

        self.maxLoadText = ctk.CTkLabel(self.tabControl.tab('Join Settings'), text="Maximum load time:")
        self.maxLoadText.configure(font=(self.font, 14))

        self.maxLoad = ctk.CTkEntry(self.tabControl.tab('Join Settings'), width=40)

        try:
            self.maxLoad.insert(0, readFile("guiFiles/maxLoadTime.txt"))
        except:
            self.maxLoad.insert(0, "10")

        self.start = ctk.CTkButton(self.window, text="Start (f1)", command=self.startMacro)
        self.stop = ctk.CTkButton(self.window, text="Stop (f2)", command=self.stopMacro)

        self.connectTitle = ctk.CTkLabel(self.tabControl.tab('Connecting'), text="Connecting")
        self.connectTitle.configure(font=(self.font, 24))

        self.ipText = ctk.CTkLabel(self.tabControl.tab('Connecting'), text="Host name (found in main, connecting tab):")
        self.ipText.configure(font=(self.font, 14))

        self.ip = ctk.CTkEntry(self.tabControl.tab('Connecting'), width=120)

        try:
            self.ip.insert(0, readFile("guiFiles/hostName.txt"))
        except:
            pass

        self.portText = ctk.CTkLabel(self.tabControl.tab('Connecting'), text="Port:")
        self.portText.configure(font=(self.font, 14))

        self.port = ctk.CTkEntry(self.tabControl.tab('Connecting'), width=120)

        try:
            self.port.insert(0, readFile("guiFiles/port.txt"))
        except:
            self.port.insert(0, "")

        self.connect = ctk.CTkButton(self.tabControl.tab('Connecting'), text="Connect to main", command=self.connectToMain)

        self.settingsTitle = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Settings")
        self.settingsTitle.configure(font=(self.font, 24))

        self.webhookText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Discord webhook:")
        self.webhookText.configure(font=(self.font, 14))

        self.webhook = ctk.CTkEntry(self.tabControl.tab('Settings'), width=200)

        try:
            self.webhook.insert(0, readFile("guiFiles/webhook.txt"))
        except:
            self.webhook.insert(0, "")

        self.mode = tk.StringVar(self.tabControl.tab('Settings'))
        self.mode.set("night searcher")

        self.modeText = ctk.CTkLabel(self.tabControl.tab('Settings'), text="Mode:")
        self.modeText.configure(font=(self.font, 14))

        self.modeBox = ctk.CTkOptionMenu(self.tabControl.tab('Settings'), 
                                       values=["night searcher", "night waiter"],
                                       variable=self.mode)

        self.privateServersText = ctk.CTkLabel(self.tabControl.tab('Private Servers'), text="Private servers")
        self.privateServersText.configure(font=(self.font, 24))

        for i in range(1, 6):
            globals()[f"self.{i}"] = ctk.CTkEntry(self.tabControl.tab('Private Servers'), width=200)
            try:
                globals()[f"self.{i}"].insert(0, self.getPrivateServer(i - 1))
            except:
                pass

        self.usingPs = tk.IntVar(self.tabControl.tab('Private Servers'))
        self.usingPsBox = ctk.CTkCheckBox(self.tabControl.tab('Private Servers'), 
                                         text="Use private servers", 
                                         variable=self.usingPs)

        try:
            self.usingPs.set(1 if eval(readFile("guiFiles/joinPrivateServers.txt")) else 0)
        except:
            pass

        owner = "Beez131"
        contributors = ["Sharkboy1663", "Pirosow"]
        specialThanks = ["Slymi", "Fire_king66", "Lvl18BubbleBee"]

        self.ownerText = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Owner/Head Developer:")
        self.ownerText.configure(font=(self.font, 15))

        self.owner = ctk.CTkLabel(self.tabControl.tab('Credits'), text=owner)

        self.contributors = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Developers:")
        self.contributors.configure(font=(self.font, 15))

        for contributor in contributors:
            globals()[f"self.{contributor}"] = ctk.CTkLabel(self.tabControl.tab('Credits'), text=contributor)

        self.specialThanks = ctk.CTkLabel(self.tabControl.tab('Credits'), text="Special Thanks To:")
        self.specialThanks.configure(font=(self.font, 15))

        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"] = ctk.CTkLabel(self.tabControl.tab('Credits'), text=specialThank)

        # Pack everything
        self.tabControl.pack(expand=2, fill="both")
        
        self.joinTitle.pack(pady=10)
        self.maxLoadText.pack(pady=5)
        self.maxLoad.pack(pady=5)
        
        self.start.pack(side="left", padx=20, pady=10)
        self.stop.pack(side="right", padx=20, pady=10)
        
        self.connectTitle.pack(pady=10)
        self.ipText.pack(pady=5)
        self.ip.pack(pady=5)
        self.portText.pack(pady=5)
        self.port.pack(pady=5)
        self.connect.pack(pady=10)
        
        self.settingsTitle.pack(pady=10)
        self.webhookText.pack(pady=5)
        self.webhook.pack(pady=5)
        self.modeText.pack(pady=5)
        self.modeBox.pack(pady=5)
        
        self.privateServersText.pack(pady=10)
        for i in range(5):
            globals()[f"self.{i + 1}"].pack(pady=5)
        self.usingPsBox.pack(pady=10)
        
        self.ownerText.pack(pady=5)
        self.owner.pack(pady=2)
        self.contributors.pack(pady=5)
        for contributor in contributors:
            globals()[f"self.{contributor}"].pack(pady=2)
        self.specialThanks.pack(pady=5)
        for specialThank in specialThanks:
            globals()[f"self.{specialThank}"].pack(pady=2)

    # Rest of the methods remain the same since they handle logic rather than UI
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
        time.sleep(0.01)
        try:
            self.Alt.connectToMain()
            self.connected = True
        except:
            pass


    def saveSettings(self):
        self.maxLoadTimeChange()
        self.ipChange()
        self.webhookChange()
        self.portChange()
        self.modeChange()
        self.privateServersChange()

        self.window.after(1000, self.saveSettings
