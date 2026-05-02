# 🧠 AI Research Intelligence System

> **Multi-Agent Academic Discovery Platform** powered by OpenRouter AI

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green?logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔬 Overview

A sophisticated **Multi-Agent AI Research System** that leverages **OpenRouter AI** (with Groq/DeepSeek models) to autonomously discover, analyze, and synthesize academic research from arXiv.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **4 Specialized Agents** | DeepAnalyzer, Synthesizer, Critic, and TrendPrediction agents |
| 📚 **arXiv Integration** | Access to millions of research papers |
| 🧠 **Deep Analysis** | AI-powered research analysis using OpenRouter API |
| 🎨 **Modern UI** | Clean, professional interface with responsive design |
| 📊 **Smart Relevance Scoring** | AI-powered paper filtering and ranking |
| 🔄 **Real-time Progress** | Live agent status and search progress tracking |

---

## � Meet the Team

<table>
  <tr>
    <th align="center">👤 Team Member</th>
    <th align="center">🎯 Role</th>
    <th align="center">📋 Contributions</th>
  </tr>
  <tr>
    <td align="center"><b>Muhammad Saad Umar</b></td>
    <td align="center">💡 Project Ideator & AI Engineer</td>
    <td>
      • Conceived the original project concept<br>
      • Designed & implemented multi-agent AI architecture<br>
      • Integrated OpenRouter API & AI models<br>
      • Developed intelligent research analysis algorithms
    </td>
  </tr>
  <tr>
    <td align="center"><b>Umme Rubab</b></td>
    <td align="center">🎨 UI/Frontend Developer & Presenter</td>
    <td>
      • Designed modern Streamlit user interface<br>
      • Created responsive layouts & visual components<br>
      • Implemented real-time progress indicators<br>
      • Prepared project presentation & demos
    </td>
  </tr>
  <tr>
    <td align="center"><b>Muhammad Fiaz</b></td>
    <td align="center">📐 System Designer & Documentation Lead</td>
    <td>
      • Architected system design & data flow<br>
      • Created comprehensive technical documentation<br>
      • Designed multi-agent orchestration patterns<br>
      • Authored README, SETUP & user guides
    </td>
  </tr>
  <tr>
    <td align="center"><b>Abdul Rehman</b></td>
    <td align="center">⚙️ Backend Developer & QA Engineer</td>
    <td>
      • Developed backend research orchestrator<br>
      • Implemented arXiv API integration<br>
      • Conducted end-to-end testing & debugging<br>
      • Ensured code quality & system reliability
    </td>
  </tr>
</table>

---

## �🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenRouter API Key ([Get one here](https://openrouter.ai/keys))
- Or Groq API Key ([Get one here](https://console.groq.com/))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/multi-agent-research-intelligence-system.git
cd multi-agent-research-intelligence-system

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
# Use OpenRouter (recommended)
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Or use Groq (alternative)
# GROQ_API_KEY=your_groq_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT UI (app.py)                    │
│              Modern Theme • Real-time Updates               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              RESEARCH ORCHESTRATOR                          │
│         (gemini3_research_system.py)                        │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐         │
│  │ DeepAnalyzer │ │  Synthesizer │ │    Critic    │         │
│  │    Agent     │ │    Agent     │ │    Agent     │         │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘         │
│         │                │                │                  │
│  ┌──────┴────────────────┴────────────────┴───────┐         │
│  │         TrendPrediction Agent                  │         │
│  └────────────────────────────────────────────────┘         │
│                          │                                   │
│  ┌───────────────────────┴────────────────────────┐         │
│  │              OPENROUTER AI API                 │         │
│  │              Deep Analysis Engine               │         │
│  └─────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATA SOURCE                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                      arXiv                           │   │
│  │          Open Access Academic Papers                 │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
project/
├── app.py                      # Streamlit UI application
├── gemini3_research_system.py  # Multi-agent orchestrator
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── DOCUMENTATION.md            # Technical documentation
├── SETUP.md                    # Setup guide
├── .env                        # API keys (create this)
├── run.bat                     # Windows launcher
├── run.sh                      # Linux/Mac launcher
├── setup.bat                   # Windows setup script
└── setup.sh                    # Linux/Mac setup script
```

---

## 🤖 Agent Descriptions

### 1. 🧠 DeepAnalyzer Agent
Analyzes individual papers deeply using OpenRouter AI for methodology evaluation, contribution assessment, and limitation identification.

### 2. 📚 Synthesizer Agent
Generates comprehensive literature reviews by synthesizing findings across all collected papers.

### 3. 🔍 Critic Agent
Identifies research gaps, unexplored areas, and potential future research directions.

### 4. 📈 TrendPrediction Agent
Predicts emerging research trends and provides forecasts based on analyzed papers.

---

## 🎨 UI Features

- **Modern Professional Theme** - Clean design with blue/purple gradients
- **Responsive Layout** - Works on various screen sizes
- **Real-time Agent Status** - Live tracking of agent activity
- **Paper Cards** - Beautiful cards with relevance scores and metadata
- **Tab Navigation** - Papers, Analysis, Literature, Gaps, Trends, Agents
- **Input Validation** - Minimum 3 character query validation
- **Tooltips** - Helpful tooltips on all interactive elements

---

## 🔧 Configuration Options

In the sidebar, you can configure:

- **Max Papers to Fetch**: 1-20 papers
- **Enable Deep Analysis**: Toggle AI analysis
- **Enable Literature Review**: Toggle synthesis
- **Enable Gap Analysis**: Toggle research gap identification
- **Enable Trend Prediction**: Toggle future trend analysis

---

## 📝 Example Usage

1. Enter a research topic (minimum 3 characters): *"transformer architectures for medical imaging"*
2. Click **🔬 Search Papers**
3. Watch as agents collect and analyze papers
4. Explore results across tabs:
   - 📄 **Papers** - Discovered papers with metadata
   - 🧠 **Analysis** - Deep AI analysis of each paper
   - 📚 **Literature** - Synthesized literature review
   - 🔍 **Gaps** - Identified research gaps
   - 📈 **Trends** - Predicted future trends
   - 🤖 **Agents** - Agent activity status

---

## 🛠️ Development

### Running the App

```bash
# Windows
run.bat

# Linux/Mac
./run.sh
```

### Setup

```bash
# Windows
setup.bat

# Linux/Mac
./setup.sh
```

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **OpenRouter** - For the AI API gateway
- **Groq** - For fast LLM inference
- **Streamlit** - For the rapid UI development framework
- **arXiv** - For providing open access to research papers

---

## Team Members

- **Project Manager:** Muhammad Fiaz
- **Full Stack Developer:** Abdul Rehman
- **AI / ML Engineer:** Muhammad Umar Saad
- **Pitch / Demo Lead:** Ume Rubab


<div align="center">

### 🌟 Developed with Passion by Team MARIS 🌟

**Muhammad Saad Umar** • **Umme Rubab** • **Muhammad Fiaz** • **Abdul Rehman**

---

**Built with ❤️ for Research Discovery**

🔬 *AI-powered academic research made simple*

</div>
