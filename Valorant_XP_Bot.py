import pyautogui, time
from random import randint
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime


start=datetime.now()
global ingame


class bot:
    def __init__(self):
        self.exp = 0

    def lobby(self): #Checks to see if you're in the lobby. Works by searching for the "START" button.
        time.sleep(10)
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " > Waiting to detect if at menu")
        print(Style.RESET_ALL)
        while True:
            lobby = pyautogui.locateOnScreen("ImageChecks/lobby.png")
            lobby2 = pyautogui.locateOnScreen("ImageChecks/lobby.png", confidence=0.6)
            if lobby is not None or lobby2 is not None:
                print(Fore.GREEN + " Detected at menu")
                print(Style.RESET_ALL)
                if lobby != None:
                    pyautogui.click(lobby)   
                if lobby2 != None:
                    pyautogui.click(lobby2)    
                time.sleep(1)
                self.ingame()
        
    def ingame(self): #Checks to see if you're in a game. Works by seeing if the banner preview can be found.
        print(Fore.YELLOW + " > Waiting for a game")
        print(Style.RESET_ALL)
        while True:
            ingame = pyautogui.locateOnScreen(banner)
            ingame2 = pyautogui.locateOnScreen(banner, confidence=0.6)
            if ingame is not None or ingame2 is not None:
                print(Fore.GREEN + " Now in a game")
                print(Style.RESET_ALL)
                time.sleep(1)
                print(Fore.YELLOW + " > Waiting for the end of the game")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.endofthegame()

    def endofthegame(self):
        time.sleep(5)
        while True:
            compteur = pyautogui.locateOnScreen("ImageChecks/confirm2.png")
            compteur2 = pyautogui.locateOnScreen("ImageChecks/confirm2.png", confidence=0.6)
            if compteur is not None or compteur2 is not None:
                print(Fore.GREEN + " Detected that the game has ended")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.result()
            else:
                self.antiafk()

    def antiafk(self):
        time.sleep(5)
        n = randint(20, 35)
        a = 0
        while a <= n:
            a += 1
            n2 = randint(1,6)
            if n2 == 1:
                pyautogui.keyDown('w')
                sleep(randint(2, 6)/10)
            if n2 == 2:
                pyautogui.keyUp('w')
                pyautogui.keyDown('d')
                pyautogui.click()
            if n2 == 3:
                pyautogui.keyDown('a')
                sleep(randint(1, 3)/10)
                pyautogui.keyDown('a')
                pyautogui.click()
                sleep(randint(2, 4)/10)
            if n2 == 4:
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                sleep(randint(2, 5)/10)
            if n2 == 5:
                pyautogui.keyUp('s')
                sleep(randint(4, 6)/10)
            if n2 == 6:
                pyautogui.keyDown('w')
                sleep(randint(2, 4)/10)
                pyautogui.keyUp('w')

        self.endofthegame()

    def result(self):
        print(Fore.YELLOW + " > Waiting for the XP screen")
        print(Style.RESET_ALL)
        time.sleep(10)
        while True:
            results = pyautogui.locateOnScreen("ImageChecks/confirm.png")
            results2 = pyautogui.locateOnScreen("ImageChecks/confirm.png", confidence=0.6)
            if results is not None or results2 is not None:
                print(Fore.GREEN + " XP screen detected")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.exp += 900
                print(Fore.MAGENTA + " Earned", self.exp, "XP in total.")
                print(Fore.MAGENTA + " Running for",datetime.now()-start)
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print(Style.RESET_ALL)
                time.sleep(2)
                pyautogui.click(x=980, y=30)
                time.sleep(2)
                self.lobby()          

a = bot()

