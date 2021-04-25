try:
    import pathlib
    import requests
    import webbrowser
    import math
    import keyboard
    import psutil
    import pyautogui
    import pygetwindow as gw
    import os
    import time
    import urllib.request


    from PIL import Image
    from pathlib import Path
    from datetime import datetime
    from random import randint
    from time import sleep
    from colorama import Fore, Style
    from colorama import init
    from configparser import ConfigParser
except Exception as e: print(e), print("Try to reinstall packages"), input(), quit()


init()  # not a clue what init function its loading but its needed lol
# ---------------------------------------------------------------

def main():

    config = ConfigParser(allow_no_value=True)
    config.read('config.ini')

    if not os.path.exists('config.ini'):
        open('config.ini','a+')
        config.add_section('settings')
        config.set('settings', 'webhook', 'EMPTY_WEBHOOK')
        config.set('settings', 'matchlimit', '0')
        config.set('settings', 'xptarget', '0')

        config.add_section('runtime_values')
        config.set('runtime_values', '; you do not need to touch these, they are for when the bot restarts', None)
        config.set('runtime_values', 'restarted', '0')
        config.set('runtime_values', 'gamesplayed', '0')
        config.set('runtime_values', 'xpamount', '0')
        config.set('runtime_values', 'runtime', '0')
        config.set('runtime_values', 'starttime', '0')
        
        config.add_section('lifetime_values')
        config.set('lifetime_values', 'totalrestarted', '0')
        config.set('lifetime_values', 'totalgamesplayed', '0')
        config.set('lifetime_values', 'totalxpamount', '0')
        config.set('lifetime_values', 'totalruntime', '0')

        
        with open('config.ini', 'w+') as configfile:
            config.write(configfile)
    
    

    version = "Valbot v2.2  "
    versionstripped = version.replace("Valbot ", "")
    print(Style.RESET_ALL) 
    os.system('mode con: cols=39 lines=31')
    title = "title " + version
    os.system(title)
    print(Fore.YELLOW + """
    ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
    ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
    ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
     ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
     ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
      ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝
                           """ + Style.NORMAL + Fore.RED, Style.RESET_ALL)

    print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "     " + version + "         Fums#0888")
    print(Style.RESET_ALL) 
    print(Style.RESET_ALL)
    print(Style.RESET_ALL + Fore.YELLOW + "———————————————————————————————————————")

    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [1]", Style.BRIGHT + "Start Bot")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [2]", Style.BRIGHT + "Information / How to Use")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [3]", Style.BRIGHT + "XP Calculator")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [4]", Style.BRIGHT + "Join Discord")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [5]", Style.BRIGHT + "Edit Discord Webhook")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [6]", Style.BRIGHT + "Change XP Limit")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [7]", Style.BRIGHT + "Change XP Target")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [8]", Style.BRIGHT + "Exit Bot")
    print(Style.RESET_ALL)
    
    print(Fore.RED + "")

    menu = int(input(" > "))
    
    try:
        if menu == 1:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.YELLOW, "Valorant must be" + Style.BRIGHT, "WINDOWED FULLSCREEN")
            print(Style.NORMAL, "for the bot to function")
            print(Style.RESET_ALL)
            print(Fore.YELLOW, "Minimise any other open programs")
            print(Style.RESET_ALL)
            print(Fore.YELLOW, "Valorant must be in English and be ")
            print(Fore.YELLOW, "1920 x 1080 resolution")


            print(Style.RESET_ALL)
            root = str(pathlib.Path(__file__).parent.absolute())
            fullpath = root + "\Valorant.lnk"
            vallnk = Path(fullpath)
            if vallnk.is_file():
                # file exists
                config = ConfigParser(allow_no_value=True)
                
                config.read('config.ini')


                totalrestarted = config.getint('lifetime_values', 'totalrestarted')
                totalgamesplayed = config.getint('lifetime_values', 'totalgamesplayed')
                totalxpamount = config.getint('lifetime_values', 'totalxpamount')
                totalruntime = config.getint('lifetime_values', 'totalruntime')

                restartedlast = config.getint('runtime_values', 'restarted')
                gamesplayedlast = config.getint('runtime_values', 'gamesplayed')
                xpamountlast = config.getint('runtime_values', 'xpamount')
                runtimelast = config.getint('runtime_values', 'runtime')

                totalrestarted += restartedlast
                totalgamesplayed += gamesplayedlast
                totalxpamount += xpamountlast
                totalruntime += runtimelast

                config.set('lifetime_values', 'totalrestarted', str(totalrestarted))
                config.set('lifetime_values', 'totalgamesplayed', str(totalgamesplayed))
                config.set('lifetime_values', 'totalxpamount', str(totalxpamount))
                config.set('lifetime_values', 'totalruntime', str(totalruntime))

                config.set('runtime_values', 'restarted', '0')
                config.set('runtime_values', 'gamesplayed', '0')
                config.set('runtime_values', 'xpamount', '0')
                config.set('runtime_values', 'runtime', '0')
                timenow = time.time()
                config.set('runtime_values', 'starttime', str(timenow))
                
                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


                if os.path.exists('config.ini'):
                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')
                    try:
                        matchlimit = config.getint('settings', 'matchlimit')
                        
                        if matchlimit != 0:
                            print(Style.RESET_ALL)
                            print(Fore.GREEN, "Stopping after" + Style.BRIGHT, str(matchlimit), "matches", Style.RESET_ALL + Fore.GREEN + "played")
                        else:
                            print(Style.RESET_ALL)
                            print(Fore.GREEN, "No match limit found")

                    except:
                        pass
                print(Style.RESET_ALL)
                time.sleep(7)
                os.startfile("bot.py")
                time.sleep(.5)
                quit()
            else:
                print(Fore.RED, 'You do not have a Valorant shortcut')
                print(' named "Valorant" in the bots folder')
                print(Fore.RED, 'Add one now to continue')
                time.sleep(5)
                print(Style.RESET_ALL)
                time.sleep(5)
                main()


        elif menu == 2:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL + "")
            print(Fore.RED + " IMPORTANT INFORMATION")
            print("")
            print(Fore.WHITE + " 1)", Fore.CYAN + "Put your Valorant shortcut")
            print("    in the same folder as the bot.", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Must be in English and ")
            print("    1920x1080 resolution")
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "Valorant must be fullscreen ")
            print("    and focused")
            print("")
            print(Fore.BLUE + " Discord :", Fore.YELLOW + "Fums#0888")
            print(Fore.BLUE + " Discord :", Fore.YELLOW + "discord.gg/QFC46XKzxU")
            print(Fore.CYAN, Fore.BLUE + "Github :", Fore.YELLOW + "https://github.com/MrFums", Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Style.BRIGHT, Fore.RED)
            print("")
            print(" Input anything to return...")
            print(Fore.RED, Style.NORMAL + "")
            input(" > ")
            main()




        elif menu == 3:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Style.RESET_ALL, Fore.YELLOW + Style.BRIGHT, "How much XP do you need to earn?")
            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()

            xpa = xpai / 900
            xpau = (math.ceil(xpa))
            print(Style.RESET_ALL)
            print(Fore.BLUE, "Required Games: " + Style.BRIGHT + str(xpau), Fore.BLUE + "games")
            print(Style.RESET_ALL)
            print(Fore.BLUE, "ETA:", Style.BRIGHT + str(xpau / 4), Fore.BLUE + "hours")

            time.sleep(7)
            print(Style.RESET_ALL)
            main()

        elif menu == 4:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.BRIGHT + Fore.GREEN + " Loading Discord invite...")
            time.sleep(1)
            webbrowser.open('https://discord.com/invite/QFC46XKzxU')
            time.sleep(1)
            print(Style.RESET_ALL)
            main()
            
        elif menu == 5:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Fore.RED + " WEBHOOK MANAGER")
            print(Style.RESET_ALL)
            print(Fore.WHITE + " 1)", Fore.CYAN + "Open Discord, go to a server where")
            print("    you have permission to create")
            print("    and manage a webhook")
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Either create and / or edit an ")
            print('    existing channel and go to')
            print('    "Integrations"')
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "Click webhooks and then click")
            print('    "Create Webhook", select the right')
            print('    channel, and then click')
            print('    "Copy Webhook URL"')
            print("")
            print(Fore.WHITE + " 4)", Fore.CYAN + "Paste your webhook below")
            print(Style.RESET_ALL)
            print(Style.BRIGHT, Fore.RED)
            print(" Paste a webhook to save or enter")
            print(" anything else to cancel")
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)

            urlcheck = "https://discord.com/api/webhooks/"
            print(Fore.RED + "")
            inputwebhook = input(" > ")
            inputwebhook = inputwebhook.replace("https://discordapp.com/api/webhooks/", "https://discord.com/api/webhooks/")


            config = ConfigParser(allow_no_value=True)
            
            if urlcheck in inputwebhook:
                print(Style.RESET_ALL)
                config.read('config.ini')


                config.set('settings', 'webhook', inputwebhook)

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)

                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Webhook added")
                print(Style.RESET_ALL)
                time.sleep(3)
                main()
                
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + " Not a valid discord webhook")
                print(Fore.RED + " webhook, returning to menu...")
                time.sleep(3)
                main()
                            
                

        elif menu == 6:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Fore.GREEN, "Here you can limit the maximum amount")
            print(" of XP you would like to earn.")
            print(Style.RESET_ALL)
            print(Fore.GREEN, "When this limit has been reached, the")
            print(" program will stop.")
            print(Style.RESET_ALL)
            print(Fore.GREEN, "If you don't want a limit, enter 0.")

            print(Style.RESET_ALL)
            print(Fore.YELLOW, "How much XP would you like to earn?")

            print(Style.RESET_ALL)
            print(Style.RESET_ALL)

            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()



            xpa = xpai / 900
            xpau = (math.ceil(xpa))

            if xpai < 0:
                xpau = 0

            # need to write to config

            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                config.set('settings', 'matchlimit', str(xpau))

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


            os.system('cls' if os.name=='nt' else 'clear')

            if xpai > 0:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "Set to stop after", str(xpau), "games played")
            else:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "No XP limit set. Valbot will not stop")


            time.sleep(4)
            main()

        elif menu == 7:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Fore.GREEN, "Set a notification to be sent once\n you reach a certain amount of XP")
            print(Style.RESET_ALL)
            print(Fore.GREEN, "If you don't want a notification,\n enter 0.")
            print(Style.RESET_ALL)
            print(Fore.RED, "A DISCORD WEBHOOK IS REQUIRED!")

            print(Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.YELLOW, "How much XP would you like to earn?")

            print(Style.RESET_ALL)
            print(Style.RESET_ALL)

            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()



            if xpai < 0:
                xpai = 0
            

            # need to write to config

            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                config.set('settings', 'xptarget', str(xpai))

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


            os.system('cls' if os.name=='nt' else 'clear')

            if xpai > 0:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "Target of", str(xpai), "XP has been set")
            else:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "No target set.")


            time.sleep(4)
            main()
            

        elif menu == 8:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.BRIGHT + Fore.RED + " Quitting...")
            time.sleep(1)
            quit()

        else:
            print(" Error 1: Enter a valid integer within the range 1 - 8!")
            time.sleep(2)
            main()


    except ValueError:
        print(" Error 2: You must enter an integer!")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
