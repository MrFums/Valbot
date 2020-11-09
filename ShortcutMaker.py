import os, winshell
from win32com.client import Dispatch

# IF YOU DO NOT UNDERSTAND THIS, HELP WILL NOT BE GIVEN FOR OBVIOUS REASONS.

desktop = winshell.desktop()
path = os.path.join(desktop, "Valbot.lnk") #name of the shortcut, not needed to be edited
target = ("C:\\Valbot\\main.py") # where the python script is, change it to where your bot.py is located
wDir = ("C:\\Valbot\\") #The folder directory / working directory, change it to where your install folder is located
icon = ("C:\\Valbot\\icon.ico")# where the shortcut icon is, change it to where your icon.ico is located (same as bot.py)

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
