@echo off
echo Killing any process using port 6900...
for /f "tokens=5" %%a in ('netstat -ano ^| find "6900"') do (
    taskkill /f /pid %%a
)
rmdir /s /q "./API/__pycache__"
python API/server.py