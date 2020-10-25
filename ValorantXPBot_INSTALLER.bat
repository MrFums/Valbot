@echo off

if not exist "%SystemDrive%\ValorantXPBot\" mkdir "%SystemDrive%\ValorantXPBot" 

if exist "%SystemDrive%\ValorantXPBot\FumsXP.zip" (
del "%SystemDrive%\ValorantXPBot\FumsXP.zip"
)

echo Created a new installation folder, downloading required assets and the bot.


powershell -c "Invoke-WebRequest -Uri 'https://github.com/MrFums/ValorantBot/releases/download/2/FumsXP.zip' -OutFile '%SystemDrive%\ValorantXPBot\FumsXP.zip'"

powershell Expand-Archive -Force %SystemDrive%\ValorantXPBot\FumsXP.zip %SystemDrive%\ValorantXPBot\
del "%SystemDrive%\ValorantXPBot\FumsXP.zip"



echo.
echo.
echo.
echo This bot requires Python to run. Please download the latest python version.

timeout /t 3 /nobreak > NUL

echo Code written and tested in Python 3.8
echo Some people have errors using anything but Python 3.8. Please use Python 3.8
start https://www.python.org/downloads/release/python-380/
start https://github.com/MrFums/ValorantBot
echo.
timeout /t 3 /nobreak > NUL
echo Now downloading dependencies
timeout /t 1 /nobreak > NUL


echo.
echo.

py -m pip install --upgrade pip
py -m pip install pillow
py -m pip install pyautogui
py -m pip install opencv-python
py -m pip install psutil
py -m pip install colorama
py -m pip install winshell
py -m pip install pypiwin32


timeout /t 3 /nobreak > NUL
echo.
echo.
echo Generating a shortcut on your desktop
timeout /t 1 /nobreak > NUL
C:\ValorantXPBot\FumsXP\shortcut.py
echo.
echo.
echo Done! Enjoy the bot.





pause