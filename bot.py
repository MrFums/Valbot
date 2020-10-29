import pyautogui, time, os, winshell, psutil
from random import randint
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime
from win32com.client import Dispatch
from discord_webhook import DiscordWebhook, DiscordEmbed

#---------------------------------------------------------------


start=datetime.now()
banner = "images/1.png" #this is a fail safe
pyautogui.FAILSAFE = False

class bot:
    def __init__(self):
        self.xpamount = 0
        self.restarted = 0
        self.gamesplayed = 0
    
    
    
    def valorantrunning(self):
        found = False
        print(Fore.YELLOW,"[-] Detecting if Valorant is running")
        print(Style.RESET_ALL)
        time.sleep(2)

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                
        if found == False:
            print(Fore.RED,"[!] Can not find Valorant running")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print (Fore.GREEN,"[√] Found Valorant running")
            time.sleep(2)
            self.playbutton()
    
    def startvalorant(self):
        
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                proc.kill()
                print (Fore.YELLOW,"[-] Killing Valorant process")
                time.sleep(10)
        
        print(Fore.YELLOW,"[-] Restarting Valorant")
        print(Style.RESET_ALL)
        os.startfile("Valorant.lnk")
        time.sleep(8)
        self.restarted += 1
        self.valorantrunning()
    
        
    def playbutton(self):
        
        now = time.time()
        
        future = now + 300
        
        print(Fore.YELLOW+" [-] Waiting for play button")
        while True:
            
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            play = pyautogui.locateOnScreen("images/play.png",grayscale = True)
            play2 = pyautogui.locateOnScreen("images/play.png", confidence=0.6,grayscale = True)

            
            if play is not None or play2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected play button")
                
                if play != None:
                    pyautogui.click(play)
                    time.sleep(1)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(play)
                    self.dmatch()
                    
                if play2 != None:
                    pyautogui.click(play2)
                    time.sleep(1)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(play2)
                    self.dmatch()
                
            
    
                
                
    def dmatch(self):
        
        print(Style.RESET_ALL)
        print(Fore.YELLOW,"[-] Searching for deathmatch button")
    
    
        time.sleep(1)
        now = time.time()
        
        future = now + 120
    
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
        
            deathmatch = pyautogui.locateOnScreen("images/deathmatch.png",grayscale = True)
            deathmatch2 = pyautogui.locateOnScreen("images/deathmatch.png", confidence=0.6,grayscale = True)
                
            
            
            if deathmatch is not None or deathmatch2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected deathmatch button")
                
                if deathmatch != None:
                    pyautogui.click(deathmatch)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(deathmatch)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(deathmatch)
                    self.lobby()                    
                    
                if deathmatch2 != None:
                    pyautogui.click(deathmatch2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(deathmatch2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(deathmatch2)
                    self.lobby()
                
                time.sleep(5)
            
    
    
    def skipbutton(self):
                    
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Detecting a skip button")
        time.sleep(8)
        now = time.time()
        
        future = now + 30
        
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            
            skip = pyautogui.locateOnScreen("images/skip.png",grayscale = True)
            skip2 = pyautogui.locateOnScreen("images/skip.png",grayscale = True,confidence=0.6)  
            

            
            if skip is not None or skip2 is not None:
                
                if skip is not None:
                
                    print(Style.RESET_ALL)
                    print(Fore.RED+" [!] Detected a skip button")
                    time.sleep(1)
                    pyautogui.click(skip)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip)
                    
                    self.playagain()
                    
                if skip2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.RED+" [!] Detected a skip button")
                    time.sleep(1)
                    pyautogui.click(skip2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip2)
                    
                    
                    self.playagain()
                
            if skip is None or skip2 is None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected no skip button")
                time.sleep(1)
            
                self.playagain()





    def playagain(self):
        time.sleep(1)
        now = time.time()
        
        future = now + 780
        
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Waiting for play again button")
        while True:
            
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            playagain = pyautogui.locateOnScreen("images/playagain.png",grayscale = True)
            playagain2 = pyautogui.locateOnScreen("images/playagain.png", confidence=0.6,grayscale = True)
            
            
            if playagain is not None or playagain2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected play again button")
                    
                    
                if playagain != None:
                    pyautogui.click(playagain)
                    self.inqueue2()
                    
                    
                if playagain2 != None:
                    pyautogui.click(playagain2)
                    self.inqueue2()
    
    def firststart(self):
        
        print(Style.RESET_ALL)
        print(Fore.RED,Style.BRIGHT+"[!] Bot will start in 10 seconds. Make sure you are in the menu.")
        print(Style.RESET_ALL)
        time.sleep(10)
        
        self.playbutton()
        
        
    def lobby(self):
        
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Waiting for menu")
        
        
        
        now = time.time()
        
        future = now + 120
        
        while True:
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            lobby = pyautogui.locateOnScreen("images/lobby.png",grayscale = True)
            lobby2 = pyautogui.locateOnScreen("images/lobby.png", confidence=0.6,grayscale = True)

            again = pyautogui.locateOnScreen("images/playagain.png",grayscale = True)
            again2 = pyautogui.locateOnScreen("images/playagain.png", confidence=0.6,grayscale = True)
        

            
            if lobby is not None or lobby2 is not None or again is not None or again2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected at menu")
                
                if lobby != None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(lobby)
                    self.inqueue()
                    
                
                if lobby2 != None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(lobby2)
                    self.inqueue()
                    
                if again != None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(again2)
                    self.inqueue()
                    
                if again2 != None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(again2)
                    self.inqueue()
                
                
        
    def inqueue(self):
        
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Detecting if in queue")
        time.sleep(.1)
        now = time.time()
        
        future = now + 660
        
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            
            q = pyautogui.locateOnScreen("images/inqueue.png",grayscale = True)  
            q2 = pyautogui.locateOnScreen("images/inqueue.png",grayscale = True,confidence=0.6)  

            
            if q is not None or q2 is not None:
                if q is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN+" [√] Detected in queue")
                    time.sleep(1)
                    self.game()
                if q2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN+" [√] Detected in queue")
                    time.sleep(1)
                    self.game()
            
            if q is None:
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Detected not in queue")
                time.sleep(1)
            
                self.lobby()
                
                
    def inqueue2(self):
            
            print(Style.RESET_ALL)
            print(Fore.YELLOW+" [-] Detecting if in queue after game")
            time.sleep(.2)
            now = time.time()
            
            future = now + 660
            
            while True:
                
                if time.time() > future:
                    #detects possible issue with valorant and restarts the game
                    print(Style.RESET_ALL)
                    print(Fore.RED+" [!] Found a possible error with Valorant.")
                    self.startvalorant()
                    break
                
                
                q = pyautogui.locateOnScreen("images/inqueue2.png",grayscale = True)
                q2 = pyautogui.locateOnScreen("images/inqueue2.png",grayscale = True,confidence=0.6)  


                
                if q is not None or q2 is not None:
                    
                    print(Style.RESET_ALL)
                    print(Fore.GREEN+" [√] Detected in queue after game")
                    self.game()
                    
                if q is None or q2 is None:
                    print(Style.RESET_ALL)
                    print(Fore.RED+" [!] Detected not in queue after game")
                    time.sleep(1)
                
                    self.skipbutton()        
        
        
        
    def game(self):
        time.sleep(1)
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Waiting for a game")
        
        
        now = time.time()
        
        future = now + 660
        
        
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            ingame = pyautogui.locateOnScreen(banner)
            ingame2 = pyautogui.locateOnScreen(banner, confidence=0.6)
            
            
            
            if ingame is not None or ingame2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected in game")
                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.YELLOW+" [-] Waiting for the game to end")
                time.sleep(2)
            
                self.endofgame()
    
    
    def endofgame(self):
        
        now = time.time()
        
        future = now + 780
        
        time.sleep(5)
        
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            menu = pyautogui.locateOnScreen("images/menu.png",grayscale = True)
            menu2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6,grayscale = True)
            
            if menu is not None or menu2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected that the game has ended")
                time.sleep(2)
                self.result()
            
            else:
                self.antiafk()
    
    
    def antiafk(self):
        time.sleep(5)
        n = randint(20,35)
        a = 0
        while a <= n:
            a += 1
            n2 = randint(1,6)
            if n2 == 1:
                pyautogui.keyDown('w')
                sleep(randint(2,6)/10)
                
            if n2 == 2:
                pyautogui.keyUp('w')
                pyautogui.keyDown('d')
                pyautogui.click()
                
            if n2 == 3:
                pyautogui.keyDown('a')
                sleep(randint(1,3)/10)
                pyautogui.keyDown('a')
                pyautogui.click()
                sleep(randint(2,4)/10)
                
            if n2 == 4:
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                sleep(randint(2,5)/10)
                
            if n2 == 5:
                pyautogui.keyUp('s')
                sleep(randint(4,6)/10)
                
            if n2 == 6:
                pyautogui.keyDown('w')
                sleep(randint(2,4)/10)
                pyautogui.keyUp('w')
        self.endofgame()
    
    
    def result(self):
        print(Style.RESET_ALL)
        print(Fore.YELLOW+" [-] Waiting for an XP screen")
        
        time.sleep(3)
        
        now = time.time()
        
        future = now + 120
        
        while True:
            
            if time.time() > future:
                #detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED+" [!] Found a possible error with Valorant.")
                self.startvalorant()
                break
            
            xpscreen = pyautogui.locateOnScreen("images/menu.png",grayscale = True)
            xpscreen2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6,grayscale = True)
            if xpscreen is not None or xpscreen2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Detected XP screen")
                time.sleep(2)
                self.gamesplayed += 1
                self.xpamount += 900
                
                
                runtime = datetime.now() - start
                runtime = str(runtime)
                runtime = runtime[:-7]
                
                exact = start.strftime("%H:%M:%S")
                dat = start.strftime("%d %h %Y")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                
                
                print(Style.RESET_ALL+Fore.YELLOW+"———————————————————————————————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW+" Earned",Style.BRIGHT+Fore.YELLOW+str(self.xpamount)+" XP"+Style.RESET_ALL+Fore.YELLOW,"in total")
                print (Fore.YELLOW+" Bot has been running for",Style.BRIGHT+Fore.YELLOW+str(runtime)+Style.RESET_ALL+Fore.YELLOW)
                print (Fore.YELLOW+" Bot was started at",Style.BRIGHT+Fore.YELLOW+str(exact),Style.RESET_ALL+Fore.YELLOW+"on the"+Style.BRIGHT+Fore.YELLOW,(dat)+Style.RESET_ALL+Fore.YELLOW)
                print(Fore.YELLOW+" Played",Style.BRIGHT+Fore.YELLOW+str(self.gamesplayed),"games"+Style.RESET_ALL+Fore.YELLOW)
                print (" Valorant has been",Style.BRIGHT+Fore.YELLOW+"restarted",self.restarted,"times")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL+Fore.YELLOW+"———————————————————————————————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW+"                                 Valbot v1.4")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                
                try:
                    f = open('webhook.save', 'r')
                    line = f.readline()
                    f.close()
                    found = True
                except Exception:
                    found = False


                if found == True:

                    webhook = DiscordWebhook(url=line)

                    # create embed object for webhook


                    embed = DiscordEmbed(title='Match Completed', color=242424)
                    embed.set_author(name='Valbot', url='https://github.com/MrFums/ValorantBot', icon_url='https://raw.githubusercontent.com/MrFums/ValorantBot/main/Valbot.png')
                    embed.set_footer(text='Valbot v1.4')
                    embed.set_timestamp()
                    embed.add_embed_field(name='Total XP', value=self.xpamount)
                    embed.add_embed_field(name='Time Elapsed', value=runtime)
                    embed.add_embed_field(name='Games Played', value=self.gamesplayed)



                    webhook.add_embed(embed)
                    response = webhook.execute()
                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED+" [!] Discord webhook is not setup. Set it up in the menu.")
                    print(Style.RESET_ALL)

                                
                                
                time.sleep(4)
                pyautogui.click(x=960, y=540)
                time.sleep(1)
                self.skipbutton()
                



