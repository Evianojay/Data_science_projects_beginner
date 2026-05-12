@echo off
REM NYC Schools Analysis Runner
REM This script activates the virtual environment and runs the analysis script

echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment. Please ensure venv is set up.
    pause
    exit /b 1
)

echo Running analysis...
python analysis.py
if %errorlevel% neq 0 (
    echo Error: Analysis script failed to run.
    pause
    exit /b 1
)

echo Analysis completed successfully.
pause