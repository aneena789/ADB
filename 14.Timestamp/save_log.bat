@echo off
:: Get current date and time
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do set d=%%c%%b%%a
for /f "tokens=1-2 delims=: " %%a in ("%time%") do set t=%%a%%b

:: Remove spaces and colons
set timestamp=%d%_%t%
set timestamp=%timestamp::=%
set timestamp=%timestamp: =0%

:: Save logcat to file
adb logcat -d > logcat_%timestamp%.txt

echo Log saved as logcat_%timestamp%.txt
pause
