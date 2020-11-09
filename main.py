import math
import os
import time
from pathlib import Path
import requests
from colorama import Fore, Style
from colorama import init
from pypresence import Presence

init()
os.system('mode con: cols=39 lines=25')

def main():
    
    try:
        RPC = Presence(client_id="772841390467711041")
        RPC.connect()
    except Exception:
        pass
    
    version = "Valbot v1.7.4"
    versionstripped = version.replace("Valbot ", "")


    activeactivity = "In console"

    try:

        RPC.update(state=("Running "+ version.replace("Valbot ","")), start=time.time(), large_image="valbot",large_text=version, details=activeactivity)

    except Exception:
        pass

    print(Fore.RED + """
    ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
    ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
    ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
     ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
     ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
      ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝
                             """ + Style.NORMAL + Fore.RED, versionstripped + Style.RESET_ALL)

    print(Style.RESET_ALL)
    print(Style.RESET_ALL + Fore.RED + "          By Fums & WolfAnto")
    print(Style.RESET_ALL)
    print(Style.RESET_ALL + Fore.RED + "———————————————————————————————————————")

    print(Style.RESET_ALL)
    print(Fore.RED + " [1]", Style.BRIGHT + "Start Bot")
    print(Style.RESET_ALL)
    print(Fore.RED + " [2]", Style.BRIGHT + "Information")
    print(Style.RESET_ALL)
    print(Fore.RED + " [3]", Style.BRIGHT + "Manage Discord Webhook")
    print(Style.RESET_ALL)
    print(Fore.RED + " [4]", Style.BRIGHT + "XP Calculator")
    print(Style.RESET_ALL)
    print(Fore.RED + " [5]", Style.BRIGHT + "Exit Bot")
    print(Style.RESET_ALL)

    print(Fore.YELLOW + "")
    menu = int(input(" > "))

    try:
        if menu == 1:

            print(Style.RESET_ALL)
            print(Fore.YELLOW, "Make sure you have the")
            print(Style.BRIGHT, "Valorant Card", Style.NORMAL + "Player Card equipped")
            print(Style.RESET_ALL)
            print(Fore.YELLOW, "Valorant must be" + Style.BRIGHT, "FULLSCREEN")
            print(Style.NORMAL, "for the bot to function")
            response = requests.get("https://api.github.com/repos/MrFums/Valbot/releases/latest")
            latest2 = response.json()["name"]
            changelog = response.json()["body"]

            latest3 = latest2.replace("Valbot v", "")
            latest4 = latest2.replace("Valbot ","")
            latest = latest3.replace(".", "")
            latest = int(latest)

            version = version.replace("Valbot v", "")
            version = version.replace(".", "")
            version = int(version)

            if version < latest:
                print(Style.RESET_ALL)
                print(Fore.RED, "Version (" + str(versionstripped) + ") is outdated")
                print(Style.RESET_ALL)
                print(Fore.RED, "Download latest version (" + str(latest4) + ") now")
                print(Style.RESET_ALL)
                time.sleep(5)

            print(Style.RESET_ALL)

            vallnk = Path("Valorant.lnk")
            if vallnk.is_file():
                # file exists
                try:
                    RPC.close()
                except Exception:
                    pass
                time.sleep(2)
                os.startfile("bot.py")
                time.sleep(.5)
                quit()
            else:
                print(Fore.RED, 'You do not have a Valorant shortcut')
                print(' named "Valorant" in the directory')
                print(Fore.RED, 'Add one now to continue')
                time.sleep(5)
                print(Style.RESET_ALL)
                if os.path.exists("runtime_values"):
                    os.remove("runtime_values")
                time.sleep(5)
                main()


        elif menu == 2:
            print(Style.RESET_ALL + "")
            print(Fore.RED + " IMPORTANT INFORMATION")
            print("")
            print(Fore.WHITE + " 1)", Fore.CYAN + "Setup your Valorant shortcut")
            print("    and discord webhook (optional)", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Change your player card to the")
            print("    Valorant Card Player Card")
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "Valorant must be fullscreen")
            print("    and focused")
            print("")
            print(Fore.BLUE + " Discord :", Fore.YELLOW + "Fums#0888")
            print(Fore.CYAN, Fore.BLUE + "Github :",Fore.YELLOW + "https://github.com/MrFums", Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Style.BRIGHT, Fore.RED)
            print("")
            print(" Input anything to return...")
            print(Fore.YELLOW, Style.NORMAL + "")
            input(" > ")
            main()



        elif menu == 3:
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
            print(" Paste a webhook to save or anything")
            print(" else to cancel")
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)

            urlcheck = "https://discord.com/api/webhooks/"
            print(Fore.YELLOW + "")
            inputwebhook = input(" > ")
            inputwebhook = inputwebhook.replace("https://discordapp.com/api/webhooks/",
                                                "https://discord.com/api/webhooks/")

            if urlcheck in inputwebhook:
                print(Style.RESET_ALL)

                if os.path.exists("webhook.config"):
                    os.remove("webhook.config")

                f = open("webhook.config", "a+")
                f.write(inputwebhook)
                f.close()
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] Webhook added")
                print(Style.RESET_ALL)
                time.sleep(3)
                main()

            else:
                print(Style.RESET_ALL)
                print(Fore.RED + " The input was not a webhook, returning to menu...")
                time.sleep(3)
                main()

        elif menu == 4:
            print(Style.RESET_ALL)
            print(Style.RESET_ALL, Fore.YELLOW + Style.BRIGHT, "How much XP do you need to earn?")
            try:
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "")
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

        elif menu == 5:
            print(Style.BRIGHT + Fore.RED + " Quitting...")
            time.sleep(1)
            quit()

        else:
            print(" Error 1: Enter a valid integer within the range 1 - 5!")
            time.sleep(2)
            main()


    except ValueError:
        print(" Error 2: You must enter an integer!")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
