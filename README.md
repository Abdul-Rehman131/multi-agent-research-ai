# 🧠 AI Research Intelligence System

> **Multi-Agent Academic Discovery Platform** powered by Google Gemini AI

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Gemini](https://img.shields.io/badge/Gemini-API-blue?logo=google)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔬 Overview

A sophisticated **Multi-Agent AI Research System** that leverages **Google Gemini AI** to autonomously discover, analyze, and synthesize academic research from arXiv.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **Multi-Agent System** | 6 specialized AI agents for comprehensive research analysis |
| 📚 **arXiv Integration** | Direct access to millions of academic research papers |
| 🧠 **Deep AI Analysis** | Advanced paper analysis using Google Gemini AI models |
| 📊 **Smart Relevance Scoring** | AI-powered paper filtering and ranking system |
| 🎨 **Modern UI/UX** | Professional Streamlit interface with responsive design |
| � **Real-time Progress** | Live agent status tracking and search progress |
| 📈 **Trend Prediction** | AI-driven research trend forecasting |
| 🔍 **Gap Analysis** | Automated identification of research gaps |
| 🕸️ **Network Graphs** | Interactive concept relationship visualization |
| � **AI Chat Interface** | Natural language interaction with research papers |
| 📄 **PDF Export** | Export literature reviews and analysis to PDF |
| 🎯 **Innovation Scoring** | Automated assessment of paper novelty and innovation |
| 📋 **Literature Synthesis** | AI-generated comprehensive literature reviews |
| 🔐 **API Integration** | Google Gemini AI integration for powerful analysis |
| 📱 **Responsive Design** | Works seamlessly on desktop, tablet, and mobile |
| 🎯 **Search Optimization** | Advanced filtering and search capabilities |

---

## 🧠 Meet the Team

<table>
  <tr>
    <th align="center">👤 Team Member</th>
    <th align="center">🎯 Role</th>
    <th align="center">📋 Contributions</th>
  </tr>
  <tr>
    <td align="center"><b>Hasseb</b></td>
    <td align="center">�‍💼 Project Manager</td>
    <td>
      • Led project planning and coordination<br>
      • Managed team resources and timelines<br>
      • Oversaw project delivery and quality assurance<br>
      • Coordinated stakeholder communication
    </td>
  </tr>
  <tr>
    <td align="center"><b>Abdul Rehman</b></td>
    <td align="center">⚙️ Full Stack Developer</td>
    <td>
      • Developed complete backend architecture<br>
      • Implemented multi-agent research orchestrator<br>
      • Created modern Streamlit user interface<br>
      • Integrated arXiv API and AI services
    </td>
  </tr>
  <tr>
    <td align="center"><b>Hussnain Dawood</b></td>
    <td align="center">🎥 Demo Video</td>
    <td>
      • Created comprehensive demo videos<br>
      • Produced tutorial and walkthrough content<br>
      • Designed visual presentations<br>
      • Managed video production and editing
    </td>
  </tr>
  <tr>
    <td align="center"><b>Sehreen Atta Gul</b></td>
    <td align="center">📚 Documentation</td>
    <td>
      • Authored comprehensive technical documentation<br>
      • Created user guides and API documentation<br>
      • Maintained project README and setup guides<br>
      • Documented system architecture and features
    </td>
  </tr>
</table>

---

## �🚀 Quick Start

### Prerequisites

- Python 3.10+
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

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
# Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here
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
│         Modern Theme • Real-time Updates • Responsive       │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│  │   Papers    │ │  Analysis   │ │ Literature  │ │  Gaps   │ │
│  │    Tab      │ │    Tab      │ │    Tab      │ │   Tab   │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│  │   Trends    │ │   Network   │ │   Chat      │ │ Agents  │ │
│  │    Tab      │ │    Tab      │ │    Tab      │ │   Tab   │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
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
│  ┌──────┴───────┐ ┌──────┴───────┐ ┌──────┴───────┐         │
│  │TrendPrediction│ │NetworkGraph  │ │PaperChat     │         │
│  │    Agent      │ │    Agent      │ │    Agent      │         │
│  └───────────────┘ └──────────────┘ └───────────────┘         │
│                          │                                   │
│  ┌───────────────────────┴────────────────────────┐         │
│  │              GOOGLE GEMINI AI API              │         │
│  │              Deep Analysis Engine               │         │
│  └─────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                      arXiv                           │   │
│  │          Open Access Academic Papers                 │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    PDF Export                       │   │
│  │          Literature Review Generation              │   │
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
Performs comprehensive analysis of individual research papers using Google Gemini AI for methodology evaluation, contribution assessment, innovation scoring, and limitation identification.

### 2. 📚 SynthesisAgent
Generates comprehensive literature reviews by synthesizing findings across all collected papers using Google Gemini AI with self-correction capabilities for hallucination detection.

### 3. 🔍 CriticAgent
Identifies research gaps, unexplored areas, contradictions in findings, and potential future research directions using Google Gemini AI's critical analysis capabilities.

### 4. 📈 TrendPredictionAgent
Predicts emerging research trends, forecasts future developments, and identifies promising research directions using Google Gemini AI-driven analysis.

### 5. 🕸️ NetworkGraphAgent
Creates interactive concept relationship visualizations, builds knowledge graphs showing paper connections, and identifies key research clusters using Google Gemini AI.

### 6. 💬 PaperChatAgent
Enables natural language interaction with research papers, answers questions about analyzed content, and provides intelligent paper discussions powered by Google Gemini AI.

---

## 🎨 UI Features

- **Modern Professional Theme** - Clean design with blue/purple gradients and animations
- **Fully Responsive Layout** - Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Agent Status** - Live tracking of all 6 agent activities with progress indicators
- **Interactive Paper Cards** - Beautiful cards with relevance scores, innovation metrics, and metadata
- **8-Tab Navigation** - Papers, Analysis, Literature, Gaps, Trends, Network, Chat, Agents
- **Smart Input Validation** - Minimum 3 character query validation with helpful error messages
- **Advanced Search & Filter** - Real-time paper filtering with multiple sort options
- **PDF Export Functionality** - Export literature reviews and analysis to PDF format
- **Interactive Network Graphs** - Visualize concept relationships and research clusters
- **AI Chat Interface** - Natural language conversation with analyzed papers
- **Progress Tracking** - Visual progress bars and novelty status indicators
- **Consistent Card Sizing** - Uniform layout across all UI components
- **Dark/Light Theme Support** - Professional color schemes for comfortable viewing

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
   - 🕸️ **Network** - Interactive concept relationship graphs
   - 💬 **Chat** - AI-powered paper discussion interface
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

- **Google Gemini** - For the powerful AI API and language models
- **Streamlit** - For the rapid UI development framework
- **arXiv** - For providing open access to research papers

---

## Team Members

- **Project Manager:** Hasseb
- **Full Stack Developer:** Abdul Rehman
- **ML/Demo Video:** Hussnain Dawood
- **Documentation/ppt:** Sehreen Atta Gul


<div align="center">

### 🌟 Developed with Passion by the Research Intelligence Team 🌟

**Hasseb** • **Abdul Rehman** • **Hussnain Dawood** • **Sehreen Atta Gul**

---

**Built with ❤️ for Advanced Research Discovery**

🔬 *Multi-Agent AI-powered academic research made simple*

📚 *Transforming how researchers discover, analyze, and synthesize academic literature*

</div>
