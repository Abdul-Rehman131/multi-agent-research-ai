@echo off
:: ============================================
:: AI Research Intelligence System
:: Windows Run Script
:: ============================================

echo.
echo ========================================
echo   AI Research Intelligence System
echo ========================================
echo.

:: Check if .venv exists
if not exist ".venv" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first.
    echo.
    pause
    exit /b 1
)

:: Check if .env exists
if not exist ".env" (
    echo [ERROR] .env file not found!
    echo Please copy .env.example to .env and add your API key.
    echo.
    pause
    exit /b 1
)

:: Activate virtual environment
echo [1/2] Activating virtual environment...
call .venv\Scripts\activate.bat

:: Run the app
echo [2/2] Starting Streamlit app...
echo.
echo ----------------------------------------
echo   Open: http://localhost:8501
echo   Press Ctrl+C to stop
echo ----------------------------------------
echo.

streamlit run app.py

pause
