"""
Grand Theft Auto - Vice City Extreme

Cheat                        Result 
-----------------------------------
General Cheats             
==============        
THUGSTOOLS                 - All Level1 Weapons 
PROFESSIONALTOOLS          - All Level2 Weapons  
NUTTERTOOLS                - All Level3 Weapons 
ASPIRINE                   - Full Health 
PRECIOUSPROTECTION         - Full Armor 
FANNYMAGNET                - Ladies Magnet (women follow you) 
YOUWONTTAKEMEALIVE         - Higher Wanted Level  
LEAVEMEALONE               - No Wanted Level 
ICANTTAKEITANYMORE         - Commit Suicide 
youcantleavemealone        - can't die
fullcitypeoplemines        - buy full city
freewayforangeljoy         - Get 100 bikes
americahelicopter          - get ahunter helicopter
flyingways                 - get a aeroplane dodo or kimo
DEMONSPEED                 - makes faster the whole city including Tommy
leavemealone               - No Police

Character Skin Cheats
=====================     
DEEPFRIEDMARSBARS          - Fat Body 
PROGRAMMER                 - Skinny arms and legs 
STILLLIKEDRESSINGUP        - Random Change of Clothes 
CERTAINDEATH               - Smoke a cigarette 
CHEATSHAVEBEENCRACKED      - Play as Ricardo Diaz 
LOOKLIKELANCE              - Play as Lance Vance 
MYSONISALAWYER             - Play as Ken Rosenberg 
LOOKLIKEHILARY             - Play as Hilary King 
ROCKANDROLLMAN             - Play as Love Fist character Jezz Torent 
WELOVEOURDICK              - Play as Love Fist character Dick 
ONEARMEDBANDIT             - Play as Phil Cassidy.  
IDONTHAVETHEMONEYSONNY     - Play as Sonny Forelli.  
FOXYLITTLETHING            - Play as Mercedes 

Vehicle Spawn Cheats  
====================   
PANZER                     - Spawns a Rhino 
TRAVELINSTYLE              - Spawns a Bloodring Banger  
GETTHEREQUICKLY            - Spawns Bloodring Banger#2  
GETTHEREFAST               - Spawns a Sabre Turbo  
GETTHEREVERYFASTINDEED     - Spawns a Hotring Racer  
GETTHEREAMAZINGLYFAST      - Spawns Hotring Racer#2  
THELASTRIDE                - Spawns a Romero's Hearse  
ROCKANDROLLCAR             - Spawns Love Fist's Limo 
RUBBISHCAR                 - Spawns a Trashmaster 
BETTERTHANWALKING          - Spawns a Caddie 

Vehicle Cheats 
============== 
Update by: CyberWolf

AIRSHIP                    - Ships have flying ability 
BIGBANG                    - Blows up all nearby vehicles 
MIAMITRAFFIC               - Aggressive Traffic  
AHAIRDRESSERSCAR           - All Pink Vehicles 
IWANTITPAINTEDBLACK        - All Black Vehicles 
COMEFLYWITHME              - Vehicles have flying ability 
GRIPISEVERYTHING           - Better Vehicle Handling 
GREENLIGHT                 - All Traffic Lights are green 
SEAWAYS                    - Vehicles drive on water 
WHEELSAREALLINEED          - Makes only vehicle wheels visible 
LOADSOFLITTLETHINGS        - Sportscars have bigger wheels 

Weather Cheats 
==============     
ALOVELYDAY                 - Clear Weather 
APLEASANTDAY               - Lightly Clouded 
ABITDRIEG                  - Dense Clouds 
CANTSEEATHING              - Foggy Weather 
CATSANDDOGS                - Stormy Weather 

Miscellaneous Cheats  
====================    
LIFEISPASSINGMEBY          - Speeds up Game Clock  
ONSPEED                    - Makes everything faster  
BOOOOOORING                - Makes everything slower  
FIGHTFIGHTFIGHT            - Aggressive Pedestrians  
NOBODYLIKESME              - Everybody wants to kill you 
OURGODGIVENRIGHTTOBEARARMS - Pedestrians carry weapons 
CHICKSWITHGUNS             - Only Female Peds carry weapons 
CHASESTAT                  - Shows Media Level  

"""

