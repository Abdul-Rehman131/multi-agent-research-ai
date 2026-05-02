# 🚀 Quick Setup Guide

> Get the AI Research Intelligence System running in 5 minutes!

---

## 📋 Prerequisites

- **Python 3.10+** - [Download](https://python.org/downloads)
- **Google Gemini API Key** - [Get one free](https://aistudio.google.com/app/apikeys)
- **Git** - [Download](https://git-scm.com/downloads)

---

## ⚡ Quick Start

### Option 1: Automated Setup (Recommended)

#### Windows
```cmd
git clone https://github.com/YOUR_USERNAME/ai-research-intelligence.git
cd ai-research-intelligence
setup.bat
```

#### Linux/Mac
```bash
git clone https://github.com/YOUR_USERNAME/ai-research-intelligence.git
cd ai-research-intelligence
chmod +x setup.sh run.sh
./setup.sh
```

### Option 2: Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-research-intelligence.git
cd ai-research-intelligence

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp .env.example .env

# 6. Add your API key to .env
# Edit .env and add: GEMINI_API_KEY=your_key_here
```

---

## 🔑 Configure API Key

1. Open `.env` file in any text editor
2. Add your Google Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

**Get your key:** https://aistudio.google.com/app/apikeys

---

## 🏃 Run the Application

### Windows
```cmd
run.bat
```

### Linux/Mac
```bash
./run.sh
```

### Manual
```bash
streamlit run app.py
```

Then open: **http://localhost:8501**

---

## 📁 Project Structure

```
project/
├── app.py                    # 🖥️  Main Streamlit UI
├── gemini3_research_system.py # 🤖 Multi-agent orchestrator
├── requirements.txt          # 📦 Python dependencies
├── .env                      # 🔑 Your API key (create this)
├── .env.example              # 📋 Template for .env
├── setup.bat / setup.sh      # 🔧 Setup scripts
├── run.bat / run.sh          # 🚀 Run scripts
├── README.md                 # 📖 Project overview
└── DOCUMENTATION.md          # 📚 Technical docs
```

---

## 🔧 Troubleshooting

### "GEMINI_API_KEY not set"
- Create `.env` file from `.env.example`
- Add your Google Gemini API key to `.env`

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Python not found"
- Install Python 3.10+ from python.org
- Make sure Python is in your PATH

### "Permission denied" (Linux/Mac)
```bash
chmod +x setup.sh run.sh
```

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

---

## 📊 How to Use

1. **Enter a research topic** in the search box
   - Example: "transformer architectures for medical imaging"

2. **Configure options** in sidebar:
   - Max papers to fetch
   - Enable/disable analysis features

3. **Click "🔬 Search Papers"**

4. **Explore results** in tabs:
   - 📄 Papers - Found papers
   - 🧠 Analysis - AI analysis
   - 📚 Literature - Synthesized review
   - 🔍 Gaps - Research gaps
   - 📈 Trends - Future predictions

---

## 👥 Team Development

### Pull Latest Changes
```bash
git pull origin main
pip install -r requirements.txt
```

### Create a Branch
```bash
git checkout -b feature/your-feature
```

### Push Changes
```bash
git add .
git commit -m "Your message"
git push origin feature/your-feature
```

---

## 📞 Need Help?

1. Check [DOCUMENTATION.md](DOCUMENTATION.md) for technical details
2. Check [README.md](README.md) for project overview
3. Ask in team chat

---

**Happy Researching! 🔬**
