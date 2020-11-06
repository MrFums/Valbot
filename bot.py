import os
import time
from datetime import datetime
from pathlib import Path
from random import randint
from time import sleep

import psutil
import pyautogui
import pygetwindow as gw
from colorama import Fore, Style
from colorama import init
from discord_webhook import DiscordWebhook, DiscordEmbed
from pycaw.pycaw import AudioUtilities
from pypresence import Presence

init()

# ---------------------------------------------------------------

start_time = time.time()
start = datetime.now()



pyautogui.FAILSAFE = False
print(Style.BRIGHT + Fore.RED + """
                                   
                                                                        
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
print(Fore.RED + "                         v1.7.2" + Style.RESET_ALL, "-" + Fore.RED,
      Style.BRIGHT + "by Fums and WolfAnto")
print(Style.RESET_ALL + Fore.RED + "———————————————————————————————————————————————————————————————————————————————")
print(Style.RESET_ALL + Style.BRIGHT + Fore.RED)


class bot:
    def __init__(self):

        self.xpamount = 0  # how much xp the bot has earnt during runtime
        self.restarted = 0  # how many times the bot has restarted during runtime
        self.gamesplayed = 0  # num of games played during runtime

        try:  # if cant connect to discord (if it isnt open for example), bot doesnt crash
            self.RPC = Presence(client_id="772841390467711041")  # discord rpc client id

            self.RPC.connect()  # connects to rpc

            self.version = "Valbot v1.7.2"  # varible str to change valbot version name in outputs
        except Exception:
            pass

    def restartbot(self):  # restarts the bot after 2 hours
        print(Style.RESET_ALL)
        print(Fore.RED + " [!] BOT IS RESTARTING AFTER 2 HOURS")
        self.RPC.close()
        time.sleep(1)
        os.startfile("restart.py")  # starts the restart script which reopens this script
        quit()  # quits this runtime of the script

    def inqueue2(self):  # if in queue after the game (due to different in queue buttons)

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF IN QUEUE")
        time.sleep(.2)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            q = pyautogui.locateOnScreen("images/inqueue2.png", grayscale=True)
            q2 = pyautogui.locateOnScreen("images/inqueue2.png", grayscale=True, confidence=0.6)

            if q is not None or q2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                self.waitingforgame()

            if q is None or q2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED NOT IN QUEUE")
                time.sleep(1)

                self.skiprewardbutton()

    def playagain(self):
        time.sleep(1)
        now = time.time()

        desynccheck = now + 30

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR PLAY AGAIN BUTTON")
        while True:

            if time.time() > desynccheck:
                # detects possible server -> client desync so presses play button instead (thanks @guwopg0d for the idea)
                # works by pressing the play button after 30 seconds
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE SERVER DESYNC ISSUE")
                self.playbutton()
                break

            playagain = pyautogui.locateOnScreen("images/playagain.png", grayscale=True)
            playagain2 = pyautogui.locateOnScreen("images/playagain.png", confidence=0.6, grayscale=True)

            if playagain is not None or playagain2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED PLAY AGAIN BUTTON")

                if playagain is not None:
                    pyautogui.click(playagain)
                    time.sleep(1)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(playagain)

                    self.inqueue2()

                if playagain2 is not None:
                    pyautogui.click(playagain2)
                    time.sleep(1)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(playagain2)
                    self.inqueue2()

    def valorantrunning(self):
        found = False
        print(Fore.YELLOW, "[-] CHECKING IF VALORANT IS RUNNING")
        print(Style.RESET_ALL)
        time.sleep(2)

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                break

        if not found:
            print(Fore.RED, "[!] VALORANT IS NOT RUNNING")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print(Fore.GREEN, "[√] VALORANT IS RUNNING")
            time.sleep(2)
            self.playbutton()

    def startvalorant(self):

        activeactivity = "STARTING VALORANT"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

        except Exception:
            pass

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                proc.kill()
                print(Fore.YELLOW, "[-] KILLING THE VALORANT PROCESS")
                time.sleep(10)

        print(Style.RESET_ALL + Fore.YELLOW, "[-] STARTING VALORANT")
        print(Style.RESET_ALL)
        vallnk = Path("Valorant.lnk")
        if vallnk.is_file():
            # file exists
            time.sleep(5)
            os.startfile("Valorant.lnk")

        else:
            print(Style.RESET_ALL, Fore.RED + "[!] YOU DO NOT HAVE A VALORANT SHORTCUT IN THE BOT DIRECTORY!")
            print(Style.RESET_ALL)
        time.sleep(8)
        self.restarted += 1
        self.valorantrunning()

    def playbutton(self):

        now = time.time()

        future = now + 720

        activeactivity = "In pre-game lobby"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

        except Exception:
            pass
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR PLAY BUTTON")
        time.sleep(2)
        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            play = pyautogui.locateOnScreen("images/play.png", grayscale=True)
            play2 = pyautogui.locateOnScreen("images/play.png", confidence=0.6, grayscale=True)

            if play is not None or play2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED PLAY BUTTON")

                if play is not None:
                    time.sleep(1)
                    pyautogui.click(play)
                    time.sleep(2)
                    self.playbuttonclicked()

                if play2 is not None:
                    time.sleep(1)
                    pyautogui.click(play2)
                    time.sleep(2)
                    self.playbuttonclicked()

    def deathmatchbutton(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW, "[-] SEARCHING FOR DEATHMATCH BUTTON")

        time.sleep(1)
        now = time.time()

        future = now + 45

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            deathmatch = pyautogui.locateOnScreen("images/deathmatch.png", grayscale=True)
            deathmatch2 = pyautogui.locateOnScreen("images/deathmatch.png", confidence=0.6, grayscale=True)

            if deathmatch is not None or deathmatch2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED DEATHMATCH BUTTON")

                if deathmatch is not None:
                    pyautogui.click(deathmatch)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    self.deathmatchbuttonclicked()

                if deathmatch2 is not None:
                    pyautogui.click(deathmatch2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    self.deathmatchbuttonclicked()

                time.sleep(5)

    def skiprewardbutton(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR A SKIP BUTTON")
        time.sleep(3)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            skip = pyautogui.locateOnScreen("images/skip.png", grayscale=True)
            skip2 = pyautogui.locateOnScreen("images/skip.png", grayscale=True, confidence=0.6)

            if skip is not None or skip2 is not None:

                if skip is not None:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] DETECTED A SKIP BUTTON")
                    time.sleep(1)
                    pyautogui.click(skip)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip)

                    self.playagain()

                if skip2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] DETECTED A SKIP BUTTON")
                    time.sleep(1)
                    pyautogui.click(skip2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip2)

                    self.playagain()

            if skip is None or skip2 is None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] COULD NOT DETECT A SKIP BUTTON")
                time.sleep(1)

                self.playagain()

    def deathmatchbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF DEATHMATCH IS DETECTED")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            ondeathmatch = pyautogui.locateOnScreen("images/ondeathmatch.png", grayscale=True)
            ondeathmatch2 = pyautogui.locateOnScreen("images/ondeathmatch.png", grayscale=True, confidence=0.8)

            if ondeathmatch is not None or ondeathmatch2 is not None:

                if ondeathmatch is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT DEATHMATCH IS SELECTED")
                    time.sleep(1)
                    self.searchforgame()

                if ondeathmatch2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT DEATHMATCH IS SELECTED")
                    time.sleep(1)
                    self.searchforgame()

            if ondeathmatch is None or ondeathmatch2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT DEATHMATCH IS NOT SELECTED")
                time.sleep(1)
                self.deathmatchbutton()

    def playbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF PLAY BUTTON IS SELECTED")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            onplay = pyautogui.locateOnScreen("images/onplay.png", grayscale=True)
            onplay2 = pyautogui.locateOnScreen("images/onplay.png", grayscale=True, confidence=0.8)

            if onplay is not None or onplay2 is not None:

                if onplay is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT PLAY BUTTON IS SELECTED")
                    time.sleep(1)
                    self.deathmatchbutton()

                if onplay2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT PLAY BUTTON IS SELECTED")
                    time.sleep(1)
                    self.deathmatchbutton()

            if onplay is None or onplay2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT PLAY BUTTON IS NOT SELECTED")
                time.sleep(1)
                self.playbutton()

    def firststart(self):
        if os.path.exists("runtime_values"):
            try:
                f = open('runtime_values', 'r')
                for i, line in enumerate(f):
                    if i == 0:
                        self.xpamount = int(line.strip())
                    elif i == 1:
                        self.gamesplayed = int(line.strip())
                    elif i == 2:
                        self.restarted = int(line.strip())
                f.close()

                if os.path.exists("runtime_values"):
                    os.remove("runtime_values")

            except Exception:
                pass

        foundval = False
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                window = gw.getWindowsWithTitle('Valorant')[0]
                foundval = True

        if not foundval:
            self.startvalorant()

        if not window.isMaximized:
            window.maximize()
            self.firststart()

        activeactivity = "Loading bot"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

        except Exception:
            pass

        print(Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT + "[!] BOT WILL BEGIN IN 15 SECONDS")
        print(Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT + "[!] SCHEDULED TO RESTART EVERY 2 HOURS")
        print(Style.RESET_ALL)
        time.sleep(15)

        self.playbutton()

    def searchforgame(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR START BUTTON")

        now = time.time()

        future = now + 240

        while True:
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " Found a possible error with Valorant.")
                self.startvalorant()
                break

            startbutton = pyautogui.locateOnScreen("images/start.png", grayscale=True)
            start2 = pyautogui.locateOnScreen("images/start.png", confidence=0.6, grayscale=True)

            again = pyautogui.locateOnScreen("images/playagain.png", grayscale=True)
            again2 = pyautogui.locateOnScreen("images/playagain.png", confidence=0.6, grayscale=True)

            if startbutton is not None or start2 is not None or again is not None or again2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED START BUTTON")

                if startbutton is not None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(startbutton)
                    self.inqueue()

                if start2 is not None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(start2)
                    self.inqueue()

                if again is not None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(again2)
                    self.inqueue()

                if again2 is not None:
                    pyautogui.click(x=960, y=540)
                    time.sleep(.5)
                    pyautogui.click(again2)
                    self.inqueue()

    def inqueue(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] CHECKING IF IN QUEUE")
        time.sleep(.1)
        now = time.time()

        future = now + 240

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            q = pyautogui.locateOnScreen("images/inqueue.png", grayscale=True)
            q2 = pyautogui.locateOnScreen("images/inqueue.png", grayscale=True, confidence=0.6)

            if q is not None or q2 is not None:
                if q is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    time.sleep(1)
                    self.waitingforgame()
                if q2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    time.sleep(1)
                    self.waitingforgame()

            if q is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED NOT IN QUEUE")
                time.sleep(1)

                self.searchforgame()

    def waitingforgame(self):
        time.sleep(1)
        print(Style.RESET_ALL)

        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "VALORANT-Win64-Shipping.exe":
                volume.SetMute(1, None)

        activeactivity = "In a queue"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

        except Exception:
            pass
        print(Fore.YELLOW + " [-] WAITING FOR A GAME")

        now = time.time()

        future = now + 900  # if not in game after 15 mins, restart valorant as there may be an error. Change this if
        # your servers are bad (in seconds)

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            ingame = pyautogui.locateOnScreen("images/playercard.png")
            ingame2 = pyautogui.locateOnScreen("images/playercard.png", confidence=0.6)

            defaultcard = pyautogui.locateOnScreen("images/defaultcard.png", grayscale=True)
            defaultcard2 = pyautogui.locateOnScreen("images/defaultcard.png", grayscale=True, confidence=0.6)

            if ingame is not None or ingame2 is not None or defaultcard is not None or defaultcard2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED IN A GAME")
                pyautogui.click(x=960, y=540)
                activeactivity = "In a game"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

                except Exception:
                    pass

                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " [-] WAITING FOR THE GAME TO END")
                time.sleep(2)

                self.endofgame()

    def endofgame(self):

        now = time.time()

        future = now + 780

        time.sleep(5)

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            menu = pyautogui.locateOnScreen("images/menu.png", grayscale=True)
            menu2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6, grayscale=True)

            if menu is not None or menu2 is not None:
                self.gamesplayed += 1
                self.xpamount += 900

                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED AT END GAME SCREEN")

                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    volume = session.SimpleAudioVolume
                    if session.Process and session.Process.name() == "VALORANT-Win64-Shipping.exe":
                        volume.SetMute(0, None)

                activeactivity = "In pre-game lobby"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=time.time(), large_image="valbot",large_text=self.version, details=activeactivity)

                except Exception:
                    pass

                time.sleep(2)
                self.xpscreen()

            else:
                self.antiafk()

    def antiafk(self):
        time.sleep(5)
        n = randint(20, 35)
        a = 0
        while a <= n:
            a += 1
            n2 = randint(1, 6)
            if n2 == 1:
                pyautogui.keyDown('w')
                sleep(randint(2, 6) / 10)

            if n2 == 2:
                pyautogui.keyUp('w')
                pyautogui.keyDown('d')
                pyautogui.click()

            if n2 == 3:
                pyautogui.keyDown('a')
                sleep(randint(1, 3) / 10)
                pyautogui.keyDown('a')
                pyautogui.click()
                sleep(randint(2, 4) / 10)

            if n2 == 4:
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                sleep(randint(2, 5) / 10)

            if n2 == 5:
                pyautogui.keyUp('s')
                sleep(randint(4, 6) / 10)

            if n2 == 6:
                pyautogui.keyDown('w')
                sleep(randint(2, 4) / 10)
                pyautogui.keyUp('w')
        self.endofgame()

    def xpscreen(self):
        global line
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR THE XP SCREEN")

        time.sleep(3)

        now = time.time()

        future = now + 600

        twohour = start_time + 7200

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            xpscreen = pyautogui.locateOnScreen("images/menu.png", grayscale=True)
            xpscreen2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6, grayscale=True)
            if xpscreen is not None or xpscreen2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED THE XP SCREEN")
                time.sleep(2)

                runtime = datetime.now() - start
                runtime = str(runtime)
                runtime = runtime[:-7]

                exact = start.strftime("%H:%M:%S")
                dat = start.strftime("%d %h %Y")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)

                print(
                    Style.RESET_ALL + Fore.YELLOW + "———————————————————————————————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " Earned",
                      Style.BRIGHT + Fore.YELLOW + str(self.xpamount) + " XP" + Style.RESET_ALL + Fore.YELLOW,
                      "in total")
                print(Fore.YELLOW + " Bot has been running for",
                      Style.BRIGHT + Fore.YELLOW + str(runtime) + Style.RESET_ALL + Fore.YELLOW)
                print(Fore.YELLOW + " Bot was started at", Style.BRIGHT + Fore.YELLOW + str(exact),
                      Style.RESET_ALL + Fore.YELLOW + "on the" + Style.BRIGHT + Fore.YELLOW,
                      dat + Style.RESET_ALL + Fore.YELLOW)
                print(Fore.YELLOW + " Played", Style.BRIGHT + Fore.YELLOW + str(self.gamesplayed),
                      "games" + Style.RESET_ALL + Fore.YELLOW)
                print(" Valorant has been", Style.BRIGHT + Fore.YELLOW + "restarted", self.restarted, "times")
                print(Style.RESET_ALL)
                print(
                    Style.RESET_ALL + Fore.YELLOW + "———————————————————————————————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "                                 Valbot v1.7.2")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                time.sleep(1)
                found = False
                if os.path.exists("webhook.config"):
                    try:
                        f = open('webhook.config', 'r')
                        line = f.readline()
                        f.close()
                        found = True
                    except Exception:
                        found = False

                if found is True:

                    webhook = DiscordWebhook(url=line)

                    # create embed object for webhook
                    embed = DiscordEmbed(title='Match Completed', color=34343)
                    embed.set_author(name='Valbot', url='https://github.com/MrFums/Valbot',
                                     icon_url='https://raw.githubusercontent.com/MrFums/Valbot/main/valbot')
                    embed.set_footer(text='Valbot v1.7.2')
                    embed.set_timestamp()
                    embed.add_embed_field(name='Total XP', value=self.xpamount)
                    embed.add_embed_field(name='Games Played', value=self.gamesplayed)
                    embed.add_embed_field(name='Current Bot Runtime', value=runtime)
                    webhook.add_embed(embed)
                    response = webhook.execute()

                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] DISCORD WEBHOOK IS NOT SETUP")

                time.sleep(4)
                pyautogui.click(x=960, y=540)
                time.sleep(1)

                if time.time() > twohour:

                    if os.path.exists("runtime_values"):
                        os.remove("runtime_values")

                    f = open("runtime_values", "a+")
                    f.write(str(self.xpamount))
                    f.write("\n")
                    f.write(str(self.gamesplayed))
                    f.write("\n")
                    f.write(str(self.restarted))
                    f.close()

                    # detects possible issue with valorant and restarts the game
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] BOT IS NOW RESTARTING AFTER 2 HOURS OF RUNTIME")
                    self.restartbot()
                    break

                self.skiprewardbutton()


if __name__ == "__main__":
    bot = bot()
    bot.firststart()
