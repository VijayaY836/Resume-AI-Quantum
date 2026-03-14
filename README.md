<div align="center">

# 🌌 RESUME AI: QUANTUM
### Sovereign Local Intelligence for the Future of Hiring

*Transform your resume into a winning asset — entirely on your machine.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Llama](https://img.shields.io/badge/Local%20LLM-Llama%203.2-blueviolet.svg)](https://ollama.com)
[![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR-green.svg)](https://github.com/JaidedAI/EasyOCR)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local-brightgreen.svg)]()

</div>

---

## 🎯 The Problem

Over **75% of resumes** are rejected by Applicant Tracking Systems before a human ever reads them — not because the candidate is unqualified, but because of weak wording, missing keywords, and poor formatting.

On top of that, the tools that exist to fix this problem require you to upload your most sensitive personal document — your career history — to third-party cloud servers (OpenAI, Gemini, etc.), trading your privacy for feedback.

**There had to be a better way.**

---

## 🚀 The Solution

**ResumeAI Quantum** is an industry-grade, multimodal career optimization engine that runs 100% locally on your machine. It combines the power of **Llama 3.2** (via Ollama) with **EasyOCR** to transform any resume — PDF or photo — into a comprehensive intelligence report.

No API keys. No cloud uploads. No data leaks. Just results.

```
Upload Resume → Quantum Scan → Executive Report → Land the Job
```

---

## ✨ Core Features

### 📊 Executive Dashboard
Get an instant AI-generated impact score (1–10) alongside a sharp 2-line executive summary that captures your professional value at a glance. Powered by Llama 3.2's reasoning engine.

### 🛡️ Competency Radar
A visual "Professional Shape" radar chart mapping your strengths across six dimensions:
`Technical` · `Soft Skills` · `Leadership` · `Tools` · `Experience` · `Projects`

Instantly see where you shine and where you're leaving points on the table.

### 🔍 Actionable Audit
The AI doesn't just critique — it rewrites. It identifies your three weakest bullet points and provides high-impact, ATS-optimized alternatives. Specific, targeted, and immediately usable.

### 🎯 JD Alignment (Gap Analysis)
Paste any job description and get a side-by-side gap analysis. The engine identifies missing technical keywords, skill mismatches, and alignment score — so you know exactly what to add before you apply.

### 🛣️ Success Roadmap
A prioritized, 3-step action plan to take your resume from its current score to an 8+/10 "Winning" profile. Concrete actions, not vague advice.

### 🔒 Data Sovereignty
Every byte of your resume stays on your machine. No external API calls, no telemetry, no storage. Your career data is yours — period.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🧠 LLM | Llama 3.2 via Ollama | Local AI inference & reasoning |
| 👁️ OCR | EasyOCR | Extract text from images & screenshots |
| 📄 PDF | pdfplumber | Parse and extract PDF resume content |
| 🎨 Frontend | Streamlit | Interactive web UI |
| 📈 Charts | Plotly | Radar & gauge visualizations |
| 🖋️ Typography | Syne + Outfit (Google Fonts) | Premium UI aesthetics |

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

### Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Quantum-Resume-AI.git
cd Quantum-Resume-AI
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Pull the Llama 3.2 model**
```bash
ollama pull llama3.2
```

**4. Launch the app**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser and you're live.

---

## 🖥️ Usage

1. **(Optional)** Paste a target job description into the JD field
2. Upload your resume — PDF, PNG, or JPG supported
3. Click **🚀 Execute Quantum Scan**
4. Navigate the five analysis tabs:

| Tab | What You Get |
|-----|-------------|
| 📊 Dashboard | Score + executive summary |
| ⚔️ Skills | Competency radar chart |
| 🔍 Audit | Rewritten bullet points |
| 🎯 Match | JD keyword gap analysis |
| 🛣️ Roadmap | 3-step improvement plan |

---

## 🌍 Deployment

The project is containerized via **Docker** and deployable to any cloud provider without code changes. It is optimized for **Hugging Face Spaces** for zero-cost, server-side local inference — making it accessible without requiring users to install Ollama locally.

```bash
# Build and run with Docker
docker build -t resumeai-quantum .
docker run -p 8501:8501 resumeai-quantum
```

---

## 🏆 Hackathon Context

Built for **"Code the Future: AI Edition"** by UnsaidTalks. The challenge: solve a real-world hiring problem using Generative AI with genuine technical depth. ResumeAI Quantum addresses the dual crisis of ATS rejection rates and AI privacy concerns — delivering a production-quality solution that works entirely offline.

---

## ⚖️ Privacy Disclaimer

ResumeAI Quantum is built on the principle of **data sovereignty**. All processing occurs within your local environment — whether that's your laptop or a private Docker container. No external API keys are used, no data is transmitted to third parties, and nothing persists after your session ends.

Your resume is yours. Full stop.

---

## 📄 License

MIT — Built with ❤️ by Vijaya Y
