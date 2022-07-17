# Please note; this project is now no longer updated. Please do not message me or add my discord about it, I wont respond. Thanks

# Valbot

[![Issues](https://img.shields.io/github/issues/MrFums/Valbot)](https://github.com/MrFums/Valbot/issues)
[![Forks](https://img.shields.io/github/forks/MrFums/Valbot)](https://github.com/MrFums/Valbot/network)
[![Stars](https://img.shields.io/github/stars/MrFums/Valbot)](https://github.com/MrFums/Valbot/stargazers)


**FAIR USE**

Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research.

Fair use is a use permitted by copyright statute that might otherwise be infringing. 

Non-profit, educational or personal use tips the balance in favor of fair use. 

## Important Notice:

Valbot is now DEPRECATED. Riot seems to have added, and are constantly improving, their AFK bot detection vectors. Valbot will not receive support or updates for the foreseeable future. Running the program is now considered unsafe and I do NOT recommend it. Some changes will also need to be made to the bot to accomodate the introdouction of the new game launcher; around line 270.


## Features

* Fully AFK XP farmer
* Discord RPC support
* Discord webhook support
* Optimized and has fail safes for events that may happen during runtime of the game
* Restarts Valorant if detects an issue with it / detects that it isn't running
* Automated restarts to prevent script from ending prematurely 
* Undetected 
* Easy navigation
* Can set XP targets and XP limits


## Requirements

Only works on 1920 x 1080 resolution. If you wish to make the bot work with a different resolution other than 1920 x 1080, you need to get your own version of the images for the bot to recognize. Read on how to do this [here](https://github.com/MrFums/Valbot/blob/master/information/change_resolution.txt).

Run the batch file as Administator to install the dependencies. 
Seems to only work on 64bit Windows 10 with Python 3.9 

For the program to function properly, please copy and paste your OWN Valorant shortcut for the program to function properly. This makes it so if Valorant encounters any issues when AFK, it can restart the game. You should not need to edit any code.

You also need a functioning brain, please have one of these; it's very important.

You should also read the [saftey precautions](https://github.com/MrFums/Valbot/blob/master/information/safetyprecautions.txt) to keep your account safe while running Valbot.

### Windows installation

You will have to have a few things installed before running Valbot. This installation guide assumes that you are on a 64bit Windows system.

First, you will need to install Python. It's recommended to use either version `3.9.0` or `3.8.6`. You must use a Python version above `3.7`. 

### Installing Python

Go to the following link and download Python:

[https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

Once you have opened the installer, make sure that you add Python to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/iefWNyw.png">

Run through the installer as normal, then download the Valbot files.


## Download

[Download here](https://github.com/MrFums/Valbot/releases/latest)

Click on the zip file that says `Valbot-X.X.X` and unzip to where you would like the bot to be stored. Be advised to not put this in an Admin only folder as the bot must write the folder it is in to manage the `config.ini` file it creates.


## Instructions

1- Install Python 3.9.0.

2- Open `PackageInstaller.bat` as admin to install pakcages using pip. Do this after every update to maintain functionality.

3- Open `Valbot.py` and read the bot console.

4- Navigate the menu and read the information.

5- Put your Valorant shortcut in the bots directory.

6- Follow the instructions that will appear on screen if you haven't already.

7- If you encounter issues please [create one](https://github.com/MrFums/ValBot/issues/new) or if you have suggestions please create a [pull request](https://github.com/MrFums/ValBot/compare)

8- (Optional) Setup a Discord webhook to get updates to your discord server for when the bot has completed a game.

## Valbot Premium

This version of the bot is a variant of Valbot that I work on in my free time. The updates or not guaranteed; think of it as my own private version. As a thank you for donating, you will be given access to this version of the bot and access to the private discord server.

Keep in mind that the premium build is not fully finished and is still being worked on. There is no promise that premium will continue to be updated as it is classed as a closed project. As it is classed as a donation, I will not accept any refund requests under any circumstances.


The minimum donation amount to gain access to *Valbot Premium* is 7USD / 6EUR / 5GBP __after fees__. Please keep in mind by donating you aren't "buying" access to Valbot Premium; it's merely a way of saying thank you for donating.

### Feature List
```
- Random mouse movements
- Humanised mouse movements
- Highly improved anti-afk system
- Most base features are rewritten
- XP Target (set how much XP you want and you will be tagged in Discord when this has been reached)
- XP Limit (set how much XP you want and then your computer will be shut down after reaching this)
- Improved restart function
- Toggle Discord Rich Presence
- Fallback image assets incase Valbot can't connect to GitHub
- Debug Discord webhook
- Better detections of current stage (kicked from game, invite screen appearing etc)
- Better front-end (includes submenus for XP options)
- Safe Cycle (run the bot for x amount of hours and pause for y amount of hours)
- Mute Valorant when in a match and unmute when in menu
- Sends a message when AFK in chat
- Force close Valbot hotkey (F5)
- Major Bugfixes
- Major optimization work
```


## Previews

![1](https://cdn.discordapp.com/attachments/805228393314516992/837761660265037854/unknown.png)
![2](https://cdn.discordapp.com/attachments/805228393314516992/837761751420239912/unknown.png)
![3](https://cdn.discordapp.com/attachments/805228393314516992/837762587671920717/unknown.png)
![4](https://cdn.discordapp.com/attachments/805228393314516992/837762620018524170/unknown.png)
