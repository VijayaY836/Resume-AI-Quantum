# ResumeAI Quantum

A local, privacy-first resume analyzer powered by Llama 3.2. Upload your resume as a PDF or image and get an AI-generated score, skill breakdown, actionable improvements, and a job description alignment report — all without sending your data anywhere.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)
![Llama](https://img.shields.io/badge/Local%20LLM-Llama%203.2-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Resume Scoring** — AI rates your resume 1–10 with an executive summary
- **Skill Radar** — Visual breakdown across Technical, Leadership, Soft Skills, and more
- **Actionable Audit** — Identifies weak bullet points and rewrites them for ATS
- **JD Alignment** — Paste a job description to see keyword gaps and alignment score
- **Success Roadmap** — 3-step action plan to improve your resume
- **100% Local** — Runs entirely on your machine via Ollama, no API keys needed

## Tech Stack

| Layer | Tool |
|-------|------|
| LLM | Llama 3.2 via Ollama |
| OCR | EasyOCR |
| Frontend | Streamlit |
| Charts | Plotly |
| PDF Parsing | pdfplumber |

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/Quantum-Resume-AI.git
cd Quantum-Resume-AI
pip install -r requirements.txt
```

Pull the model:

```bash
ollama pull llama3.2
```

## Usage

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

1. Optionally paste a target job description
2. Upload your resume (PDF, PNG, JPG)
3. Click **Execute Quantum Scan**
4. Review results across the Dashboard, Skills, Audit, Match, and Roadmap tabs

## Privacy

All processing happens locally. No data is sent to external servers, no API keys are required, and nothing is stored after your session ends.

## License

MIT — Built with ❤️ by Vijaya Y