def select_banner():
    global banner
    print ("")
    print (Style.RESET_ALL,Fore.YELLOW+"Make sure you have read the information about the bot before continuing")
    print(Style.RESET_ALL,Fore.YELLOW+"Please select a Player Card and equip that EXACT one in game: ")
    
    print(Style.RESET_ALL)
    print (Style.BRIGHT,Fore.WHITE+"1)",Fore.YELLOW+"Beta Pioneer Player Card")
    print("")
    print (Fore.WHITE+" 2)",Fore.YELLOW+"Valorant Card Player Card")
    print ("")
    print (Fore.WHITE+" 3)",Fore.YELLOW+"Return to Menu",Style.RESET_ALL)
    print ("")
    print(Style.BRIGHT + Fore.GREEN+"")
    banneroption = int(input(" > "))
    try:
        if banneroption == 1:
            banner = "images/1.png"
            print (Style.RESET_ALL)
            print (Fore.WHITE+" Selected the Beta Pioneer Player Card")
        
        elif banneroption == 2:
            banner = "images/2.png"
            print (Style.RESET_ALL)
            print (Fore.WHITE+" Selected the Valorant Card Player Card")
        
        elif banneroption == 3:
            main()
       
        else:
            print (Fore.RED+" [!] Error 1: Enter a valid integer within the range 1 - 3!")
            time.sleep(2)
            main()
    
    
    except ValueError:
        print (" Error 2: You must enter an integer!")
        time.sleep(2)
        main()



