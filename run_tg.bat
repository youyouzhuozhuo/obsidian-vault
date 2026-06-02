@echo off
cd /d "D:\Desktop\obsidian"
:restart
echo [%date% %time%] Starting tg_to_obsidian.py >> logs\tg.log 2>&1
python -u tg_to_obsidian.py >> logs\tg.log 2>&1
echo [%date% %time%] tg_to_obsidian.py exited, restarting in 10s... >> logs\tg.log 2>&1
timeout /t 10 /nobreak > nul
goto restart
