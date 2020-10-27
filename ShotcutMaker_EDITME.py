import os, winshell
from win32com.client import Dispatch




# run the following command in cmd:

# pip install winshell



desktop = winshell.desktop()
path = os.path.join(desktop, "Valbot.lnk") #name of the shortcut, not needed to be edited
target = ("C:\\ValorantXPBot\\bot.py") # where the python script is, change it to where your bot.py is located
wDir = ("C:\\ValorantXPBot\\") #The folder directory / working directory, change it to where your install folder is located
icon = ("C:\\ValorantXPBot\\icon.ico")# where the shortcut icon is, change it to where your icon.ico is located (same as bot.py)




shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()


