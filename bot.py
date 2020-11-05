from datetime import datetime
from random import randint
from time import sleep
from pathlib import Path
from colorama import Fore, Style
from colorama import init
from discord_webhook import DiscordWebhook, DiscordEmbed
from pycaw.pycaw import AudioUtilities
from pypresence import Presence

import psutil
import pyautogui
import pygetwindow as gw
import os
import time

init()
# test
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
print(Fore.RED + "                         v1.7" + Style.RESET_ALL, "-" + Fore.RED,
      Style.BRIGHT + "by Fums and WolfAnto")
print(Style.RESET_ALL + Fore.RED + "———————————————————————————————————————————————————————————————————————————————")
print(Style.RESET_ALL + Style.BRIGHT + Fore.RED)


def restartbot():
    print(Style.RESET_ALL)
    print(Fore.RED + " [!] Restarting the bot")
    time.sleep(1)
    os.startfile("restart.py")
    quit()


class bot:
    def __init__(self):

        self.xpamount = 0
        self.restarted = 0
        self.gamesplayed = 0
        self.restarted = 0

        try:
            self.RPC = Presence(client_id="772841390467711041")

            self.RPC.connect()

            self.version = "Valbot v1.7"
        except Exception:
            pass

    def inqueue2(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Detecting if in queue after game")
        time.sleep(.2)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            q = pyautogui.locateOnScreen("images/inqueue2.png", grayscale=True)
            q2 = pyautogui.locateOnScreen("images/inqueue2.png", grayscale=True, confidence=0.6)

            if q is not None or q2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected in queue after game")
                self.ingame()

            if q is None or q2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Detected not in queue after game")
                time.sleep(1)

                self.skiprewardbutton()

    def playagain(self):
        time.sleep(1)
        now = time.time()

        future = now + 120

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Waiting for play again button")
        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            playagain = pyautogui.locateOnScreen("images/playagain.png", grayscale=True)
            playagain2 = pyautogui.locateOnScreen("images/playagain.png", confidence=0.6, grayscale=True)

            if playagain is not None or playagain2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected play again button")

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
        print(Fore.YELLOW, "[-] Detecting if Valorant is running")
        print(Style.RESET_ALL)
        time.sleep(2)

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                break

        if not found:
            print(Fore.RED, "[!] Can not find Valorant running")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print(Fore.GREEN, "[√] Found Valorant running")
            time.sleep(2)
            self.playbutton()

    def startvalorant(self):

        activeactivity = "Starting Valorant"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                            large_text=self.version, details=activeactivity)

        except Exception:
            pass

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                proc.kill()
                print(Fore.YELLOW, "[-] Killing Valorant process")
                time.sleep(10)

        print(Style.RESET_ALL + Fore.YELLOW, "[-] Starting Valorant")
        print(Style.RESET_ALL)
        vallnk = Path("Valorant.lnk")
        if vallnk.is_file():
            # file exists
            time.sleep(5)
            os.startfile("Valorant.lnk")

        else:
            print(Style.RESET_ALL, Fore.RED, "You do not have a Valorant shortcut in the bots directory!")
        time.sleep(8)
        self.restarted += 1
        self.valorantrunning()

    def playbutton(self):

        now = time.time()

        future = now + 720

        activeactivity = "In pre-game lobby"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                            large_text=self.version, details=activeactivity)

        except Exception:
            pass
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Waiting for play button")
        time.sleep(2)
        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            play = pyautogui.locateOnScreen("images/play.png", grayscale=True)
            play2 = pyautogui.locateOnScreen("images/play.png", confidence=0.6, grayscale=True)

            if play is not None or play2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected play button")

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
        print(Fore.YELLOW, "[-] Searching for deathmatch button")

        time.sleep(1)
        now = time.time()

        future = now + 45

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            deathmatch = pyautogui.locateOnScreen("images/deathmatch.png", grayscale=True)
            deathmatch2 = pyautogui.locateOnScreen("images/deathmatch.png", confidence=0.6, grayscale=True)

            if deathmatch is not None or deathmatch2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected deathmatch button")

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
        print(Fore.YELLOW + " [-] Detecting a skip button")
        time.sleep(3)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            skip = pyautogui.locateOnScreen("images/skip.png", grayscale=True)
            skip2 = pyautogui.locateOnScreen("images/skip.png", grayscale=True, confidence=0.6)

            if skip is not None or skip2 is not None:

                if skip is not None:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] Detected a skip button")
                    time.sleep(1)
                    pyautogui.click(skip)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip)

                    self.playagain()

                if skip2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] Detected a skip button")
                    time.sleep(1)
                    pyautogui.click(skip2)
                    time.sleep(.5)
                    pyautogui.click(x=960, y=540)
                    time.sleep(1)
                    pyautogui.click(skip2)

                    self.playagain()

            if skip is None or skip2 is None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected no skip button")
                time.sleep(1)

                self.playagain()

    def deathmatchbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Detecting if deathmatch is selected")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            ondeathmatch = pyautogui.locateOnScreen("images/ondeathmatch.png", grayscale=True)
            ondeathmatch2 = pyautogui.locateOnScreen("images/ondeathmatch.png", grayscale=True, confidence=0.8)

            if ondeathmatch is not None or ondeathmatch2 is not None:

                if ondeathmatch is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] Detected that deathmatch is selected")
                    time.sleep(1)
                    self.searchforgame()

                if ondeathmatch2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] Detected that deathmatch is selected")
                    time.sleep(1)
                    self.searchforgame()

            if ondeathmatch is None or ondeathmatch2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Detected that deathmatch is not selected")
                time.sleep(1)
                self.deathmatchbutton()

    def playbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Detecting if play is selected")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            onplay = pyautogui.locateOnScreen("images/onplay.png", grayscale=True)
            onplay2 = pyautogui.locateOnScreen("images/onplay.png", grayscale=True, confidence=0.8)

            if onplay is not None or onplay2 is not None:

                if onplay is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] Detected that play is selected")
                    time.sleep(1)
                    self.deathmatchbutton()

                if onplay2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] Detected that play is selected")
                    time.sleep(1)
                    self.deathmatchbutton()

            if onplay is None or onplay2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Detected that play is not selected")
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

                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    volume = session.SimpleAudioVolume
                    if session.Process and session.Process.name() == "VALORANT-Win64-Shipping.exe":
                        volume.SetMute(1, None)
                break

        if not foundval:
            self.startvalorant()

        if not window.isMaximized:
            window.maximize()
            self.firststart()

        activeactivity = "Loading bot"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                            large_text=self.version, details=activeactivity)

        except Exception:
            pass

        print(Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT + "[!] Bot will start in 10 seconds")
        print(Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT + "[!] The bot will automatically restart every 2 hours")
        print(Style.RESET_ALL)
        time.sleep(10)

        self.playbutton()

    def searchforgame(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] Waiting for start button")

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
                print(Fore.GREEN + " [√] Detected start button")

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
        print(Fore.YELLOW + " [-] Detecting if in queue")
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
                    print(Fore.GREEN + " [√] Detected in queue")
                    time.sleep(1)
                    self.ingame()
                if q2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] Detected in queue")
                    time.sleep(1)
                    self.ingame()

            if q is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Detected not in queue")
                time.sleep(1)

                self.searchforgame()

    def ingame(self):
        time.sleep(1)
        print(Style.RESET_ALL)

        activeactivity = "In a queue"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                            large_text=self.version, details=activeactivity)

        except Exception:
            pass
        print(Fore.YELLOW + " [-] Waiting for a game")

        now = time.time()

        future = now + 900  # if not in game after 15 mins, restart valorant as there may be an error. Change this if
        # your servers are bad (in seconds)

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            ingame = pyautogui.locateOnScreen("images/playercard.png")
            ingame2 = pyautogui.locateOnScreen("images/playercard.png", confidence=0.6)

            defaultcard = pyautogui.locateOnScreen("images/defaultcard.png", grayscale=True)
            defaultcard2 = pyautogui.locateOnScreen("images/defaultcard.png", grayscale=True, confidence=0.6)

            if ingame is not None or ingame2 is not None or defaultcard is not None or defaultcard2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected in game")
                pyautogui.click(x=960, y=540)
                activeactivity = "In a game"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                                    large_text=self.version, details=activeactivity)

                except Exception:
                    pass

                time.sleep(1)
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " [-] Waiting for the game to end")
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
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            menu = pyautogui.locateOnScreen("images/menu.png", grayscale=True)
            menu2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6, grayscale=True)

            if menu is not None or menu2 is not None:
                self.gamesplayed += 1
                self.xpamount += 900

                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected that the game has ended")
                activeactivity = "In pre-game lobby"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=start_time, large_image="valbot",
                                    large_text=self.version, details=activeactivity)

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
        print(Fore.YELLOW + " [-] Waiting for an XP screen")

        time.sleep(3)

        now = time.time()

        future = now + 600

        twohour = start_time + 7200

        while True:

            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] Found a possible error with Valorant.")
                self.startvalorant()
                break

            xpscreen = pyautogui.locateOnScreen("images/menu.png", grayscale=True)
            xpscreen2 = pyautogui.locateOnScreen("images/menu.png", confidence=0.6, grayscale=True)
            if xpscreen is not None or xpscreen2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Detected XP screen")
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
                print(Fore.YELLOW + "                                 Valbot v1.7")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                time.sleep(1)
                try:
                    f = open('webhook.txt', 'r')
                    line = f.readline()
                    line = line.strip()
                    f.close()
                    found = True
                except Exception:
                    found = False

                if found is True:

                    webhook = DiscordWebhook(url=line)

                    # create embed object for webhook
                    embed = DiscordEmbed(title='Match Completed', color=34343)
                    embed.set_author(name='Valbot', url='https://github.com/MrFums/Valbot',
                                     icon_url='https://raw.githubusercontent.com/MrFums/Valbot/main/Valbot.png')
                    embed.set_footer(text='Valbot v1.7')
                    embed.set_timestamp()
                    embed.add_embed_field(name='Total XP', value=self.xpamount)
                    embed.add_embed_field(name='Games Played', value=self.gamesplayed)
                    embed.add_embed_field(name='Current Bot Runtime', value=runtime)
                    webhook.add_embed(embed)
                    response = webhook.execute()

                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] Discord webhook is not setup. Set it up in the menu.")

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
                    print(Fore.RED + " [!] Restarting bot after 2 hours runtime")
                    restartbot()
                    break

                self.skiprewardbutton()


if __name__ == "__main__":
    bot = bot()
    bot.firststart()
