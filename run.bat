@echo off
setlocal

cd /d "%~dp0"
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    pause
    exit /b 1
)

python main.py

if errorlevel 1 (
    echo.
    echo main.py exited with an error.
    pause
)

endlocal