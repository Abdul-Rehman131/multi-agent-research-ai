import streamlit as st
import time
import re
from datetime import datetime
import html

# --- Backend imports ---
from gemini3_research_system import ResearchOrchestrator

# ============================================
# 🎨 MODERN UI CONFIGURATION
# ============================================

st.set_page_config(
    page_title="🧠 AI Research Intelligence",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS - Premium Modern Theme ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Root variables for modern theme */
    :root {
        --primary-blue: #3b82f6;
        --primary-indigo: #6366f1;
        --primary-purple: #8b5cf6;
        --accent-cyan: #06b6d4;
        --accent-pink: #ec4899;
        --bg-primary: #ffffff;
        --bg-secondary: #f8fafc;
        --text-primary: #0f172a;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --hover-bg: #f1f5f9;
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #f0f9ff 100%);
    }
    
    /* Fix all text colors - ensure high contrast */
    body, p, span, div, li, h1, h2, h3, h4, h5, h6, label, a {
        color: var(--text-primary) !important;
    }
    
    /* Streamlit specific text fixes */
    .stMarkdown, .stMarkdown *, 
    [data-testid="stMarkdownContainer"] * {
        color: var(--text-primary) !important;
    }
    
    /* Expander text - high contrast */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] summary {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        background: white !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stExpander"] summary:hover {
        border-color: var(--primary-blue) !important;
        background: var(--hover-bg) !important;
        transform: translateX(4px) !important;
    }
    
    [data-testid="stExpander"] > div {
        color: var(--text-primary) !important;
        background: white !important;
        border: 2px solid var(--border-color) !important;
        border-top: none !important;
        border-radius: 0 0 12px 12px !important;
        padding: 20px !important;
    }
    
    /* Alert boxes with proper contrast */
    .stAlert {
        border-radius: 12px !important;
        border-left: 4px solid !important;
        padding: 16px !important;
    }
    
    .stAlert * {
        color: var(--text-primary) !important;
    }
    
    .stInfo {
        background: #eff6ff !important;
        border-color: #3b82f6 !important;
    }
    
    .stSuccess {
        background: #f0fdf4 !important;
        border-color: #22c55e !important;
    }
    
    .stWarning {
        background: #fffbeb !important;
        border-color: #f59e0b !important;
    }
    
    .stError {
        background: #fef2f2 !important;
        border-color: #ef4444 !important;
    }
    
    /* Links - proper blue color */
    a {
        color: var(--primary-blue) !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    
    a:hover {
        color: var(--primary-indigo) !important;
        text-decoration: underline !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary-blue) 0%, var(--primary-purple) 100%);
        border-radius: 10px;
        border: 3px solid #f1f5f9;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--primary-indigo) 0%, var(--primary-purple) 100%);
    }
    
    /* Main Header with Animation */
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -2px;
        animation: gradient-shift 5s ease infinite;
        text-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
    }
    
    @keyframes gradient-shift {
        0%, 100% {
            background: linear-gradient(135deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        50% {
            background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 50%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
    }
    
    .sub-header {
        font-family: 'Poppins', sans-serif;
        color: var(--text-secondary);
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 3rem;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* Modern Paper Cards */
    .paper-card {
        background: white;
        border: 2px solid var(--border-color);
        border-radius: 20px;
        padding: 32px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    .paper-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .paper-card:hover {
        border-color: var(--primary-blue);
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
    }
    
    .paper-card:hover::before {
        opacity: 1;
    }
    
    .paper-title {
        font-family: 'Poppins', sans-serif;
        color: var(--text-primary) !important;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 16px;
        line-height: 1.4;
        letter-spacing: -0.5px;
    }
    
    .paper-title a {
        color: var(--text-primary) !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }
    
    .paper-title a:hover {
        color: var(--primary-blue) !important;
    }
    
    .paper-meta {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        font-size: 0.95rem;
        font-weight: 500;
        margin-bottom: 20px;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 20px;
    }
    
    .paper-meta span {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: var(--text-secondary);
        background: var(--bg-secondary);
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .paper-abstract {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
        font-size: 1rem;
        font-weight: 400;
        line-height: 1.8;
        margin-bottom: 24px;
        padding: 24px;
        background: linear-gradient(135deg, #f0f9ff 0%, #faf5ff 100%);
        border-radius: 16px;
        border-left: 4px solid var(--primary-blue);
        word-wrap: break-word;
        overflow-wrap: break-word;
        white-space: pre-wrap;
    }
    
    /* Ensure no code/HTML shows in abstract */
    .paper-abstract code,
    .paper-abstract pre {
        display: none;
    }
    
    .paper-actions {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }
    
    .btn-action {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 24px;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        text-decoration: none !important;
        border-radius: 12px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border: none;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .btn-action::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .btn-action:hover::before {
        left: 100%;
    }
    
    .btn-view {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .btn-view:hover {
        background: #000000 !important;
        color: white !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transform: translateY(-3px);
    }
    
    .btn-pdf {
        background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);
        color: white !important;
        box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
    }
    
    .btn-pdf:hover {
        background: #000000 !important;
        color: white !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transform: translateY(-3px);
    }
    
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        margin-bottom: 16px;
    }
    
    .card-header h3.paper-title {
        margin: 0;
        flex: 1;
    }
    
    .source-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        padding: 10px 20px;
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        border-radius: 25px;
        color: white !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        white-space: nowrap;
        flex-shrink: 0;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    
    .source-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);
    }
    
    .meta-badge {
        padding: 8px 16px;
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        border-radius: 12px;
        color: white !important;
        font-size: 0.9rem;
        font-weight: 700;
        box-shadow: 0 4px 8px rgba(6, 182, 212, 0.2);
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .meta-badge:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 6px 12px rgba(6, 182, 212, 0.3);
    }
    
    .rel-badge {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.9rem;
        font-weight: 700;
        box-shadow: 0 4px 8px rgba(16, 185, 129, 0.2) !important;
        transition: all 0.3s ease;
    }
    
    .rel-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        margin: 40px 0;
    }
    
    .stat-card {
        background: white;
        border: 2px solid var(--border-color);
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
        border-color: var(--primary-blue);
    }
    
    .stat-card:hover::before {
        transform: scaleX(1);
    }
    
    .stat-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.3));
    }
    
    .stat-number {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 8px;
        border-radius: 16px;
        border: 2px solid var(--border-color);
        margin-bottom: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        background: transparent;
        border-radius: 12px;
        color: var(--text-secondary) !important;
        padding: 14px 28px;
        letter-spacing: 0.5px;
        font-size: 0.95rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        text-transform: uppercase;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--hover-bg);
        color: var(--primary-blue) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%) !important;
        color: white !important;
        border-color: transparent !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%) !important;
        border-radius: 10px !important;
        height: 10px !important;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.4) !important;
    }
    
    .stProgress > div > div {
        background: #e2e8f0 !important;
        border-radius: 10px !important;
        height: 10px !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border-right: 3px solid transparent;
        border-image: linear-gradient(180deg, #3b82f6 0%, #8b5cf6 100%) 1;
        box-shadow: 4px 0 20px rgba(59, 130, 246, 0.1);
    }
    
    section[data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 3px;
        height: 100%;
        background: linear-gradient(180deg, #3b82f6 0%, #8b5cf6 100%);
        opacity: 0.8;
    }
    
    section[data-testid="stSidebar"] * {
        color: var(--text-primary) !important;
    }
    
    section[data-testid="stSidebar"] label {
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        color: var(--text-primary) !important;
    }
    
    /* Sidebar Text Input */
    section[data-testid="stSidebar"] .stTextInput input {
        background: #ffffff !important;
        color: var(--text-primary) !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }
    
    /* Sidebar Checkboxes */
    section[data-testid="stSidebar"] .stCheckbox {
        padding: 2px 0 !important;
    }
    
    section[data-testid="stSidebar"] .stCheckbox label {
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
    }
    
    /* Sidebar Button */
    section[data-testid="stSidebar"] .stButton button {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-weight: 700;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        font-size: 0.85rem;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    section[data-testid="stSidebar"] .stButton button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover::before {
        left: 100%;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.5);
        transform: translateY(-2px);
    }
    
    /* Sidebar Slider */
    section[data-testid="stSidebar"] .stSlider {
        padding: 4px 0 !important;
    }
    
    .stSlider [data-baseweb="slider"] > div > div {
        background: #e2e8f0 !important;
        height: 6px !important;
    }
    
    .stSlider [data-baseweb="slider"] > div > div > div {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
    }
    
    .stSlider [role="slider"] {
        background: var(--primary-blue) !important;
        border: 3px solid white !important;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.4) !important;
        width: 20px !important;
        height: 20px !important;
    }
    
    .stSlider [role="slider"]:hover {
        transform: scale(1.2);
    }
    
    /* Sidebar Selectbox */
    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        padding: 8px 12px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    }
    
    section[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
        border-color: #94a3b8 !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06) !important;
    }
    
    section[data-testid="stSidebar"] [data-baseweb="select"] > div:focus-within {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12) !important;
    }
    
    /* Dropdown menu */
    div[role="listbox"],
    div[role="listbox"] ul {
        background-color: white !important;
    }
    
    div[role="listbox"] li[role="option"] {
        background-color: white !important;
        color: var(--text-primary) !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    
    div[role="listbox"] li[role="option"]:hover,
    div[role="listbox"] li[role="option"][aria-selected="true"] {
        background-color: var(--hover-bg) !important;
        color: var(--primary-blue) !important;
    }

    [data-baseweb="popover"],
    [data-baseweb="menu"] {
        background-color: white !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1) !important;
        z-index: 9999 !important;
    }
    
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] [role="option"] {
        background-color: white !important;
        color: var(--text-primary) !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    
    [data-baseweb="menu"] li:hover,
    [data-baseweb="menu"] [role="option"]:hover {
        background-color: var(--hover-bg) !important;
        color: var(--primary-blue) !important;
    }
    
    [data-baseweb="menu"] [aria-selected="true"] {
        background-color: #eff6ff !important;
        color: var(--primary-blue) !important;
        font-weight: 700 !important;
    }
    
    /* Fix for dropdown text visibility */
    [data-baseweb="select"] span,
    [data-baseweb="select"] div {
        color: var(--text-primary) !important;
    }
    
    /* Agent Cards */
    .agent-card {
        background: white;
        border: 2px solid var(--border-color);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .agent-card:hover {
        box-shadow: 0 12px 24px rgba(59, 130, 246, 0.15);
        border-color: var(--primary-blue);
        transform: translateY(-4px);
    }
    
    .agent-avatar {
        width: 70px;
        height: 70px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        flex-shrink: 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .agent-card:hover .agent-avatar {
        transform: scale(1.1) rotate(5deg);
    }
    
    .agent-running {
        background: linear-gradient(135deg, #ec4899 0%, #f43f5e 100%);
        animation: pulse-glow 2s ease-in-out infinite;
        color: white;
    }
    
    .agent-done {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }
    
    .agent-waiting {
        background: linear-gradient(135deg, #f1f5f9 0%, #e0e7ff 100%);
        border: 2px dashed #cbd5e1;
        color: #475569;
    }
    
    @keyframes pulse-glow {
        0%, 100% {
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.4);
        }
        50% {
            box-shadow: 0 0 40px rgba(236, 72, 153, 0.7);
        }
    }
    
    .agent-name {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
    }
    
    .agent-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: var(--text-secondary);
        margin: 4px 0 0 0;
    }
    
    .agent-status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        padding: 10px 20px;
        border-radius: 25px;
        margin-left: auto;
        flex-shrink: 0;
        font-weight: 700;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .status-running {
        background: linear-gradient(135deg, #ec4899 0%, #f43f5e 100%);
        color: white !important;
        box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
        animation: pulse-status 2s ease-in-out infinite;
    }
    
    .status-done {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    
    .status-waiting {
        background: #f1f5f9;
        color: #64748b !important;
        border: 2px solid #cbd5e1;
    }
    
    @keyframes pulse-status {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 100px 40px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f0f9ff 100%);
        border-radius: 24px;
        border: 2px dashed var(--border-color);
        margin: 20px 0;
        transition: all 0.3s ease;
    }
    
    .empty-state:hover {
        border-color: var(--primary-blue);
        border-style: solid;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.1);
    }
    
    .empty-state .icon {
        font-size: 6rem;
        margin-bottom: 24px;
        filter: drop-shadow(0 4px 12px rgba(59, 130, 246, 0.3));
        animation: float-icon 3s ease-in-out infinite;
    }
    
    @keyframes float-icon {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-10px) scale(1.05); }
    }
    
    .empty-state h3 {
        font-family: 'Poppins', sans-serif;
        color: var(--text-primary);
        font-size: 2rem;
        margin-bottom: 12px;
        font-weight: 800;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .empty-state p {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        font-size: 1.1rem;
        max-width: 400px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Glass Card */
    .glass-card {
        background: white;
        border: 2px solid var(--border-color);
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-color: var(--primary-blue);
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        color: var(--text-primary);
        margin-bottom: 24px;
        padding-bottom: 12px;
        border-bottom: 3px solid var(--primary-blue);
        font-weight: 700;
        display: inline-block;
    }
    
    /* Filter row container */
    .filter-container {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 2px solid var(--border-color);
        margin-bottom: 24px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .filter-container:hover {
        border-color: var(--primary-blue);
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.1);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: var(--primary-blue) !important;
    }
    
    /* Metric Cards */
    .stMetric {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid var(--border-color);
    }
    
    .stMetric label {
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: var(--primary-blue) !important;
        font-weight: 700 !important;
    }
    
    /* Sidebar collapse button - visible and styled */
    [data-testid="collapsedControl"] {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%) !important;
        border-radius: 0 12px 12px 0 !important;
        padding: 12px 10px !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="collapsedControl"]:hover {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%) !important;
        box-shadow: 0 6px 28px rgba(59, 130, 246, 0.6) !important;
        transform: scale(1.05);
    }
    
    [data-testid="collapsedControl"] svg {
        color: white !important;
        fill: white !important;
    }
    
    /* Main content inputs */
    .stTextInput input,
    .stSelectbox select {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
        color: var(--text-primary) !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
    }
    
    .stTextInput input:hover,
    .stSelectbox select:hover {
        border-color: #94a3b8 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
    }
    
    .stTextInput input:focus,
    .stSelectbox select:focus {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12), 0 2px 8px rgba(59, 130, 246, 0.1) !important;
        outline: none !important;
        background: #ffffff !important;
        caret-color: #0f172a !important;
    }
    
    .stTextInput input {
        caret-color: #0f172a !important;
    }
    
    .stTextInput input::placeholder {
        color: #94a3b8 !important;
        font-weight: 400 !important;
    }
    
    /* Main selectbox */
    [data-baseweb="select"] > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
    }
    
    [data-baseweb="select"] > div:hover {
        border-color: #94a3b8 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
    }
    
    [data-baseweb="select"] > div:focus-within {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12), 0 2px 8px rgba(59, 130, 246, 0.1) !important;
        background: #ffffff !important;
    }
    
    [data-baseweb="select"] svg {
        color: var(--primary-blue) !important;
        transition: transform 0.3s ease !important;
    }
    
    [data-baseweb="select"]:hover svg {
        transform: rotate(180deg) !important;
    }
    
    /* Input hover effects - already defined above */
    
    /* Button hover glow effect */
    .stButton button {
        position: relative;
        overflow: hidden;
    }
    
    .stButton button::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton button:hover::after {
        width: 300px;
        height: 300px;
    }
    
    /* Card stacking effect on hover */
    .glass-card {
        position: relative;
        z-index: 1;
    }
    
    .glass-card::after {
        content: '';
        position: absolute;
        top: 8px;
        left: 0;
        right: 0;
        bottom: -8px;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        border-radius: 16px;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .glass-card:hover::after {
        opacity: 1;
    }
    
    /* Hide "Press Enter to apply" hint in text inputs */
    .stTextInput div[data-testid="InputInstructions"] {
        display: none !important;
    }
    
    /* Chat Input Styling */
    .stChatInput textarea {
        background: white !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 16px !important;
        font-family: Inter, sans-serif !important;
        font-size: 1rem !important;
        padding: 16px !important;
        color: #0f172a !important;
        transition: all 0.3s ease !important;
    }
    .stChatInput textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
    }
    .stChatInput button {
        background: linear-gradient(135deg, #3b82f6, #6366f1) !important;
        border-radius: 12px !important;
    }
    
    /* Question Chip Styling */
    .question-chip {
        display: inline-block;
        padding: 10px 18px;
        margin: 6px;
        background: linear-gradient(135deg, #eff6ff 0%, #f5f3ff 100%);
        border: 2px solid #c7d2fe;
        border-radius: 25px;
        color: #4f46e5;
        font-family: Inter, sans-serif;
        font-weight: 600;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
    }
    .question-chip:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white;
        border-color: transparent;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    .chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin-bottom: 20px;
        padding: 16px;
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Fix for Streamlit Cloud ChatInput module loading issues
# This workaround prevents dynamic import errors on deployed instances
if 'chat_input_initialized' not in st.session_state:
    st.session_state.chat_input_initialized = True
    # Add retry mechanism for chat input component
    st.session_state.chat_retry_count = 0

# ============================================
# 🔧 BACKEND FUNCTIONS
# ============================================

def collect_papers(query, limit):
    orchestrator = ResearchOrchestrator(query)
    papers = orchestrator._fetch_arxiv(query, limit)
    papers = orchestrator._deduplicate_papers(papers)
    return papers

def analyze_papers(papers, orchestrator, deep=False):
    analyses = []
    for paper in papers[:10]:
        analysis = orchestrator.analyzer.analyze_paper_deeply(paper)
        paper['analysis'] = analysis
        analyses.append({
            'title': paper.get('title', ''),
            'main_idea': analysis.get('main_contribution', ''),
            'contribution': analysis.get('novel_aspects', []),
            'limitations': analysis.get('limitations', []),
            'novelty_score': analysis.get('technical_novelty', 0),
            'innovation_score': analysis.get('innovation_score', 0),
            'self_corrections': analysis.get('self_corrections', [])
        })
    return analyses

def synthesize_literature(papers, orchestrator):
    return orchestrator.synthesizer.synthesize_literature(papers)

def find_research_gaps(papers, orchestrator):
    return orchestrator.critic.identify_gaps_and_opportunities(papers)

def predict_trends(papers, orchestrator):
    return orchestrator.trends.predict_trends(papers)

def escape_html(text):
    """Safely escape HTML to prevent rendering issues"""
    if text is None:
        return ""
    text = str(text)
    # Escape HTML entities
    text = html.escape(text)
    # Remove backticks that cause code block rendering
    text = text.replace('`', '')
    # Remove any remaining problematic characters
    text = text.replace('```', '')
    return text

# ============================================
# 🎯 SESSION STATE
# ============================================

defaults = {
    'step': 0,
    'papers': [],
    'analyses': [],
    'literature': '',
    'gaps': {},
    'trends': {},
    'chat_history': [],
    'network_graph': {},
    'network_built': False,
    'agent_status': {},
    'error': None,
    'search_started': False,
    'orchestrator': None,
    'network_graph_enabled': True,
    'chat_enabled': True,
    'auto_build_network': False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================
# 🎨 SIDEBAR
# ============================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 8px 0; position: relative;">
        <div style="font-size: 2.2rem; margin-bottom: 4px; filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.4)); animation: float 3s ease-in-out infinite;">🧠</div>
        <h2 style="font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; font-size: 1.1rem; letter-spacing: 1.5px; font-weight: 900;">RESEARCH AI</h2>
        <p style="font-family: 'Inter', sans-serif; color: #64748b; font-size: 0.65rem; margin-top: 2px; letter-spacing: 0.5px; font-weight: 600;">POWERED BY ADVANCED AI</p>
    </div>
    <style>
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-4px); }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""<p style="font-family: Inter; color: #475569; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">🎓 Research Topic</p>""", unsafe_allow_html=True)
    query = st.text_input("Topic", placeholder="e.g., quantum computing, machine learning", label_visibility="collapsed")
    
    st.markdown("""<p style="font-family: Inter; color: #475569; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; margin-top: 12px;">📊 Papers Limit</p>""", unsafe_allow_html=True)
    limit = st.slider("Limit", 5, 15, 10, label_visibility="collapsed")
    
    st.markdown("""<p style="font-family: Inter; color: #475569; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; margin-top: 12px;">⚙️ Analysis Options</p>""", unsafe_allow_html=True)
    deep_analysis = st.checkbox("Deep Analysis", value=True, help="AI-powered in-depth paper analysis with innovation scoring")
    gap_analysis = st.checkbox("Gap Analysis", value=True, help="Identify research gaps and unexplored opportunities")
    trend_prediction = st.checkbox("Trends", value=True, help="Predict future research directions and emerging topics")
    quota_safe = st.checkbox("Lite Mode", value=False, help="Skip AI analysis to save API quota (papers only)")
    
    st.markdown("<hr style='border:1px solid #e2e8f0; margin:12px 0;'>", unsafe_allow_html=True)
    st.markdown('<p style="font-family:Inter; color:#475569; font-size:0.85rem; font-weight:600; margin-bottom:8px;">🕸️ Network & Chat Options</p>', unsafe_allow_html=True)
    
    network_graph_enabled = st.checkbox(
        "Network Graph", 
        value=True, 
        help="Build interactive concept network showing paper relationships",
        key="network_graph_checkbox"
    )
    chat_enabled = st.checkbox(
        "Chat with Papers", 
        value=True,
        help="Enable AI chat to ask questions about analyzed papers",
        key="chat_checkbox"
    )
    auto_build_network = st.checkbox(
        "Auto-Build Network", 
        value=False,
        help="Automatically build concept network after analysis (uses extra API calls)",
        key="auto_network_checkbox"
    )
    
    st.session_state.network_graph_enabled = network_graph_enabled
    st.session_state.chat_enabled = chat_enabled
    st.session_state.auto_build_network = auto_build_network
    
    st.markdown("<div style='margin-top: 12px; margin-bottom: 8px;'></div>", unsafe_allow_html=True)
    start_btn = st.button("⚡ LAUNCH RESEARCH", width='stretch', type="primary")
    
    if st.session_state.papers:
        st.markdown("---")
        st.markdown('<p style="font-family: Poppins; color: #3b82f6; font-size: 0.9rem; letter-spacing: 1px; font-weight: 700; margin-bottom: 12px;">📊 SESSION STATS</p>', unsafe_allow_html=True)
        num_papers = len(st.session_state.papers)
        num_sources = len(set(p.get('source', '') for p in st.session_state.papers))
        num_analyzed = len(st.session_state.analyses)
        sidebar_stats = '<div style="background: white; border: 2px solid #e2e8f0; border-radius: 14px; padding: 20px; margin-top: 12px;">'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-family: Inter;"><span style="color: #475569; font-weight: 600;">Papers</span><span style="color: #3b82f6; font-weight: 800; font-size: 1.1rem;">{num_papers}</span></div>'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-family: Inter;"><span style="color: #475569; font-weight: 600;">Sources</span><span style="color: #6366f1; font-weight: 800; font-size: 1.1rem;">{num_sources}</span></div>'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-family: Inter;"><span style="color: #475569; font-weight: 600;">Analyzed</span><span style="color: #8b5cf6; font-weight: 800; font-size: 1.1rem;">{num_analyzed}</span></div>'
        network_color = "#10b981" if st.session_state.get("network_built") else "#94a3b8"
        network_status = "✓ Built" if st.session_state.get("network_built") else "○ Pending"
        sidebar_stats += f'<div style="display:flex; justify-content:space-between; margin-bottom:12px; font-family:Inter;"><span style="color:#475569; font-weight:600;">Network</span><span style="color:{network_color}; font-weight:800; font-size:0.95rem;">{network_status}</span></div>'
        chat_qa = len(st.session_state.get("chat_history", [])) // 2
        sidebar_stats += f'<div style="display:flex; justify-content:space-between; font-family:Inter;"><span style="color:#475569; font-weight:600;">Chat Q&A</span><span style="color:#6366f1; font-weight:800; font-size:1.1rem;">{chat_qa}</span></div>'
        sidebar_stats += '</div>'
        st.markdown(sidebar_stats, unsafe_allow_html=True)

# ============================================
# 🎬 MAIN CONTENT
# ============================================

st.markdown('<h1 class="main-header">🔬 AI RESEARCH INTELLIGENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Multi-Agent Academic Discovery System</p>', unsafe_allow_html=True)

# Progress
if st.session_state.search_started:
    st.progress(min(st.session_state.step / 5, 1.0))

# ============================================
# 🔄 ORCHESTRATION
# ============================================

# Validation for empty query
if start_btn and not query:
    st.warning("⚠️ Please enter a research topic to search.")
elif start_btn and len(query.strip()) < 3:
    st.warning("⚠️ Search query must be at least 3 characters long.")
elif start_btn and query:
    # Validate query - remove special characters that might break search
    clean_query = query.strip()
    
    st.session_state.error = None
    st.session_state.step = 0
    st.session_state.search_started = True
    
    try:
        st.session_state.orchestrator = ResearchOrchestrator(clean_query)
    except Exception as e:
        st.session_state.error = f"❌ Failed to initialize research system: {str(e)}"
        st.session_state.search_started = False
    
    if st.session_state.search_started:
        import time
        if "agent_times" not in st.session_state:
            st.session_state.agent_times = {}
            
        try:
            st.session_state.agent_status = {"Collector": "running"}
            t0 = time.time()
            with st.spinner("🔍 Scanning arXiv for papers..."):
                st.session_state.papers = collect_papers(clean_query, limit)
            st.session_state.agent_status["Collector"] = "done"
            st.session_state.agent_times["Collector"] = round(time.time() - t0, 1)
            st.session_state.step = 1
            
            # Check if papers were found
            if not st.session_state.papers:
                st.session_state.error = "⚠️ No papers found for this query. Try different keywords."
            elif not quota_safe:
                st.session_state.agent_status["Analyzer"] = "running"
                t0 = time.time()
                with st.spinner("🧠 Deep analysis with advanced AI..."):
                    if deep_analysis:
                        st.session_state.analyses = analyze_papers(
                            st.session_state.papers, 
                            st.session_state.orchestrator, 
                            deep=True
                        )
                st.session_state.agent_status["Analyzer"] = "done"
                st.session_state.agent_times["Analyzer"] = round(time.time() - t0, 1)
                st.session_state.step = 2
                
                st.session_state.agent_status["Synthesis"] = "running"
                t0 = time.time()
                with st.spinner("📚 Synthesizing literature..."):
                    st.session_state.literature = synthesize_literature(
                        st.session_state.papers,
                        st.session_state.orchestrator
                    )
                st.session_state.agent_status["Synthesis"] = "done"
                st.session_state.agent_times["Synthesis"] = round(time.time() - t0, 1)
                st.session_state.step = 3
                
                if gap_analysis:
                    st.session_state.agent_status["Critic"] = "running"
                    t0 = time.time()
                    with st.spinner("🔍 Identifying gaps..."):
                        st.session_state.gaps = find_research_gaps(
                            st.session_state.papers,
                            st.session_state.orchestrator
                        )
                    st.session_state.agent_status["Critic"] = "done"
                    st.session_state.agent_times["Critic"] = round(time.time() - t0, 1)
                    st.session_state.step = 4
                
                if trend_prediction:
                    st.session_state.agent_status["Trends"] = "running"
                    t0 = time.time()
                    with st.spinner("📈 Predicting trends..."):
                        st.session_state.trends = predict_trends(
                            st.session_state.papers,
                            st.session_state.orchestrator
                        )
                    st.session_state.agent_status["Trends"] = "done"
                    st.session_state.agent_times["Trends"] = round(time.time() - t0, 1)
                    st.session_state.step = 5
                
                if st.session_state.auto_build_network and st.session_state.papers:
                    st.session_state.agent_status["Network"] = "running"
                    with st.spinner("🕸️ Auto-building concept network..."):
                        network_result = st.session_state.orchestrator.build_concept_network(
                            st.session_state.papers
                        )
                        st.session_state.network_graph = network_result
                        st.session_state.network_built = True
                    st.session_state.agent_status["Network"] = "done"
        
            st.rerun()
            
        except Exception as e:
            st.session_state.error = f"❌ Research failed: {str(e)}"
            st.session_state.agent_status = {}

# ============================================
# 📊 STATS
# ============================================

if st.session_state.papers:
    num_papers = len(st.session_state.papers)
    
    cols = st.columns(4)
    stats = [
        ("📄", num_papers, "Papers Found"),
        ("🌐", len(set(p.get('source', '') for p in st.session_state.papers)), "Data Sources"),
        ("🧠", len(st.session_state.analyses), "Deep Analyzed"),
        ("⚡", len(st.session_state.agent_status), "Active Agents")
    ]
    
    for col, (icon, num, label) in zip(cols, stats):
        with col:
            stat_html = f'<div class="stat-card"><div class="stat-icon">{icon}</div><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>'
            st.markdown(stat_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# 📑 TABS
# ============================================

tabs = st.tabs(["📄 Papers", "🧠 Analysis", "📚 Literature", "🔍 Gaps", "📈 Trends", "🕸️ Network", "💬 Ask Papers", "🤖 Agents"])

# --- Papers Tab ---
with tabs[0]:
    if st.session_state.error:
        st.error(st.session_state.error)
    elif st.session_state.papers:
        st.markdown('<div class="filter-container">', unsafe_allow_html=True)
        search_filter = st.text_input("🔍 Search", placeholder="Search by title, author, or keywords...", label_visibility="collapsed", key="search_papers")
        st.markdown('</div>', unsafe_allow_html=True)
        
        filtered_papers = list(st.session_state.papers)
        if search_filter:
            filtered_papers = [p for p in filtered_papers if search_filter.lower() in p.get('title', '').lower() or search_filter.lower() in p.get('summary', '').lower()]
        
        # Sort dropdown
        sort_col1, sort_col2 = st.columns([3, 1])
        with sort_col2:
            st.markdown('<div style="font-size: 0.8rem; color: #475569; margin-bottom: 4px; position: relative; z-index: 10;">Sort by:</div>', unsafe_allow_html=True)
            sort_option = st.selectbox("Sort by", ["Relevance", "Date", "Innovation Score"], label_visibility="collapsed")
            
        if sort_option == "Relevance":
            filtered_papers.sort(key=lambda p: float(p.get('relevance_score', 0) or 0), reverse=True)
        elif sort_option == "Date":
            filtered_papers.sort(key=lambda p: p.get('published', '') or '', reverse=True)
        elif sort_option == "Innovation Score":
            filtered_papers.sort(key=lambda p: p.get('analysis', {}).get('innovation_score', 0) if isinstance(p.get('analysis'), dict) else 0, reverse=True)

        # Show filtered count and query info
        total_papers = len(st.session_state.papers)
        filtered_count = len(filtered_papers)
        query_text = st.session_state.get('query', 'your query')
        
        if search_filter:
            st.markdown(f'''
            <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 10px 16px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                <span style="color: #0284c7; font-weight: 600; font-family: Inter;">🔎 Showing {filtered_count} of {total_papers} papers</span>
                <span style="color: #64748b; font-size: 0.9rem;">matching "{search_filter}" for "{escape_html(query_text)}"</span>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 10px 16px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                <span style="color: #0284c7; font-weight: 600; font-family: Inter;">🔎 Showing {total_papers} papers for:</span>
                <span style="color: #64748b; font-size: 0.9rem;">"{escape_html(query_text)}"</span>
            </div>
            ''', unsafe_allow_html=True)
        
        if not filtered_papers:
            st.info("No papers match your filter criteria. Try adjusting your search.")
        
        for i, paper in enumerate(filtered_papers):
            # Extract basic info
            title = paper.get('title', 'Untitled')
            authors_list = paper.get('authors', [])[:3]
            authors = ', '.join(authors_list) if authors_list else 'Unknown'
            if len(paper.get('authors', [])) > 3:
                authors += f" +{len(paper.get('authors', [])) - 3} more"
            
            pub_date = paper.get('published', '')[:10] if paper.get('published') else 'N/A'
            
            # Get clean summary text
            summary_text = paper.get('summary', '') or ''
            if summary_text:
                # Clean the summary - remove any HTML tags or special characters
                import re
                # Remove any HTML tags that might be present
                summary_text = re.sub(r'<[^>]+>', '', str(summary_text))
                # Remove any remaining angle brackets
                summary_text = summary_text.replace('<', '').replace('>', '')
                if len(summary_text) > 400:
                    summary_text = summary_text[:400] + '...'
            
            source_name = paper.get('source', 'Unknown')
            paper_link = paper.get('link', '#')
            pdf_link = paper.get('pdf_link', '')
            
            # Citations badge
            citations = paper.get('citation_count', 0)
            citations_badge = ''
            if citations and citations > 0:
                citations_badge = f'<span class="meta-badge">📊 {citations} citations</span>'
            
            # Relevance badge - always show if relevance > 0
            relevance = paper.get('relevance_score', 0)
            relevance_badge = ''
            
            try:
                rel_val = float(relevance)
                if rel_val > 0:
                    display_rel = int(rel_val * 100) if rel_val <= 1.0 else int(rel_val)
                    relevance_badge = f'<span class="rel-badge">🎯 {display_rel}%</span>'
            except (ValueError, TypeError):
                pass
            
            # PDF button
            pdf_button = ''
            if pdf_link:
                pdf_button = f'<a href="{pdf_link}" target="_blank" class="btn-action btn-pdf">📄 PDF</a>'
            
            # Build clean HTML card - use proper string concatenation to avoid markdown parsing issues
            abstract_text = escape_html(summary_text) if summary_text else "No abstract available."
            card_html = '<div class="paper-card" style="position: relative; margin-top: 15px;">'
            card_html += f'<div style="position: absolute; top: -12px; left: -12px; width: 28px; height: 28px; background: #0284c7; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: bold; border: 2px solid white; z-index: 10; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">#{i+1}</div>'
            card_html += '<div class="card-header">'
            card_html += f'<h3 class="paper-title" style="margin-left: 8px;">{escape_html(title)}</h3>'
            card_html += f'<span class="source-badge">{escape_html(source_name)}</span>'
            card_html += '</div>'
            card_html += '<div class="paper-meta">'
            card_html += f'<span>👥 {escape_html(authors)}</span>'
            card_html += f'<span>📅 {pub_date}</span>'
            card_html += citations_badge
            card_html += relevance_badge
            card_html += '</div>'
            card_html += f'<p class="paper-abstract">{abstract_text}</p>'
            card_html += '<div class="paper-actions">'
            card_html += f'<a href="{paper_link}" target="_blank" class="btn-action btn-view">🔗 View Paper</a>'
            card_html += pdf_button
            card_html += '</div>'
            card_html += '</div>'
            
            st.markdown(card_html, unsafe_allow_html=True)
    elif st.session_state.search_started:
        # Search was attempted but no papers found
        empty_html = '''
        <div class="empty-state">
            <div class="icon">⚠️</div>
            <h3>Unable to Fetch Papers</h3>
            <p>No papers were found for your search query. Please try a different topic or check your internet connection.</p>
        </div>
        '''
        st.markdown(empty_html, unsafe_allow_html=True)
    else:
        empty_html = '''
        <div class="empty-state">
            <div class="icon">🔬</div>
            <h3>Ready to Discover</h3>
            <p>Enter a research topic in the sidebar and click "Launch Research" to begin your AI-powered academic exploration</p>
        </div>
        '''
        st.markdown(empty_html, unsafe_allow_html=True)

# --- Analysis Tab ---
with tabs[1]:
    if st.session_state.analyses:
        for i, a in enumerate(st.session_state.analyses, 1):
            with st.expander(f"📊 Analysis {i}: {a.get('title', f'Paper {i}')[:70]}...", expanded=(i==1)):
                
                # Check for research category
                category = a.get('research_category')
                if category:
                    st.markdown(f'<div style="display:inline-block; background-color:#8b5cf6; color:white; padding:4px 12px; border-radius:12px; font-size:0.8rem; font-weight:bold; margin-bottom:12px;">{escape_html(str(category))}</div>', unsafe_allow_html=True)
                
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**🎯 Main Contribution**")
                    st.info(a.get('main_idea', 'Not analyzed'))
                    st.markdown("**💡 Novel Aspects**")
                    aspects = a.get('contribution', [])
                    if isinstance(aspects, list):
                        for asp in aspects[:3]:
                            st.markdown(f"• {asp}")
                    else:
                        st.markdown(f"• {aspects}")
                with c2:
                    st.markdown("**⚠️ Limitations**")
                    lims = a.get('limitations', [])
                    if isinstance(lims, list):
                        for lim in lims[:3]:
                            st.markdown(f"• {lim}")
                    else:
                        st.markdown(f"• {lims}")
                    st.markdown("**📈 Innovation Score**")
                    sc1 = st.columns(1)[0]
                    
                    # Score Progress Bar
                    title = "Innovation"
                    key = 'innovation_score'
                    with sc1:
                        try:
                            score = float(a.get(key, 0))
                        except:
                            score = 0
                        
                        color = "red" if score < 5 else "orange" if score < 8 else "green"
                        st.markdown(f'<span style="color:{color}; font-weight:bold; font-size:0.9rem;">{score}/10 {title}</span>', unsafe_allow_html=True)
                        
                        # Custom progress bar html to support raw colors directly in basic Streamlit
                        bar_width = min(max(int(score * 10), 0), 100)
                        color_hex = "#ef4444" if score < 5 else "#f97316" if score < 8 else "#22c55e"
                        
                        st.markdown(f'''
                        <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 8px; margin-bottom: 12px; overflow: hidden;">
                            <div style="width: {bar_width}%; background-color: {color_hex}; height: 100%; border-radius: 4px;"></div>
                        </div>
                        ''', unsafe_allow_html=True)
                
                # Confidence Indicator
                confidence = a.get('confidence_in_analysis', 0.5)
                color = "#10b981" if confidence > 0.7 else "#f59e0b" if confidence > 0.4 else "#ef4444"
                label = "High Confidence" if confidence > 0.7 else "Medium" if confidence > 0.4 else "Low"
                
                st.markdown(f'<div style="color:{color}; font-weight:700; margin-top:16px; margin-bottom:16px;">● {label} Analysis ({int(confidence*100)}% confidence)</div>', unsafe_allow_html=True)

                if a.get('self_corrections'):
                    st.markdown("---")
                    st.markdown("**🔄 Self Corrections**")
                    corrections = a.get('self_corrections', [])
                    if isinstance(corrections, list):
                        for c in corrections:
                            st.warning(c, icon="🔄")
                    else:
                        st.warning(corrections, icon="🔄")
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">🧠</div>
            <h3>No Analysis Yet</h3>
            <p>Enable "Deep Analysis" in the sidebar and run a search to see detailed paper analysis</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Literature Tab ---
with tabs[2]:
    if st.session_state.literature:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown('<div class="section-header">📚 AI-Generated Literature Review</div>', unsafe_allow_html=True)
            
        lit = st.session_state.literature
        
        # Helper function to clean text
        def clean_lit_text(text):
            if not text:
                return ""
            text = str(text)
            # Remove markdown code blocks
            text = text.replace('```json', '').replace('```python', '').replace('```', '')
            # Remove literal \n
            text = text.replace('\\n', '\n')
            return text.strip()
        
        # Parse the literature content
        lit_data = None
        if isinstance(lit, dict):
            # Check for expected keys from the backend
            if 'title' in lit or 'introduction' in lit or 'major_research_themes' in lit:
                # This is the correct structure from backend
                lit_data = lit
            elif 'deep_synthesis_analysis' in lit:
                lit_data = lit.get('deep_synthesis_analysis', lit)
            elif 'summary_report' in lit:
                lit_data = lit.get('summary_report', lit)
            elif 'raw_response' in lit and lit.get('parsing_error'):
                # Just display raw text
                raw_text = clean_lit_text(lit.get('raw_response', ''))
                st.info(raw_text if raw_text else "No content available")
                lit_data = None
            else:
                lit_data = lit
        else:
            # String content - try to parse as JSON first
            try:
                import json
                parsed_json = json.loads(str(lit))
                if isinstance(parsed_json, dict) and ('title' in parsed_json or 'introduction' in parsed_json or 'major_research_themes' in parsed_json):
                    lit_data = parsed_json
                else:
                    st.info(clean_lit_text(str(lit)))
                    lit_data = None
            except (json.JSONDecodeError, TypeError):
                # Not valid JSON, display as plain text
                st.info(clean_lit_text(str(lit)))
                lit_data = None
            
        if lit_data and isinstance(lit_data, dict):
            # Extract fields (gaps and future directions are shown in Gaps tab only)
            title = lit_data.get('title', 'Literature Review')
            intro = lit_data.get('introduction', lit_data.get('overview', lit_data.get('summary', '')))
            themes = lit_data.get('major_research_themes', lit_data.get('themes', []))
            evolution = lit_data.get('evolution_of_ideas', lit_data.get('evolution', ''))
            contradictions = lit_data.get('contradictions', '')
            conclusion = lit_data.get('conclusion', lit_data.get('synthesis', ''))
            
            # Word count calculation
            all_text = " ".join([str(intro), str(themes), str(evolution), str(contradictions), str(conclusion)])
            word_count = len(all_text.split())
            
            import io
            from fpdf import FPDF
            
            class LitPDF(FPDF):
                def header(self):
                    self.set_font('Arial', 'B', 10)
                    self.set_text_color(100, 100, 100)
                    self.cell(0, 10, 'Literature Review', 0, 1, 'C')
                
                def prepare_text(self, text):
                    # FPDF1 doesn't support full unicode using Arial. We convert safely.
                    return text.encode('latin-1', 'replace').decode('latin-1')

                def chapter_title(self, title):
                    self.set_font('Arial', 'B', 14)
                    self.set_text_color(0, 51, 102)
                    self.cell(0, 10, self.prepare_text(title), 0, 1, 'L')
                    self.ln(2)
                
                def chapter_body(self, text):
                    self.set_font('Arial', '', 11)
                    self.set_text_color(0, 0, 0)
                    self.multi_cell(0, 6, self.prepare_text(text))
                    self.ln(4)

            # Generate PDF
            pdf = LitPDF()
            pdf.add_page()
            pdf.set_font('Arial', 'B', 18)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 10, pdf.prepare_text(clean_lit_text(title)))
            pdf.ln(5)
            
            if intro:
                pdf.chapter_title('Overview')
                pdf.chapter_body(clean_lit_text(intro))
            if themes:
                pdf.chapter_title('Major Research Themes')
                theme_list = themes if isinstance(themes, list) else [themes]
                for i, theme in enumerate(theme_list[:6], 1):
                    theme_text = theme.get('theme', theme) if isinstance(theme, dict) else str(theme)
                    pdf.chapter_body(f"{i}. {clean_lit_text(theme_text)}")
            if evolution:
                pdf.chapter_title('Evolution of Research')
                pdf.chapter_body(clean_lit_text(evolution))
            if contradictions:
                pdf.chapter_title('Key Debates & Contradictions')
                pdf.chapter_body(clean_lit_text(contradictions))
            if conclusion:
                pdf.chapter_title('Synthesis & Conclusion')
                pdf.chapter_body(clean_lit_text(conclusion))
                
            pdf_bytes = pdf.output(dest='S').encode('latin-1')

            with col2:
                st.download_button(
                    label="📄 Export PDF",
                    data=pdf_bytes,
                    file_name="Literature_Review.pdf",
                    mime="application/pdf",
                    help="Export this literature review as a PDF document"
                )
            
            # Title
            st.markdown(f"### 📖 {clean_lit_text(title)}")
            st.markdown(f'<p style="color: #64748b; font-size: 0.9rem; margin-top: -10px;">AI-synthesized analysis • ~{word_count} word review generated</p>', unsafe_allow_html=True)
            st.divider()
            
            # Overview
            if intro:
                with st.container():
                    st.markdown('<div style="border-left: 4px solid #3b82f6; padding-left: 16px; margin-bottom: 20px;"><h4 style="margin-top: 0; color: #0f172a;">📝 Overview</h4></div>', unsafe_allow_html=True)
                    st.markdown(clean_lit_text(intro))
                    st.markdown("")
            
            # Research Themes
            if themes:
                st.markdown('<div style="border-left: 4px solid #8b5cf6; padding-left: 16px; margin-bottom: 20px;"><h4 style="margin-top: 0; color: #0f172a;">🎯 Major Research Themes</h4></div>', unsafe_allow_html=True)
                theme_list = themes if isinstance(themes, list) else [themes]
                
                # Create a more structured display
                for i, theme in enumerate(theme_list[:6], 1):
                    if isinstance(theme, dict):
                        # Handle dictionary format
                        theme_text = theme.get('theme', str(theme))
                        theme_desc = theme.get('description', '')
                    else:
                        # Handle string format - split by colon to separate title and description
                        theme_str = str(theme)
                        if ':' in theme_str:
                            parts = theme_str.split(':', 1)
                            theme_text = parts[0].strip()
                            theme_desc = parts[1].strip()
                        else:
                            theme_text = theme_str
                            theme_desc = ''
                    
                    # Clean up the text
                    theme_text = clean_lit_text(theme_text)
                    theme_desc = clean_lit_text(theme_desc) if theme_desc else ''
                    
                    # Build description HTML if it exists
                    desc_html = ""
                    if theme_desc:
                        desc_html = f'<div style="color: #475569; font-size: 0.9rem; line-height: 1.5; margin-top: 8px;">{theme_desc}</div>'
                    
                    # Create theme card
                    theme_card = f'''
                    <div style="border: 2px solid #e2e8f0; border-radius: 12px; padding: 16px; background: linear-gradient(135deg, #f5f3ff 0%, #eff6ff 100%); margin-bottom: 12px;">
                        <div style="display: flex; gap: 16px;">
                            <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; flex-shrink: 0; min-width: 32px;">{i}</div>
                            <div style="flex: 1;">
                                <div style="font-weight: 700; color: #0f172a; font-size: 1rem;">{theme_text}</div>
                                {desc_html}
                            </div>
                        </div>
                    </div>
                    '''
                    st.markdown(theme_card, unsafe_allow_html=True)
            
            # Evolution
            if evolution:
                st.markdown('<div style="border-left: 4px solid #06b6d4; padding-left: 16px; margin-bottom: 20px;"><h4 style="margin-top: 0; color: #0f172a;">📈 Evolution of Research</h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="background: linear-gradient(135deg, #cffafe 0%, #f0f9ff 100%); padding: 16px; border-radius: 12px; border-left: 4px solid #06b6d4; color: #0f172a; line-height: 1.6;">{clean_lit_text(evolution)}</div>', unsafe_allow_html=True)
                st.markdown("")
            
            # Contradictions
            if contradictions:
                st.markdown('<div style="border-left: 4px solid #ec4899; padding-left: 16px; margin-bottom: 20px;"><h4 style="margin-top: 0; color: #0f172a;">⚡ Key Debates & Contradictions</h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="background: linear-gradient(135deg, #fef3c7 0%, #fef08a 100%); padding: 16px; border-radius: 12px; border-left: 4px solid #ec4899; color: #0f172a; line-height: 1.6;">{clean_lit_text(contradictions)}</div>', unsafe_allow_html=True)
                st.markdown("")
            
            # Conclusion
            if conclusion:
                st.markdown('<div style="border-left: 4px solid #3b82f6; padding-left: 16px; margin-bottom: 20px;"><h4 style="margin-top: 0; color: #0f172a;">📋 Synthesis & Conclusion</h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%); padding: 16px; border-radius: 12px; border-left: 4px solid #3b82f6; color: #0f172a; line-height: 1.6;">{clean_lit_text(conclusion)}</div>', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">📚</div>
            <h3>No Literature Review</h3>
            <p>Run Deep Analysis to generate a comprehensive literature review</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Gaps Tab ---
with tabs[3]:
    if st.session_state.gaps:
        gaps = st.session_state.gaps
        
        # Handle error responses from AI
        if isinstance(gaps, dict) and gaps.get('error'):
            error_msg = gaps.get('error', 'Unknown error')
            if gaps.get('rate_limited'):
                st.warning("🚫 **API Rate Limit Reached**\n\nPlease wait a moment and try again, or add credits to your API account.")
            elif gaps.get('auth_error'):
                st.error("🔑 **API Authentication Error**\n\n" + error_msg)
            else:
                st.error(f"⚠️ Gap analysis failed: {error_msg}")
        elif isinstance(gaps, dict) and gaps.get('parsing_error'):
            # Display raw response if parsing failed
            raw_text = gaps.get('raw_response', str(gaps))
            st.markdown(f'''
            <div class="glass-card" style="padding: 24px;">
                <h3 style="color: #ec4899; margin-bottom: 16px;">🔍 Research Gap Analysis</h3>
                <p style="color: #1e293b; line-height: 1.8;">{escape_html(raw_text)}</p>
            </div>
            ''', unsafe_allow_html=True)
        elif isinstance(gaps, dict):
            c1, c2 = st.columns(2)
            with c1:
                with st.container(height=500):
                    st.markdown('<div class="section-header">🎯 Research Gaps</div>', unsafe_allow_html=True)
                    major_gaps = gaps.get('major_gaps', [])
                    if major_gaps:
                        for gap in major_gaps[:5]:
                            if isinstance(gap, dict):
                                difficulty_html = ""
                                if gap.get('difficulty'):
                                    try:
                                        dif_val = int(gap['difficulty'])
                                        d_color = "#ef4444" if dif_val >= 7 else "#f59e0b" if dif_val >= 4 else "#10b981"
                                        d_label = "Hard" if dif_val >= 7 else "Medium" if dif_val >= 4 else "Easy"
                                        icon = "🔥" if dif_val >= 7 else "⚡" if dif_val >= 4 else "🌱"
                                        difficulty_html = f'<div style="display:inline-block; padding:2px 8px; border-radius:12px; background:{d_color}20; color:{d_color}; font-size:0.8rem; font-weight:600; margin-top:8px;">{icon} {d_label} ({dif_val}/10)</div>'
                                    except:
                                        pass
                                
                                gap_html = f'''
                                <div class="glass-card" style="height: 100%;">
                                    <strong style="color: #ec4899; font-size: 1.1rem;">{escape_html(str(gap.get("gap", "")))}</strong>
                                    {difficulty_html}
                                    <p style="color: #475569; margin-top: 12px; line-height: 1.6;">{escape_html(str(gap.get("why_important", "")))}</p>
                                </div>
                                '''
                                st.markdown(gap_html, unsafe_allow_html=True)
                            else:
                                st.info(str(gap))
                    else:
                        st.info("No major gaps identified in the analysis.")
            with c2:
                with st.container(height=500):
                    st.markdown('<div class="section-header">🚀 Future Directions</div>', unsafe_allow_html=True)
                    future_dirs = gaps.get('future_directions', [])
                    if future_dirs:
                        for d in future_dirs[:5]:
                            if isinstance(d, dict):
                                stats_html = ""
                                feas = d.get("feasibility")
                                imp = d.get("impact")
                                if feas or imp:
                                    feas_str = f"⚡ Feasibility: {feas}/10" if feas else ""
                                    imp_str = f"💥 Impact: {imp}/10" if imp else ""
                                    sep = " | " if feas and imp else ""
                                    stats_html = f'<div style="font-size:0.85rem; color:#64748b; margin-top:8px; font-weight:500;">{feas_str}{sep}{imp_str}</div>'
                                
                                dir_html = f'''
                                <div class="glass-card" style="height: 100%;">
                                    <strong style="color: #3b82f6; font-size: 1.1rem;">{escape_html(str(d.get("direction", "")))}</strong>
                                    {stats_html}
                                    <p style="color: #475569; margin-top: 8px; line-height: 1.5; font-size: 0.95rem;">{escape_html(str(d.get("description", "")))}</p>
                                </div>
                                '''
                                st.markdown(dir_html, unsafe_allow_html=True)
                            else:
                                st.info(str(d))
                    else:
                        st.info("No future directions identified.")
        else:
            # Handle string or other response types
            st.markdown(f'''
            <div class="glass-card" style="padding: 24px;">
                <h3 style="color: #ec4899; margin-bottom: 16px;">🔍 Research Gap Analysis</h3>
                <p style="color: #1e293b; line-height: 1.8;">{escape_html(str(gaps))}</p>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">🔍</div>
            <h3>No Gaps Identified</h3>
            <p>Enable "Gap Analysis" to identify research opportunities</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Trends Tab ---
with tabs[4]:
    if st.session_state.trends:
        trends = st.session_state.trends
        
        # Handle error responses from AI
        if isinstance(trends, dict) and trends.get('error'):
            error_msg = trends.get('error', 'Unknown error')
            if trends.get('rate_limited'):
                st.warning("🚫 **API Rate Limit Reached**\n\nPlease wait a moment and try again, or add credits to your API account.")
            elif trends.get('auth_error'):
                st.error("🔑 **API Authentication Error**\n\n" + error_msg)
            else:
                st.error(f"⚠️ Trend analysis failed: {error_msg}")
        elif isinstance(trends, dict) and trends.get('parsing_error'):
            # Display raw response if parsing failed
            raw_text = trends.get('raw_response', str(trends))
            st.markdown(f'''
            <div class="glass-card" style="padding: 24px;">
                <h3 style="color: #6366f1; margin-bottom: 16px;">📈 Trend Analysis</h3>
                <p style="color: #1e293b; line-height: 1.8;">{escape_html(raw_text)}</p>
            </div>
            ''', unsafe_allow_html=True)
        elif isinstance(trends, dict):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="section-header">📈 Growing Trends</div>', unsafe_allow_html=True)
                growing = trends.get('growing_trends', [])
                if growing:
                    for t in growing[:5]:
                        if isinstance(t, dict):
                            st.success(f"📈 **{t.get('trend', '')}** ({t.get('growth_rate', 'N/A')})")
                        else:
                            st.success(f"📈 {t}")
                else:
                    st.info("No growing trends identified.")
            with c2:
                st.markdown('<div class="section-header">🔮 2026 Predictions</div>', unsafe_allow_html=True)
                predictions = trends.get('predictions_2026', [])
                if predictions:
                    for p in predictions[:5]:
                        st.info(f"🔮 {p}")
                else:
                    st.info("No predictions available.")
        else:
            # Handle string or other response types
            st.markdown(f'''
            <div class="glass-card" style="padding: 24px;">
                <h3 style="color: #6366f1; margin-bottom: 16px;">📈 Trend Analysis</h3>
                <p style="color: #1e293b; line-height: 1.8;">{escape_html(str(trends))}</p>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">📈</div>
            <h3>No Trends Analysis</h3>
            <p>Enable "Trends" to predict future research directions</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Network Tab ---
with tabs[5]:
    st.markdown('<div class="section-header">🕸️ Concept Network Graph</div>', unsafe_allow_html=True)
    if not st.session_state.get('network_graph_enabled', True):
        st.info("📌 Enable 'Network Graph' in sidebar to use this feature")
    elif st.session_state.papers and getattr(st.session_state, 'orchestrator', None) and getattr(st.session_state.orchestrator, 'network_agent', None):
        if not getattr(st.session_state, 'network_built', False):
            if st.button("Generate Network Graph 🕸️"):
                with st.spinner("Extracting concepts and weaving network..."):
                    graph_data = st.session_state.orchestrator.build_concept_network(st.session_state.papers)
                    st.session_state.network_graph = graph_data
                    st.session_state.network_built = True
                    st.rerun()
        
        if getattr(st.session_state, 'network_built', False):
            import plotly.graph_objects as go
            
            graph_data = st.session_state.network_graph
            nodes = graph_data["nodes"]
            edges = graph_data["edges"]
            
            # --- Draw Graph Stats ---
            papers_count = sum(1 for n in nodes if n['type'] == 'paper')
            concepts_count = sum(1 for n in nodes if n['type'] in ('concept', 'bridge_concept'))
            bridge_concepts_count = sum(1 for n in nodes if n['type'] == 'bridge_concept')
            stats_cols = st.columns(5)
            stats_cols[0].markdown(f'<div class="stat-card">Total Nodes<br><span class="stat-value">{len(nodes)}</span></div>', unsafe_allow_html=True)
            stats_cols[1].markdown(f'<div class="stat-card">Total Edges<br><span class="stat-value">{len(graph_data.get("edges", []))}</span></div>', unsafe_allow_html=True)
            stats_cols[2].markdown(f'<div class="stat-card">Papers<br><span class="stat-value">{papers_count}</span></div>', unsafe_allow_html=True)
            stats_cols[3].markdown(f'<div class="stat-card">Concepts<br><span class="stat-value">{concepts_count - bridge_concepts_count}</span></div>', unsafe_allow_html=True)
            stats_cols[4].markdown(f'<div class="stat-card">🌉 Bridges<br><span class="stat-value">{bridge_concepts_count}</span></div>', unsafe_allow_html=True)
            
            edge_x = []
            edge_y = []
            for edge in edges:
                edge_x.extend([edge['x0'], edge['x1'], None])
                edge_y.extend([edge['y0'], edge['y1'], None])
                
            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.5, color='#cbd5e1'),
                hoverinfo='none',
                mode='lines',
                showlegend=False)

            # Separate paper and concept traces for legend and styling
            paper_x = []
            paper_y = []
            paper_texts = []
            paper_hover = []
            paper_sizes = []
            paper_colors = []
            
            concept_x = []
            concept_y = []
            concept_texts = []
            concept_hover = []
            concept_sizes = []
            concept_positions = []
            concept_raw = [] # For ranking below
            bridge_x = []
            bridge_y = []
            bridge_texts = []
            bridge_hover = []
            bridge_sizes = []
            
            # Dynamic text positioning to avoid overlap
            def get_text_position(x, y, center_x, center_y):
                """Position label away from graph center to avoid overlap"""
                if x > center_x and y > center_y:
                    return "top right"
                elif x > center_x and y <= center_y:
                    return "bottom right"  
                elif x <= center_x and y > center_y:
                    return "top left"
                else:
                    return "bottom left"
            
            # Calculate center of all nodes
            all_x = [n['x'] for n in nodes]
            all_y = [n['y'] for n in nodes]
            center_x = sum(all_x) / len(all_x) if all_x else 0
            center_y = sum(all_y) / len(all_y) if all_y else 0
            
            # Populate separated lists
            concept_idx = 0
            for n in nodes:
                if n['type'] == 'paper':
                    paper_x.append(n['x'])
                    paper_y.append(n['y'])
                    full_title = n['title']
                    trunc_title = full_title[:40] + "..." if len(full_title) > 40 else full_title
                    paper_texts.append(trunc_title)
                    
                    # Get innovation score from paper analysis
                    innovation_score = 5  # Default
                    paper_index = int(n['id'].replace('Paper ', '')) - 1
                    if paper_index < len(st.session_state.papers):
                        analysis = st.session_state.papers[paper_index].get('analysis', {})
                        innovation_score = analysis.get('innovation_score', 5)
                    
                    # Size by innovation score (30-60 range)
                    paper_size = 30 + (innovation_score * 3)
                    
                    # Color by innovation
                    if innovation_score >= 8:
                        paper_color = "#10b981"  # green
                    elif innovation_score >= 6:
                        paper_color = "#3b82f6"  # blue
                    else:
                        paper_color = "#6366f1"  # indigo
                    
                    paper_sizes.append(paper_size)
                    
                    # Rich hover with innovation score
                    conn_count = n.get('connections', 0)
                    paper_hover.append(f"📄 {full_title}<br>Innovation: {innovation_score}/10<br>Connections: {conn_count}")
                elif n['type'] == 'bridge_concept':
                    bridge_x.append(n['x'])
                    bridge_y.append(n['y'])
                    bridge_texts.append(n['title'])
                    
                    paper_count = n.get('paper_count', 0)
                    bridge_hover.append(f"🌉 {n['title']}<br>Bridges {paper_count} papers")
                    bridge_sizes.append(35)
                else:
                    concept_x.append(n['x'])
                    concept_y.append(n['y'])
                    concept_texts.append(n['title'])
                    
                    # Use paper_count from node data
                    paper_count = n.get('paper_count', 0)
                    all_connections = n.get('connections', 0)
                    concept_raw.append({"title": n['title'], "paper_count": paper_count, "connections": all_connections})
                    
                    concept_hover.append(f"💡 {n['title']}<br>In {paper_count} papers • {all_connections} total connections")
                    concept_sizes.append(min(45, max(18, paper_count * 8)))
                    
                    # Dynamic text positioning
                    text_pos = get_text_position(n['x'], n['y'], center_x, center_y)
                    concept_positions.append(text_pos)
            
            paper_trace = go.Scatter(
                x=paper_x, y=paper_y,
                mode='markers+text',
                text=paper_texts,
                textposition='bottom center',
                textfont=dict(size=9, color="#1e293b"),
                hoverinfo='text',
                hovertext=paper_hover,
                name="📄 Research Papers",
                marker=dict(
                    color=paper_colors,
                    size=paper_sizes,
                    symbol="diamond",
                    line=dict(width=2, color='#ffffff')
                ))

            concept_trace = go.Scatter(
                x=concept_x, y=concept_y,
                mode='markers+text',
                text=concept_texts,
                textposition=concept_positions,
                textfont=dict(size=9, color="#475569"),
                hoverinfo='text',
                hovertext=concept_hover,
                name="💡 Key Concepts",
                marker=dict(
                    color='#ec4899',
                    size=concept_sizes,
                    line=dict(width=1, color='#ffffff')
                ))
            
            bridge_trace = go.Scatter(
                x=bridge_x, y=bridge_y,
                mode='markers+text',
                text=bridge_texts,
                textposition='top center',
                textfont=dict(size=10, color="#92400e"),
                hoverinfo='text',
                hovertext=bridge_hover,
                name="🌉 Bridge Concepts",
                marker=dict(
                    color='#f59e0b',
                    size=bridge_sizes,
                    line=dict(width=2, color='#fcd34d')
                ))
            
            fig = go.Figure(data=[edge_trace, paper_trace, concept_trace, bridge_trace],
                            layout=go.Layout(
                                title=dict(text='Knowledge Graph', font=dict(size=16, color="#0f172a")),
                                showlegend=True,
                                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                hovermode='closest',
                                margin=dict(b=20,l=5,r=5,t=40),
                                paper_bgcolor="#ffffff",
                                plot_bgcolor="#f8fafc",
                                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                            )
            st.plotly_chart(fig, width='stretch')
            
            # Add color legend
            st.markdown("""
<div style="display:flex; gap:20px; padding:12px; background:#f8fafc; 
border-radius:12px; margin-top:8px; flex-wrap:wrap; font-size:0.9rem;">
  <span>🟢 High Innovation (8-10)</span>
  <span>🔵 Medium Innovation (6-7)</span>  
  <span>🟣 Standard Paper (1-5)</span>
  <span>🟠 Bridge Concept</span>
  <span>🩷 Specific Concept</span>
</div>
""", unsafe_allow_html=True)
            
            # --- Draw Top Concepts ---
            st.markdown("### 🔥 Most Connected Concepts (by Papers)")
            # Filter concepts that appear in at least 1 paper
            valid_concepts = [c for c in concept_raw if c.get('paper_count', 0) >= 1]
            # Sort by paper_count (most papers first)
            top_concepts = sorted(valid_concepts, key=lambda x: x.get('paper_count', 0), reverse=True)[:8]
            
            if top_concepts:
                max_paper_count = max([c.get('paper_count', 1) for c in top_concepts])
                
                for c in top_concepts:
                    paper_count = c.get('paper_count', 0)
                    
                    # Color by paper count
                    if paper_count >= 3:
                        color = "#8b5cf6"  # purple
                        icon = "♦️"
                    elif paper_count >= 2:
                        color = "#3b82f6"  # blue
                        icon = "◆"
                    else:
                        color = "#94a3b8"  # gray
                        icon = "●"
                    
                    colA, colB, colC = st.columns([2, 2, 5])
                    with colA:
                        st.write(f"{icon} **{c['title']}**")
                    with colB:
                        st.write(f"__{paper_count} paper{'s' if paper_count != 1 else ''}__")
                    with colC:
                        # Progress bar width proportional to paper_count
                        progress = paper_count / max_paper_count
                        st.progress(progress, text=f"{int(progress*100)}%")
            else:
                st.info("No concepts found with paper connections")
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">🕸️</div>
            <h3>No Network Data</h3>
            <p>Run a research session first to generate the concept network</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Ask Papers Tab ---
with tabs[6]:
    st.markdown('<div class="section-header">💬 Chat with Papers</div>', unsafe_allow_html=True)
    if not st.session_state.get('chat_enabled', True):
        st.info("📌 Enable 'Chat with Papers' in sidebar to use this feature")
    elif st.session_state.papers and getattr(st.session_state, 'orchestrator', None) and getattr(st.session_state.orchestrator, 'chat_agent', None):
        st.markdown('<div class="glass-card" style="padding: 24px; margin-bottom: 24px;">', unsafe_allow_html=True)
        
        from datetime import datetime
        
        # 1. Suggested Questions at the top with styled chips
        st.markdown("**Suggested Questions:**")
        suggested = [
            "🔬 What methods are most common?",
            "🔍 What are the main research gaps?", 
            "🏆 Which paper has highest innovation?",
            "💡 What are the key findings?",
            "📈 What trends do you see?",
            "⚡ What contradictions exist?"
        ]
        
        s_cols = st.columns(3)
        for i, q in enumerate(suggested):
            with s_cols[i % 3]:
                if st.button(q, key=f"sug_btn_{i}", use_container_width=True):
                    # Extract question text without emoji
                    question_text = q.split(" ", 1)[1] if " " in q else q
                    st.session_state.chat_history.append({
                        "role": "user", 
                        "content": question_text, 
                        "time": datetime.now().strftime("%H:%M")
                    })
                    st.rerun()
                
        st.markdown("<hr style='margin: 16px 0; border: 0.5px solid #e2e8f0;'>", unsafe_allow_html=True)
        
        # 2. Render chat history WITH custom styles
        for msg in st.session_state.chat_history:
            role = msg["role"]
            content = msg["content"]
            t_str = msg.get("time", datetime.now().strftime("%H:%M"))
            
            if role == "user":
                header = f'<div style="display: flex; justify-content: flex-end; margin-bottom: 16px;"><div style="background: #eff6ff; padding: 12px 16px; border-radius: 12px 12px 0 12px; color: #0f172a; max-width: 85%; font-size: 0.95rem; line-height: 1.5; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">'
                footer = f'<div style="font-size: 0.75rem; color: #94a3b8; text-align: right; margin-top: 6px;">{t_str}</div></div></div>'
                st.markdown(header + escape_html(content).replace("\n", "<br>") + footer, unsafe_allow_html=True)
            else:
                # Use st.chat_message for assistant with proper avatar
                with st.chat_message("assistant", avatar="🔬"):
                    st.markdown(content)
                    st.caption(f"_{t_str}_")

        if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
            with st.spinner("🔬 Analyzing papers..."):
                ans = st.session_state.orchestrator.ask_papers(
                    st.session_state.chat_history[-1]["content"], 
                    st.session_state.papers,
                    st.session_state.chat_history  # Pass history for context
                )
                st.session_state.chat_history.append({
                    "role": "assistant", 
                    "content": ans,
                    "time": datetime.now().strftime("%H:%M")
                })
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)

        # 3. Chat Input AT BOTTOM - with error handling
        try:
            if user_q := st.chat_input("Ask a question about the analyzed papers..."):
                st.session_state.chat_history.append({
                    "role": "user", 
                    "content": user_q,
                    "time": datetime.now().strftime("%H:%M")
                })
                st.rerun()
        except Exception as e:
            # Fallback if chat_input fails
            st.warning(f"Chat input error: {str(e)}. Please refresh the page.")
            # Provide alternative text input
            alt_input = st.text_input("Alternative: Ask a question about the papers...")
            if alt_input:
                st.session_state.chat_history.append({
                    "role": "user", 
                    "content": alt_input,
                    "time": datetime.now().strftime("%H:%M")
                })
                st.rerun()
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="icon">💬</div>
            <h3>No Papers Available</h3>
            <p>Run a search to be able to ask questions about papers</p>
        </div>
        ''', unsafe_allow_html=True)

# --- Agents Tab ---  
with tabs[7]:
    st.markdown('<div class="section-header">🤖 Multi-Agent Orchestration</div>', unsafe_allow_html=True)
    
    agents = [
        ("🔍", "Collector", "Academic paper discovery from arXiv database"),
        ("🧠", "Analyzer", "Deep analysis with Gemini AI thinking mode"),
        ("📚", "Synthesis", "Automated literature review generation"),
        ("🔍", "Critic", "Research gap and opportunity identification"),
        ("📈", "Trends", "Future trend prediction and forecasting"),
        ("🕸️", "Network", "Concept extraction and knowledge graph building"),
        ("💬", "Chat", "AI-powered Q&A over analyzed paper corpus"),
    ]
    
    for icon, name, desc in agents:
        agent_key = name
        status = st.session_state.agent_status.get(agent_key, "waiting")
        timing_str = ""
        detail_text = ""
        
        if name == "Chat":
            chat_count = len(st.session_state.get('chat_history', []))
            if st.session_state.agent_status.get("Chat") == "running":
                status = "running"
            elif chat_count > 0:
                status = "done"
                st.session_state.agent_status["Chat"] = "done"
            else:
                status = "waiting"
        
        if name == "Network":
            if st.session_state.get('network_built', False):
                status = "done"
                st.session_state.agent_status["Network"] = "done"
            elif st.session_state.agent_status.get("Network") == "running":
                status = "running"
            else:
                status = "waiting"
        
        if name == "Collector":
            detail_text = f"📄 {len(st.session_state.papers)} papers collected"
        elif name == "Analyzer":
            detail_text = f"🧠 {len(st.session_state.analyses)} papers analyzed"
        elif name == "Synthesis":
            detail_text = "✅ Literature review generated" if st.session_state.literature else "⏳ Pending"
        elif name == "Critic":
            detail_text = "✅ Gaps identified" if st.session_state.gaps else "⏳ Pending"
        elif name == "Trends":
            detail_text = "✅ Trends predicted" if st.session_state.trends else "⏳ Pending"
        elif name == "Network":
            detail_text = "✅ Graph built" if st.session_state.network_built else "⏳ Click Build in Network tab"
        elif name == "Chat":
            detail_text = f"💬 {len(st.session_state.chat_history)//2} questions answered"
        
        if status == "running":
            avatar_class = "agent-running"
            status_class = "status-running"
            status_text = "● RUNNING"
        elif status == "done":
            avatar_class = "agent-done"
            status_class = "status-done"
            status_text = "✓ COMPLETE"
            
            if "agent_times" in st.session_state and agent_key in st.session_state.agent_times:
                runtime = st.session_state.agent_times[agent_key]
                timing_str = f'<p style="color: #94a3b8; font-size: 0.75rem; margin-top: 4px; font-style: italic;">Completed in {runtime}s</p>'
        else:
            avatar_class = "agent-waiting"
            status_class = "status-waiting"
            status_text = "○ STANDBY"
            
        agent_html = f'''
        <div class="agent-card">
            <div class="agent-avatar {avatar_class}">{icon}</div>
            <div style="flex: 1;">
                <p class="agent-name">{name} Agent</p>
                <p class="agent-desc">{desc}</p>
                <p style="font-family:Inter; font-size:0.8rem; color:#94a3b8; margin:4px 0 0 0; font-weight:500;">{detail_text}</p>
            </div>
            <span class="agent-status {status_class}">{status_text}</span>
        </div>
        '''
        st.markdown(agent_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    total_agents = 7
    completed = sum(1 for a_name in ["Collector","Analyzer","Synthesis","Critic","Trends","Network","Chat"]
                    if st.session_state.agent_status.get(a_name) == "done")
    
    progress_pct = completed / total_agents
    
    st.markdown(f'''
    <div style="background:white; border:2px solid #e2e8f0; border-radius:16px; padding:20px; text-align:center;">
        <p style="font-family:Poppins; font-weight:700; color:#0f172a; font-size:1rem; margin-bottom:12px;">
           🏁 Pipeline Progress: {completed}/{total_agents} Agents Complete
        </p>
    </div>
    ''', unsafe_allow_html=True)
    st.progress(progress_pct)
    
    if completed == total_agents:
        st.success("🏆 All agents complete! Your research analysis is ready.")
    elif completed >= 5:
        st.info(f"⚡ {total_agents - completed} agents remaining. Check Network tab to build graph.")
    else:
        st.warning(f"🔄 {completed} of {total_agents} agents complete.")

# ============================================
# 📝 FOOTER
# ============================================

st.markdown("<br><hr style='border: 1px solid #e2e8f0; margin: 40px 0;'>", unsafe_allow_html=True)
footer_html = '''
<div style="text-align: center; padding: 20px; font-family: Inter;">
    <p style="color: #64748b; font-size: 1rem; margin-bottom: 8px;">
        ✨ <strong style="color: #3b82f6;">Multi-Agent Research Intelligence System</strong>
    </p>
    <p style="color: #94a3b8; font-size: 0.9rem;">
        Advanced Academic Discovery • Powered by AI
    </p>
</div>
'''
st.markdown(footer_html, unsafe_allow_html=True)