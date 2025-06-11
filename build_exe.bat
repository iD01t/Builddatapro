@echo off
REM Build executable for Windows using PyInstaller
python -m pip install --upgrade pyinstaller >nul
pyinstaller --onefile --windowed app.py
ECHO Executable will be located in the dist folder.