def main():

    from colorama import init
    from colorama import Fore, Back, Style
    init()
    print (Fore.RED + """
 __      __   _                       _     __   __        ____        _   
 \ \    / /  | |                     | |    \ \ / /       |  _ \      | |  
  \ \  / /_ _| | ___  _ __ __ _ _ __ | |_    \ V / _ __   | |_) | ___ | |_ 
   \ \/ / _` | |/ _ \| '__/ _` | '_ \| __|    > < | '_ \  |  _ < / _ \| __|
    \  / (_| | | (_) | | | (_| | | | | |_    / . \| |_) | | |_) | (_) | |_ 
     \/ \__,_|_|\___/|_|  \__,_|_| |_|\__|  /_/ \_\ .__/  |____/ \___/ \__|
                                                  | |                      
                                                  |_|                      """)
    print(Style.RESET_ALL)


    print(Style.RESET_ALL)
    print("")
    print(Fore.RED + "                               by Fums, WolfAnto and jordan123pal")
    print("")
    print(Style.BRIGHT + Fore.RED + "                               Use this bot in Deathmatch only.")
    print ("")
    print(Style.RESET_ALL)
    
    time.sleep(1/2)
    print("")
    print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(Style.RESET_ALL)
    time.sleep(1/2)
    print (Style.BRIGHT + Fore.RED)
    print(Fore.WHITE+" 1)",Fore.YELLOW+"Launch Bot")
    print("")
    print(Fore.WHITE+" 2)",Fore.YELLOW+"Exit Bot")
    print("")
    print(Fore.WHITE+" 3)",Fore.YELLOW+"Help + Information")
    print("")
    print(Style.BRIGHT + Fore.RED+"")
    menu = int(input(" > "))
    
    try:
        if menu == 1:
            print ("")
            print(Style.RESET_ALL,Fore.YELLOW+"Please select a banner and equip that EXACT one in game (BETA is recommended): ")
            print ("")
            print (Style.BRIGHT,Fore.WHITE+"1)",Fore.YELLOW+"Beta Pioneer Banner")
            print("")
            print (Fore.WHITE+" 2)",Fore.YELLOW+"Valorant Card Banner",Style.RESET_ALL,)
            print ("")
            print (Fore.WHITE+" 3)",Fore.WHITE+"Return to Menu")
            print ("")
            print(Style.BRIGHT + Fore.RED+"")
            banneroption = int(input(" > "))
            try:
                global banner
                if banneroption == 1:
                    banner = ("ImageChecks/1.png")
                    print (Style.RESET_ALL)
                    print (Fore.RED+" Selected the Beta Pioneer Banner")
                elif banneroption == 2:
                    banner = ("ImageChecks/2.png")
                    print (Style.RESET_ALL)
                    print (Fore.RED+" Selected the Valorant Card Banner")
                elif banneroption == 3:
                    main()
                else:
                    print (Fore.RED+" Error 1: Enter a valid integer within the range 1 - 3!")
                    time.sleep(2)
                    main()
            except ValueError:
                print (" Error 2: You must enter an integer!")
                time.sleep(2)
                main()
            
            print (Style.RESET_ALL)
            time.sleep(2)
            print(Fore.WHITE + " 1)",Fore.CYAN +"Make sure Valorant is focused and click",Fore.BLUE +"PLAY",Fore.CYAN +"and then click",Fore.BLUE+"DEATHMATCH", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"Wait around",Fore.BLUE +"10 seconds",Fore.CYAN +"and do not click anything", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"Let the bot do the rest!", Style.RESET_ALL)
            print ("")
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print("")
            time.sleep(5)
            a.lobby()

        elif menu == 2:
            print(" Thank you for using the bot. See you later!")
            print(" ")
            time.sleep(2)
            quit()

        elif menu == 3:
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.RESET_ALL+"")
            
            print(Fore.RED + " HOW TO RUN THE BOT")
            print("")
            print(Fore.WHITE + " 1)",Fore.CYAN +"Open Valorant and click",Fore.BLUE +"PLAY",Fore.CYAN +"and then click",Fore.BLUE+"DEATHMATCH", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"Run the bot by selecting",Fore.BLUE +"1",Fore.CYAN +"in the main menu")
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"Change your player banner to either")
            print(Fore.BLUE +" Beta Pioneer Banner",Fore.CYAN +"or the",Fore.BLUE +"Valorant Card Banner",Fore.CYAN)
            print("")
            print(Fore.WHITE + " 4)",Fore.CYAN +"Select the banner you have selected in the",Fore.BLUE +"bot console",Fore.CYAN)
            print(Fore.CYAN +" You will be reminded of the next set of instructions again")
            print("")
            print(Fore.WHITE + " 5)",Fore.CYAN +"Let the game run and try not to touch your mouse / allow anything")
            print(Fore.CYAN +" to interrupt the process")
            print("")
            print(Fore.CYAN +" If you wish to stop the bot",Fore.BLUE +"simply close this window",Fore.CYAN)
            print("")
            print("")
            print(Fore.RED + " OTHER PRECAUTIONS AND INFORMATION")
            print("")
            print(Fore.CYAN +" This code is not optimised very well")
            print(Fore.CYAN +" It may stutter or crash if used for a large amount of time")
            print(Fore.CYAN +" XP gain is quite slow. This is due to the Deathmatch queue")
            print(Fore.CYAN +" If you can't find a game, change servers")
            print(Fore.CYAN +" It is advised to turn the Name Hide option on in",Fore.BLUE +"Settings > Privacy",Fore.CYAN)
            print("")
            print("") 
            print(Fore.RED + " XP GAIN")
            print("")
            print(Fore.CYAN +" Minimum XP gain are as follows")
            print(Fore.WHITE +" 1 hour:",Fore.MAGENTA +"3,600 XP")
            print(Fore.WHITE +" 8 hours:",Fore.MAGENTA +"28,800 XP")
            print(Fore.WHITE +" 24 hours:",Fore.MAGENTA +"86,400 XP")
            
            
            print("")
            print("")
            print(Fore.RED + " CREDITS AND CONTACT")
            print("")
            print(Fore.CYAN +" Base code originally written by",Fore.BLUE +"jordan123pal",Fore.CYAN +"and heavily edited by",Fore.BLUE +"WolfAnto",Fore.CYAN +"and",Fore.BLUE +"Fums",Fore.CYAN +"to work with Valorant")
            print(Fore.CYAN +" This version of the bot is maintained by",Fore.BLUE +"Fums")
            print(Fore.BLUE +" Discord :",Fore.YELLOW+ "Fums#0888",Fore.CYAN+ "| ",Fore.BLUE + "Github :",Fore.YELLOW+ "https://github.com/MrFums",Style.RESET_ALL)
            print("")
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.BRIGHT,Fore.RED)
            print("")
            print(" Input anything to return to the menu...")
            print(Style.RESET_ALL+"")
            print ("")
            menureturn = input(" > ")
            main()
                
                
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            time.sleep(30)
            main()
        else:
            print (" Error 1: Enter a valid integer within the range 1 - 3!")
            time.sleep(2)
            main()
    except ValueError:
        print (" Error 2: You must enter an integer!")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
