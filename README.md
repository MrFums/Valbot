# Valbot
[![Issues](https://img.shields.io/github/issues/MrFums/Valbot)](https://github.com/MrFums/Valbot/issues)
[![Forks](https://img.shields.io/github/forks/MrFums/Valbot)](https://github.com/MrFums/Valbot/network)
[![Stars](https://img.shields.io/github/stars/MrFums/Valbot)](https://github.com/MrFums/Valbot/stargazers)

If you have the crash when you load into the bot script / when you press 1 to begin the bot, you need to uninstall numpy ( `pip uninstall numpy` ) and install an older version of numpy: `pip install numpy==1.19.3`

## Changelog

### [1.8.0] - 29th January 2021

#### Changed
- Support for recent Valorant update / season
- Window Title
- Improved Discord Presence
- Fixed not detecting shortcut in root folder
- Fixed some minor and rare crashes
- Fixed play button detected


## Features

* Fully AFK XP farmer
* Discord RPC support
* Discord webhook support
* Optimized and has fail safes for events that may happen during runtime of the game
* Restarts Valorant if detects an issue with it / detects that it isn't running
* Automated restarts to prevent script from ending prematurely 
* Undetected / undetectable
* Easy navigation


## Requirements

Only works on 1920 x 1080 resolution. If you wish to add a custom resolution, you need to get your own version of the images from the `images` folder, call them EXACTLY the same name and replace the original files.

Run the batch file as Administator to install the dependencies. 
Seems to only work on 64bit Windows 10 with Python 3.8 

Install Python 3.8.0 [here](https://www.python.org/downloads/release/python-380/)

For the program to function properly, please copy and paste your OWN Valorant shortcut for the program to function properly. This makes it so if Valorant encounters any issues when AFK, it can restart the game. You should not need to edit any code.

You also need a functioning brain, please have one of these.


## Download

[Download here](https://github.com/MrFums/Valbot/releases/latest)

Click on the zip file that says `Valbot-X.X.X` and unzip to where you would like the bot to be stored. Be advised to not put this in an Admin only folder as the bot must write the folder it is in to store runtime data.

## Instructions

1- Install Python 3.8.0.

2- Open `Install_Packages.bat` as admin to install pakcages using pip. Do this after every update to maintain functionality.

3- Open `Valbot.py` and read the bot console.

4- Navigate the menu and read the information.

5- Put your Valorant shortcut in the bots directory.

6- Follow the instructions that will appear on screen if you haven't already.

7- If you encounter issues please [create one](https://github.com/MrFums/ValBot/issues/new) or if you have suggestions please create a [pull request](https://github.com/MrFums/ValBot/compare)

8- (Optional) Setup a Discord webhook to get updates to your discord server for when the bot has completed a game.


## Help

Make sure when installing python, you check the box next to "Add Python 3.8 to PATH"

![1](https://cdn.discordapp.com/attachments/769626861046202429/769950787304423444/0001_add_Python_to_Path.png)

In addition to this, if your program crashes and / or you have an error message that contains `psutil.AccessDenied`, you must download a different python version. ![image](https://user-images.githubusercontent.com/57535680/101982606-208ac800-3c6d-11eb-8a6a-964ae43c880b.png) [download here](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe)

Please raise an Issue [here](https://github.com/MrFums/ValBot/issues/new) if you have any problems. Do NOT message me on Discord, I will redirect you to the [issues](https://github.com/MrFums/ValBot/issues/new)

Please know that I will not be wasting time helping you if you can't read requirements or need help with Python code or installing it, Google is your friend.


## Previews

![1](https://cdn.discordapp.com/attachments/655191989305737256/775177788986359838/unknown.png)
![2](https://cdn.discordapp.com/attachments/655191989305737256/775178143987793930/unknown.png)
![3](https://cdn.discordapp.com/attachments/655191989305737256/775178335092867092/unknown.png)
