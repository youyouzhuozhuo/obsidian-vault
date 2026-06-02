@echo off
cd /d "D:\Desktop\obsidian"
:restart
echo [%date% %time%] Starting process_wechat.py >> logs\wechat.log 2>&1
python -u process_wechat.py >> logs\wechat.log 2>&1
echo [%date% %time%] process_wechat.py exited, restarting in 10s... >> logs\wechat.log 2>&1
timeout /t 10 /nobreak > nul
goto restart
