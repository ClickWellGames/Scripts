@echo off
echo Starting Day Counter...
start cmd /C pythonw.exe daycounterscHHH.pyw
echo Day Counter Started! Please close the new blank command window.
goto ask

:ask
set /p input= Press (Y/y) to stop the counter: 
if %input%==y (goto stop)
if %input%==Y (goto stop)
goto ask

:stop
echo Stopping Counter...
taskkill /IM pythonw.exe /F
exit

:noback
python.exe daycounterscHHH.py