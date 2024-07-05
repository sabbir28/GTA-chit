import pyautogui
import time
from tkinter import *
from threading import Thread
import keyboard as kb

BG = "black"
FG = "green"
RD = "blue"

OPEN = "ctrl+a+f1"
CLOSE = "ctrl+a+f2"
General_Cheats = "ctrl+a+p"
Weapons_O = "ctrl+a+o"
Weapons_L = "ctrl+a+l"
Weapons_K = "ctrl+a+k"
police = "ctrl+a+i"

Vehicle_1 = "ctrl+a+z"
Vehicle_2 = "ctrl+a+x"
Vehicle_3 = "ctrl+a+c"
Vehicle_4 = "ctrl+a+v"
Vehicle_5 = "ctrl+a+b"
Vehicle_6 = "ctrl+a+g"
Vehicle_7 = "ctrl+a+h"
Vehicle_8 = "ctrl+a+j"
Vehicle_9 = "ctrl+a+t"
Vehicle_0 = "ctrl+a+r"

class ModMenu():
    def __init__(self, window_title, width, height):
        self.win = Tk()
        x, y = self.center(width, height)
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        self.win.overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        self.win.wm_attributes("-alpha", 0.7)
        self.win.configure(background=BG)
        
        self.mainWindow()

    def mainWindow(self):
        labels_data = [
            ("GTA VICE CITY", ('Arial', 16), BG, FG, 140, 20),
            ("Cheat", ('Arial', 12), BG, RD, 30, 60),
            ("Keays", ('Arial', 12), BG, RD, 250, 60),
            (" ", ('Arial', 10), BG, RD, 10, 80),
            ("Full Health", ('Arial', 12), BG, FG, 30, 100),
            ("P,N", ('Arial', 12), BG, FG, 250, 100),
            ("Weapons", ('Arial', 12), BG, FG, 30, 130),
            ("O,L,K", ('Arial', 12), BG, FG, 250, 130),
            ("Police", ('Arial', 12), BG, FG, 30, 160),
            ("I,#", ('Arial', 12), BG, FG, 250, 160),
            ("Vehicle Cheats", ('Arial', 12), BG, FG, 30, 190),
            ("Z,X,C,V,B,G,H,J,T,R", ('Arial', 12), BG, FG, 250, 190),
            ("Vehicle Skill", ('Arial', 12), BG, FG, 30, 220),
            ("Y", ('Arial', 12), BG, FG, 250, 220),
            ("Vehicle Flay", ('Arial', 12), BG, FG, 30, 250),
            ("F", ('Arial', 12), BG, FG, 250, 250),
            ("Hide", ('Arial', 12), BG, FG, 30, 280),
            ("F1", ('Arial', 12), BG, FG, 250, 280),
            ("EXIT", ('Arial', 12), BG, FG, 30, 310),
            ("F2", ('Arial', 12), BG, FG, 250, 310)
        ]

        for text, font, bg, fg, x, y in labels_data:
            label = Label(self.win, text=text, font=font, bg=bg, fg=fg)
            label.place(x=x, y=y)

    def center(self, width, height):
        swidth = self.win.winfo_screenwidth()
        sheight = self.win.winfo_screenheight()
        x = (swidth / 2) - (width / 2)
        y = (sheight / 2) - (height / 2)
        return int(x), int(y)

def keybinds(modmenu):
    isopen = True
    while True:
        if kb.is_pressed('#'):
            pyautogui.write("YOUWONTTAKEMEALIVE")
        
        if kb.is_pressed('y'):
            pyautogui.write("GRIPISEVERYTHING")
            time.sleep(0.1)
            pyautogui.write("SEAWAYS")
            time.sleep(0.1)

        if kb.is_pressed('f'):
            pyautogui.write("AIRSHIP")
            time.sleep(0.1)

        if kb.is_pressed(General_Cheats):
            pyautogui.write("ASPIRINE")
            pyautogui.write("PRECIOUSPROTECTION")

        if kb.is_pressed('n'):
            pyautogui.write("youcantleavemealone")

        if kb.is_pressed(Vehicle_0):
            pyautogui.write("BETTERTHANWALKING")
        
        if kb.is_pressed(Vehicle_1):
            pyautogui.write("RUBBISHCAR")
        
        if kb.is_pressed(Vehicle_3):
            pyautogui.write("ROCKANDROLLCAR")
        
        if kb.is_pressed(Vehicle_4):
            pyautogui.write("THELASTRIDE")
        
        if kb.is_pressed(Vehicle_5):
            pyautogui.write("GETTHEREAMAZINGLYFAST")
        
        if kb.is_pressed(Vehicle_6):
            pyautogui.write("GETTHEREVERYFASTINDEED")
        
        if kb.is_pressed(Vehicle_7):
            pyautogui.write("GETTHEREFAST")
        
        if kb.is_pressed(Vehicle_8):
            pyautogui.write("GETTHEREQUICKLY")
        
        if kb.is_pressed(Vehicle_9):
            pyautogui.write("PANZER")

        if kb.is_pressed(Weapons_O):
            pyautogui.write("THUGSTOOLS")
            
        if kb.is_pressed(Weapons_L):
            pyautogui.write("PROFESSIONALTOOLS")

        if kb.is_pressed(Weapons_K):
            pyautogui.write("NUTTERTOOLS")
        
        if kb.is_pressed(police):
            pyautogui.write("LEAVEMEALONE")

        if kb.is_pressed(CLOSE):
            modmenu.win.destroy()

        if kb.is_pressed(OPEN):
            if isopen:
                modmenu.win.withdraw()
                isopen = False
            else:
                modmenu.win.deiconify()
                isopen = True
            time.sleep(0.5)

modmenu = ModMenu("GTA VICE CITY", 400, 400)

keybinds_thread = Thread(target=keybinds, args=(modmenu,))
keybinds_thread.setDaemon(True)
keybinds_thread.start()

modmenu.win.mainloop()
