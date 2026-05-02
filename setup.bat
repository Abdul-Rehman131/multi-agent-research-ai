@echo off
:: ============================================
:: AI Research Intelligence System
:: Windows Setup Script
:: ============================================

echo.
echo ========================================
echo   AI Research Intelligence System
echo   SETUP SCRIPT
echo ========================================
echo.

:: Check Python version
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)
python --version

:: Create virtual environment
echo.
echo [2/5] Creating virtual environment...
if exist ".venv" (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv .venv
    echo Virtual environment created.
)

:: Activate virtual environment
echo.
echo [3/5] Activating virtual environment...
call .venv\Scripts\activate.bat

:: Install dependencies
echo.
echo [4/5] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

:: Check for .env file
echo.
echo [5/5] Checking configuration...
if not exist ".env" (
    echo.
    echo [WARNING] .env file not found!
    echo Creating .env from .env.example...
    copy .env.example .env
    echo.
    echo ========================================
    echo   IMPORTANT: Add your API key!
    echo ========================================
    echo.
    echo 1. Open .env file
    echo 2. Add your xAI (Grok) API key:
    echo    XAI_API_KEY=your_key_here
    echo.
    echo Get your key at: https://console.x.ai/
    echo.
) else (
    echo .env file found.
)

echo.
echo ========================================
echo   SETUP COMPLETE!
echo ========================================
echo.
echo To run the application:
echo   1. Make sure .env has your API key
echo   2. Run: run.bat
echo.
echo Or manually:
echo   .venv\Scripts\activate
echo   streamlit run app.py
echo.

pause
