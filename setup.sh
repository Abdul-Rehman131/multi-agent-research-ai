#!/bin/bash
# ============================================
# AI Research Intelligence System
# Linux/Mac Setup Script
# ============================================

echo ""
echo "========================================"
echo "  AI Research Intelligence System"
echo "  SETUP SCRIPT"
echo "========================================"
echo ""

# Check Python version
echo "[1/5] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed!"
    echo "Please install Python 3.10+"
    exit 1
fi
python3 --version

# Create virtual environment
echo ""
echo "[2/5] Creating virtual environment..."
if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Skipping..."
else
    python3 -m venv .venv
    echo "Virtual environment created."
fi

# Activate virtual environment
echo ""
echo "[3/5] Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo ""
echo "[4/5] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check for .env file
echo ""
echo "[5/5] Checking configuration..."
if [ ! -f ".env" ]; then
    echo ""
    echo "[WARNING] .env file not found!"
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "========================================"
    echo "  IMPORTANT: Add your API key!"
    echo "========================================"
    echo ""
    echo "1. Open .env file"
    echo "2. Add your xAI (Grok) API key:"
    echo "   XAI_API_KEY=your_key_here"
    echo ""
    echo "Get your key at: https://console.x.ai/"
    echo ""
else
    echo ".env file found."
fi

echo ""
echo "========================================"
echo "  SETUP COMPLETE!"
echo "========================================"
echo ""
echo "To run the application:"
echo "  1. Make sure .env has your API key"
echo "  2. Run: ./run.sh"
echo ""
echo "Or manually:"
echo "  source .venv/bin/activate"
echo "  streamlit run app.py"
echo ""