BG = "green"
FG = "black"

import pyautogui
import keyboard
import time
#pip install pymem
#pip install keyboard
from tkinter import *
from settings import *
import keyboard as kb
from threading import Thread
from time import sleep

CARENT_WENDOW = "main"

class ModMenu():
    def __init__(self, window_title, width, height):
        self.win = Tk()
        x, y = self.center(width, height)
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        self.win.overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        self.win.wm_attributes("-alpha", 0.7)
        self.win.configure(background=BG)

        #self.title_label.pack()

        #self.ammo_btn1 = Button(self.win, text="General Cheats", font=('Arial',12), bg=BG, fg=FG, command=self.ammo_hack)
        #self.ammo_btn1.place(x=30,y=60)

        self.mainWindow()

    
    def mainWindow(self):
        self.title_label = Label(self.win, text="GTA VICE CITY", font=('Arial',16), bg=BG, fg=FG)
        self.title_label.place(x=140,y=20)


        self.title_label = Label(self.win, text="Cheat", font=('Arial',12), bg=BG, fg=RD)
        self.title_label.place(x=30,y=60)

        self.title_label = Label(self.win, text="Keays", font=('Arial',12), bg=BG, fg=RD)
        self.title_label.place(x=250,y=60)

        self.title_label = Label(self.win, text="===========================SABBIR=======================", font=('Arial',10), bg=BG, fg=RD)
        self.title_label.place(x=10,y=80)

        self.title_label = Label(self.win, text="Full Health", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=100)

        self.title_label = Label(self.win, text="P,N", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=100)

        self.title_label = Label(self.win, text="Weapons", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=130)

        self.title_label = Label(self.win, text="O,L,K", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=130)

        self.title_label = Label(self.win, text="Police", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=160)

        self.title_label = Label(self.win, text="I,#", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=160)

        self.title_label = Label(self.win, text="Vehicle Cheats", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=190)

        self.title_label = Label(self.win, text="Z,X,C,V,B,G,H,J,T,R", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=190)

        self.title_label = Label(self.win, text="Vehicle Skill", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=220)

        self.title_label = Label(self.win, text="Y", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=220)

        self.title_label = Label(self.win, text="Vehicle Flay", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=250)

        self.title_label = Label(self.win, text="F", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=250)

        #self.exit_btn = Button(self.win, text="Exit(F2)", font=('Arial',14), bg=BG, fg=FG, command=self.win.destroy)
        #self.exit_btn.place(x=180,y=300)

        self.title_label = Label(self.win, text="Hide", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=280)

        self.title_label = Label(self.win, text="F1", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=280)

        self.title_label = Label(self.win, text="EXIT", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=30,y=310)

        self.title_label = Label(self.win, text="F2", font=('Arial',12), bg=BG, fg=FG)
        self.title_label.place(x=250,y=310)
        
        return CARENT_WENDOW == "main"

        

    def center(self, width, height):
        swidth = self.win.winfo_screenwidth()
        sheight = self.win.winfo_screenheight()
        #swidth = 640
        #sheight = 480
        x = (swidth/2) - (width/2)
        y = (sheight/2) - (height/2)
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
            if isopen == True:
                modmenu.win.withdraw()
                isopen = False
            else:
                modmenu.win.deiconify()
                isopen = True
                #modmenu.win.focus_force()
            sleep(0.5)



modmenu = ModMenu("GTA VICE CITY", 400, 400)

keybinds_thread = Thread(target=keybinds, args=(modmenu,))
keybinds_thread.setDaemon(True)
keybinds_thread.start()

modmenu.win.mainloop()
