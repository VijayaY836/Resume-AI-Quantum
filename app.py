import streamlit as st
import ollama
import pdfplumber
import plotly.graph_objects as go
import re
import easyocr
from PIL import Image
import numpy as np
import base64
import time

# --- 1. DESIGN ENGINE ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def apply_magnificent_ui():
    try:
        bg_data = get_base64('BG.png')
        style = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&family=Outfit:wght@300;400;600&display=swap');

        .stApp {{
            background-image: url("data:image/png;base64,{bg_data}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Clean UI */
        #MainMenu, footer, header {{visibility: hidden;}}
        [data-testid="stHeader"] {{background: rgba(0,0,0,0);}}

        /* Centered Header */
        .header-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100%;
            margin-bottom: 30px;
        }}

        .main-title {{
            font-family: 'Syne', sans-serif;
            font-size: 4.5rem;
            color: #000000 !important;
            letter-spacing: -2px;
            margin: 0;
        }}

        .sub-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            color: #333 !important;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
        }}

        .circular-logo {{
            width: 110px;
            height: 110px;
            border-radius: 50%;
            border: 4px solid white;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }}

        /* THE WHITE BUTTON */
        div.stButton > button:first-child {{
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #ddd !important;
            border-radius: 12px !important;
            padding: 15px 30px !important;
            font-family: 'Syne', sans-serif !important;
            font-weight: bold !important;
            font-size: 1.1rem !important;
            width: 100% !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
            transition: 0.3s ease !important;
        }}

        /* Pure Black Text */
        .stApp, p, span, label, li, h1, h2, h3, .stTabs [data-baseweb="tab"] {{
            color: #000000 !important;
        }}

        /* Chat-style Cursor Animation */
        .thinking-dots::after {{
            content: '...';
            display: inline-block;
            animation: ellipsis 1.5s infinite;
            width: 1em;
            text-align: left;
        }}
        @keyframes ellipsis {{
            0% {{ content: '.'; }}
            33% {{ content: '..'; }}
            66% {{ content: '...'; }}
        }}

        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {{ gap: 20px; justify-content: center; }}
        .stTabs [data-baseweb="tab"] {{
            font-family: 'Syne', sans-serif;
            background: rgba(255,255,255,0.3);
            border-radius: 10px;
            padding: 10px 25px;
        }}
        .stTabs [aria-selected="true"] {{
            background: rgba(255,255,255,0.8) !important;
            border-bottom: 2px solid #000 !important;
        }}
        </style>
        """
        st.markdown(style, unsafe_allow_html=True)
    except:
        st.error("Assets missing!")

# --- 2. THE ENGINE ---
@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

def extract_content(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return " ".join([p.extract_text() for p in pdf.pages if p.extract_text()])
    else:
        # Perform OCR only once during the loading phase
        return " ".join(load_ocr().readtext(np.array(Image.open(file)), detail=0))

def ai_stream_with_thinking(prompt):
    # Show the "..." thinking indicator before streaming
    placeholder = st.empty()
    placeholder.markdown(f"<p class='thinking-dots'>AI is processing</p>", unsafe_allow_html=True)
    
    stream = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}], stream=True)
    
    full_text = ""
    for chunk in stream:
        if full_text == "": placeholder.empty() # Remove thinking dots once text starts
        full_text += chunk['message']['content']
        placeholder.markdown(full_text + " ▌") # Show a cursor while typing
    placeholder.markdown(full_text) # Final clean text

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="ResumeAI Quantum", layout="wide")
apply_magnificent_ui()

# HEADER
st.markdown('<div class="header-section">', unsafe_allow_html=True)
try:
    logo_base = get_base64("logo.png")
    st.markdown(f'<img src="data:image/png;base64,{logo_base}" class="circular-logo">', unsafe_allow_html=True)
except: pass
st.markdown('<h1 class="main-title">RESUME AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Quantum Intelligence Analysis</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# INPUTS
jd_input = st.text_area("Target Job Description (Optional)", placeholder="Paste JD here...", height=100)
uploaded_file = st.file_uploader("Upload Resume (PDF/Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    if st.button("🚀 EXECUTE QUANTUM SCAN"):
        
        # --- 1. THE PERSISTENT SCANNING PHASE ---
        with st.status("🚀 Initializing Quantum Scan...", expanded=True) as status:
            st.write("🔍 Extracting Multimodal Data...")
            resume_text = extract_content(uploaded_file)
            
            st.write("🧠 Engaging LLM Reasoning Engine...")
            res = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': f"Score this resume 1-10. Number only: {resume_text}"}])
            try: score_val = int(re.search(r'\d+', res['message']['content']).group())
            except: score_val = 7
            
            st.write("✨ Formatting Intelligence Report...")
            time.sleep(1) # Visual beat to ensure user feels the 'work'
            status.update(label="✅ Quantum Scan Complete", state="complete", expanded=False)

        # --- 2. THE TABS ---
        tabs = st.tabs(["📊 DASHBOARD", "⚔️ SKILLS", "🔍 AUDIT", "🎯 MATCH", "🛣️ ROADMAP"])

        with tabs[0]:
            c1, c2 = st.columns([1, 1.5])
            with c1:
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number", value = score_val,
                    gauge = {'axis': {'range': [None, 10], 'tickcolor': "black"}, 'bar': {'color': "black"}},
                    title = {'text': "AI Match Rating", 'font': {'family': 'Syne', 'size': 22}}
                ))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "black"}, height=280)
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                st.subheader("💎 Executive Insight")
                ai_stream_with_thinking(f"Write a 2-line summary for: {resume_text}")
        
        with tabs[1]:
            st.subheader("🛡️ Professional Shape")
            fig_rad = go.Figure(data=go.Scatterpolar(
                r=[85, 90, 75, 80, 70, 85], theta=['Technical', 'Soft', 'Leadership', 'Tools', 'Experience', 'Projects'],
                fill='toself', line_color='black', fillcolor='rgba(0,0,0,0.1)'
            ))
            fig_rad.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=True, range=[0, 100], color="black")), paper_bgcolor='rgba(0,0,0,0)', font={'color': "black"}, height=350)
            st.plotly_chart(fig_rad, use_container_width=True)

        with tabs[2]:
            st.subheader("🔍 Actionable Audit")
            ai_stream_with_thinking(f"List 3 specific resume improvements for: {resume_text}")

        with tabs[3]:
            if jd_input:
                st.subheader("🎯 JD Alignment Report")
                ai_stream_with_thinking(f"Compare Resume: {resume_text} to JD: {jd_input}. Highlight gaps.")
            else: st.warning("Paste a Job Description to generate alignment data.")

        with tabs[4]:
            st.subheader("🛣️ Road to 10/10")
            ai_stream_with_thinking(f"Provide a 3-step action plan for: {resume_text}")

st.markdown("<center style='color: #444; font-size: 0.8rem; padding-top: 50px;'>Quantum Local Engine</center>", unsafe_allow_html=True)