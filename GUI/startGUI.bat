@echo off
cd /d "%~dp0"
echo Killing any process using port 6969...
for /f "tokens=5" %%a in ('netstat -ano ^| find "6969" ^| find "LISTENING"') do (
    taskkill /f /pid %%a
)
echo Starting new web server...
python -m http.server 6969