def main():

    from colorama import init
    from colorama import Fore, Back, Style
    init()
    
    print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

    print (Style.BRIGHT + Fore.RED + """
                                   
                                                                        
    8b           d8              88  88                                 
    `8b         d8'              88  88                          ,d     
     `8b       d8'               88  88                          88     
      `8b     d8'    ,adPPYYba,  88  88,dPPYba,    ,adPPYba,   MM88MMM  
       `8b   d8'     ""     `Y8  88  88P'    "8a  a8"     "8a    88     
        `8b d8'      ,adPPPPP88  88  88       d8  8b       d8    88     
         `888'       88,    ,88  88  88b,   ,a8"  "8a,   ,a8"    88,    
          `8'        `"8bbdP"Y8  88  8Y"Ybbd8"'    `"YbbdP"'     "Y888  
                                                                         
                                                                        """)
    print(Style.RESET_ALL)



    print(Fore.RED + "                         v1.4"+Style.RESET_ALL,"-"+Fore.RED,Style.BRIGHT+"by Fums and WolfAnto")
    print("")
    print(Style.RESET_ALL)
    print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(Style.RESET_ALL)
    time.sleep(0.5)
    print (Style.BRIGHT + Fore.RED)
    print(Fore.WHITE+" 1)",Fore.YELLOW+"Launch Bot")
    print("")
    print(Fore.WHITE+" 2)",Fore.YELLOW+"Help + Information")
    print("")
    print(Fore.WHITE+" 3)",Fore.YELLOW+"Manage Webhook")
    print("")
    print(Fore.WHITE+" 4)",Fore.YELLOW+"Exit Bot")
    print("")
    print(Style.BRIGHT + Fore.GREEN+"")
    
    
    menu = int(input(" > "))
    
    try:
        if menu == 1:
            select_banner()
            
            print (Style.RESET_ALL)
            time.sleep(2)
            print(Fore.WHITE + " 1)",Fore.CYAN +"Make sure Valorant is focused and click",Fore.BLUE +"HOME",Fore.CYAN +"and leave it on that screen", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"Wait around",Fore.BLUE +"10 seconds",Fore.CYAN +"and do not click anything", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"Let the bot do the rest!", Style.RESET_ALL)
            print(Style.RESET_ALL)
            print("")
            print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.RESET_ALL)
            time.sleep(5)

            bot.firststart()
            
            
        elif menu == 2:
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
            print(Fore.CYAN +" If you use",Fore.BLUE+"720p",Fore.CYAN+"move the images from",Fore.BLUE+"720 folder",Fore.CYAN+"into the",Fore.BLUE+"ImageChecks",Fore.CYAN+"folder")
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
            print(Style.RESET_ALL)
            print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.BRIGHT,Fore.RED)
            print("")
            print(" Input anything to return to the menu...")
            print(Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN+"")
            menu = str(input(" > "))
            main()
            


        elif menu == 3:
            print(Style.RESET_ALL)
            print(Fore.RED + " WEBHOOK MANAGER")
            print(Style.RESET_ALL)
            print(Fore.WHITE + " 1)",Fore.CYAN +"Open Discord, go to a server where you have permission to create and manage a webhook")
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"Either create and / or edit an existing channel and go to 'Integrations'")
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"Click webhooks and then click 'Create Webhook', select the right channel,")
            print(Fore.CYAN,"edit the name and image if you wish, and then click 'Copy Webhook URL'")
            print("")
            print(Fore.WHITE + " 4)",Fore.CYAN +"Paste your webhook below with nothing else, make sure there are no spaces")
            print(Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN+"")
            
            
            if os.path.exists("webhook.save"):
                os.remove("webhook.save")
                f = open("webhook.save", "a+")
                inputwebhook = input(" > ")
                print(Style.RESET_ALL)
                f.write(inputwebhook)
                f.close()
                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Webhook added. Please make sure that it is correct:")
                print(Style.BRIGHT + Fore.RED,inputwebhook)
                print(Style.RESET_ALL+ Fore.RED)
                print(" Input anything to return to the menu...")
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.GREEN+"")
                menu = str(input(" > "))
                main()
                
                
            else:
                f = open("webhook.save", "a+")
                inputwebhook = input(" > ")
                print(Style.RESET_ALL)
                f.write(inputwebhook)
                f.close()
                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.GREEN+" [√] Webhook added. Please make sure that it is correct:")
                print(Style.BRIGHT + Fore.RED,inputwebhook)
                print(Style.RESET_ALL+ Fore.RED)
                print(" Input anything to return to the menu...")
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.GREEN+"")
                menu = str(input(" > "))
                main()

            

        elif menu == 4:
            print(Style.BRIGHT + Fore.RED+" Ok, closing. Thanks for using!")
            time.sleep(1)
            quit()

            
        else:
            print (" Error 1: Enter a valid integer within the range 1 - 3!")
            time.sleep(2)
            main()
    
    
    except ValueError:
        print (" Error 2: You must enter an integer!")
        time.sleep(2)
        main()

if __name__ == "__main__":
    bot = bot()
    
    #time.sleep(3) #comment this out if youre not testing functions
    main()

