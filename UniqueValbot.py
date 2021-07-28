from uuid import uuid4
from random import randint
from colorama import Fore, Style
from colorama import init
from time import sleep
from os import system, path
init()

system('mode con: cols=85 lines=12')
print()
print(Fore.YELLOW, "FOR USE WITH VALBOT ")
print()
print(Fore.RED, Style.BRIGHT + "Running this program will add random comments to the bottom of your python files.")
print(" This will make it so the hashes and signature are different from everyone else.")
print(" You only will need to do this once per update of Valbot.\n")
print()
print (Style.RESET_ALL, Fore.RED+ "Press enter to begin or do CTRL + C to cancel")
print ()
print (Fore.BLACK)
input()

if path.exists('bot.py') and path.exists('valbot.py'):
    try:
        valbotpy = open('bot.py', 'a')
        for i in range(1,randint(2,20)):      
            rand = '#' + uuid4().hex + '\n'
            valbotpy.write(rand)
        valbotpy.close()
        print ()
        sleep(.5)
        print (Style.RESET_ALL + Fore.YELLOW, "File Valbot.py was made unique.")
        print ()


        
        botpy = open('valbot.py', 'a')
        
        for i in range(1,randint(2,20)):        
            rand = '#' + uuid4().hex + '\n'
            botpy.write(rand)
        botpy.close()
        print ()
        sleep(.5)
        print (Style.RESET_ALL + Fore.YELLOW, "File bot.py was made unique.")
        print ()
        sleep(.5)
        print()
        print (Style.RESET_ALL + Fore.GREEN, "Successfully made the files unique! Have fun!")
        input()
        
    except Exception as e:
        print (Style.RESET_ALL + Fore.RED, "Failed to update files.")
        print (Style.RESET_ALL + Fore.RED, e)
        print ()
        print (Style.RESET_ALL + Style.BRIGHT + Fore.RED, "Send this to Fums#0888")
        input()

else:
    print (Style.RESET_ALL + Fore.RED, "Failed to update files.")
    print ()
    print (Style.RESET_ALL + Style.BRIGHT + Fore.RED, "File(s) do not exist (Valbot.py or bot.py)")
    input()
    quit()
    

    
