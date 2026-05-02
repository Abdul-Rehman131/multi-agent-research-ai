#!/bin/bash
# ============================================
# AI Research Intelligence System
# Linux/Mac Run Script
# ============================================

echo ""
echo "========================================"
echo "  AI Research Intelligence System"
echo "========================================"
echo ""

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo "Please run ./setup.sh first."
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "[ERROR] .env file not found!"
    echo "Please copy .env.example to .env and add your API key."
    exit 1
fi

# Activate virtual environment
echo "[1/2] Activating virtual environment..."
source .venv/bin/activate

# Run the app
echo "[2/2] Starting Streamlit app..."
echo ""
echo "----------------------------------------"
echo "  Open: http://localhost:8501"
echo "  Press Ctrl+C to stop"
echo "----------------------------------------"
echo ""

streamlit run app.py
