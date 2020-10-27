import time, os, psutil
from colorama import init
from colorama import Fore, Back, Style

class bot:
    def __innit__(self):
        self.restarted = 0
    
    
    
    def valorantrunning(self):
        found = False
        print(Fore.YELLOW,"Detecting if Valorant is running")
        print(Style.RESET_ALL)
        time.sleep(2)

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                
        if found == False:
            print(Fore.RED,"Can not find Valorant running")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print (Fore.GREEN,"Found Valorant running")
    
    def startvalorant(self):
        print(Fore.YELLOW,"Restarting Valorant")
        print(Style.RESET_ALL)
        os.startfile("Valorant.lnk")
        time.sleep(8)
        self.valorantrunning()
    
    
    
    
if __name__ == "__main__":
    
    a = bot()
    a.valorantrunning()