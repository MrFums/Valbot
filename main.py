import math
import os
import time
from pathlib import Path

from colorama import Fore, Style
from colorama import init

init()


def main():
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
    print(
        Style.RESET_ALL + Fore.RED + "———————————————————————————————————————————————————————————————————————————————")

    print(Style.RESET_ALL + Style.BRIGHT + Fore.RED)
    print(Fore.WHITE + " 1)", Fore.YELLOW + "Start Bot")
    print("")
    print(Fore.WHITE + " 2)", Fore.YELLOW + "Information")
    print("")
    print(Fore.WHITE + " 3)", Fore.YELLOW + "Manage Discord Webhook")
    print("")
    print(Fore.WHITE + " 4)", Fore.YELLOW + "XP Calculator")
    print("")
    print(Fore.WHITE + " 5)", Fore.YELLOW + "Restart Bot")
    print("")
    print(Fore.WHITE + " 6)", Fore.YELLOW + "Exit Bot")
    print("")
    print(Style.BRIGHT + Fore.GREEN + "")

    menu = int(input(" > "))

    try:
        if menu == 1:

            print(Style.RESET_ALL)
            time.sleep(2)
            print(Fore.WHITE + " 1)", Fore.CYAN + "Make sure Valorant is focused and make sure you are in the",
                  Fore.BLUE + "MENU", Fore.CYAN, Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Bot will then be started in", Fore.BLUE + "10 seconds",
                  Fore.CYAN + Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 3)",
                  Fore.CYAN + "The bot should now run by itself, do not interrupt it unless you want to stop the bot",
                  Style.RESET_ALL)
            print(Style.RESET_ALL)
            print("")
            print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.RESET_ALL)

            vallnk = Path("Valorant.lnk")
            if vallnk.is_file():
                # file exists
                time.sleep(5)

                os.startfile("bot.py")

            else:
                print(Fore.RED, 'You do not have a Valorant shortcut named "Valorant" in the bots directory')
                time.sleep(5)
                print(Fore.RED, 'Create on now; the bot will not continue until you do so')
                print(Style.RESET_ALL)
                if os.path.exists("runtime_values"):
                    os.remove("runtime_values")
                time.sleep(5)
                main()


        elif menu == 2:
            print(
                Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.RESET_ALL + "")
            print(Fore.RED + " HOW TO RUN THE BOT")
            print("")
            print(Fore.WHITE + " 1)",
                  Fore.CYAN + "Setup your Valorant shortcut and discord webhook (optional)", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Run the bot by selecting", Fore.BLUE + "1",
                  Fore.CYAN + "in the main menu")
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "Change your player card to the",
                  Fore.BLUE + "Valorant Card Player Card", Fore.CYAN)
            print("")
            print(Fore.WHITE + " 4)", Fore.CYAN + "Follow the instructions in the ", Fore.BLUE + "bot console",
                  Fore.CYAN)
            print("")
            print(Fore.WHITE + " 5)", Fore.CYAN + "Let the game run and try not to touch your mouse / allow anything")
            print(Fore.CYAN + "    to interrupt the process")
            print("")
            print(Fore.CYAN + " If you wish to stop the bot", Fore.BLUE + "simply close this window", Fore.CYAN)
            print("")
            print("")
            print(Fore.RED + " OTHER PRECAUTIONS AND INFORMATION")
            print("")
            print(Fore.CYAN + " After verison 1.6 the bot will now restart itself every 2 hours")
            print(Fore.CYAN + " You must put a shortcut to Valorant in the same directory of this bot")
            print(Fore.CYAN + " XP gain is quite slow. This is due to the Deathmatch queue")
            print(Fore.CYAN + " If you can't find a game, change servers")
            print(Fore.CYAN + " It is advised to turn the mame hide option and decline friend requests on in",
                  Fore.BLUE + "Settings > Privacy", Fore.CYAN)
            print(Fore.CYAN + " Tested only on", Fore.BLUE + "1920x1080", Style.RESET_ALL)
            print("")
            print("")
            print(Fore.RED + " XP GAIN")
            print("")
            print(Fore.CYAN + " Average XP gains are as follows")
            print(Fore.WHITE + " 1 hour:", Fore.MAGENTA + "3,600 XP")
            print(Fore.WHITE + " 8 hours:", Fore.MAGENTA + "28,800 XP")
            print(Fore.WHITE + " 24 hours:", Fore.MAGENTA + "86,400 XP")
            print("")
            print("")
            print(Fore.RED + " CREDITS AND CONTACT")
            print("")
            print(Fore.CYAN + " Bot is written by and managed by", Fore.BLUE + "Fums",
                  Fore.CYAN + "to work with Valorant")
            print(Fore.CYAN + " This version of the bot is maintained by", Fore.BLUE + "Fums")
            print(Fore.CYAN + " Help will not be given if it isn't regarding the bots code or a bug")
            print(Fore.CYAN + " If your question / fix is already on the GitHub page, your request may be ignored")
            print(Fore.BLUE + " Discord :", Fore.YELLOW + "Fums#0888", Fore.CYAN + "| ", Fore.BLUE + "Github :",
                  Fore.YELLOW + "https://github.com/MrFums", Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.BRIGHT, Fore.RED)
            print("")
            print(" Input anything to return to the menu...")
            print(Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN + "")
            input(" > ")
            main()



        elif menu == 3:
            print(Style.RESET_ALL)
            print(Fore.RED + " WEBHOOK MANAGER")
            print(Style.RESET_ALL)
            print(Fore.WHITE + " 1)",
                  Fore.CYAN + "Open Discord, go to a server where you have permission to create and manage a webhook")
            print("")
            print(Fore.WHITE + " 2)",
                  Fore.CYAN + "Either create and / or edit an existing channel and go to 'Integrations'")
            print("")
            print(Fore.WHITE + " 3)",
                  Fore.CYAN + "Click webhooks and then click 'Create Webhook', select the right channel,")
            print(Fore.CYAN, "edit the name and image if you wish, and then click 'Copy Webhook URL'")
            print("")
            print(Fore.WHITE + " 4)",
                  Fore.CYAN + "Paste your webhook below with nothing else, make sure there are no spaces")
            print(Style.RESET_ALL)
            print(Style.BRIGHT, Fore.RED)
            print("")
            print(" Input anything other than a discord webhook to return to the menu...")
            print(Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN + "")

            urlcheck = "https://discord.com/api/webhooks/"

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
            print(Style.RESET_ALL, Fore.YELLOW + Style.BRIGHT, "How much XP do you need to get to the item you want?")
            try:
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.GREEN + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()

            xpa = xpai / 900
            xpau = (math.ceil(xpa))
            print(Style.RESET_ALL)
            print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN, "You need to complete",
                  Style.RESET_ALL + Fore.GREEN + str(xpau), "deathmatch games", Style.BRIGHT + "to get", xpai, "XP")

            print(Style.RESET_ALL)
            print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN, "This will take roughly",
                  Style.RESET_ALL + Fore.GREEN + str(xpau / 4), Style.BRIGHT + "hours of bot runtime")

            time.sleep(7)
            print(Style.RESET_ALL)
            main()

        elif menu == 5:
            os.startfile("restart.py")

        elif menu == 6:
            print(Style.BRIGHT + Fore.RED + " Closing the bot")
            time.sleep(1)
            quit()

        else:
            print(" Error 1: Enter a valid integer within the range 1 - 6!")
            time.sleep(2)
            main()


    except ValueError:
        print(" Error 2: You must enter an integer!")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
