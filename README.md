---
title: Product Description Generator
emoji: 🛍️
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.58.0
app_file: app.py
pinned: false
license: apache-2.0
---

# 🛍️ Product Description Generator

![Live Demo](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face%20Spaces-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58%2B-red)
![Model](https://img.shields.io/badge/Model-openai%2Fgpt--oss--20b-green)
![Powered by](https://img.shields.io/badge/Powered%20by-Groq-orange)

An AI-powered web application that generates compelling marketing copy for e-commerce products using few-shot prompt engineering.

---

## 🚀 Live Demo

**Try the live application here → [Product Description Generator on Hugging Face Spaces](https://szamadesh-product-description-generator.hf.space)**

---

## 📋 Project Overview

This project demonstrates a complete prompt engineering workflow:

- **Few-shot prompting** to control output tone and style
- **Three distinct tones** — Professional, Casual, and Luxury
- **Session history** to track previously generated descriptions
- **Modular architecture** separating UI logic from generation logic

---

## ✨ Key Features

- 🎯 Tone-controlled generation (Professional / Casual / Luxury)
- 📝 Few-shot examples guide the model's output style
- 🕐 Session history displays all previously generated descriptions
- ⚡ Powered by `openai/gpt-oss-20b` via **Groq** (extremely fast inference)
- 🧩 Clean two-file architecture (`app.py` + `generator.py`)

---

## 🛠️ Technologies Used

- **openai/gpt-oss-20b** — the language model powering generation
- **Groq** — ultra-fast inference API
- **Streamlit** — web interface
- **Python** — backend logic and prompt construction

---

## 🗂️ Project Structure


product-description-generator/

├── app.py              # Streamlit UI and session management

├── generator.py        # Prompt engineering and Groq API calls

├── requirements.txt    # Dependencies

└── README.md           # Project documentation

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/sammeee/product-description-generator.git
cd product-description-generator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your Groq API key**
```bash
export GROQ_API_KEY=your_token_here   # Mac/Linux
set GROQ_API_KEY=your_token_here      # Windows CMD
$env:GROQ_API_KEY="your_token_here"   # Windows PowerShell
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 🎨 Tone Examples

| Tone | Style |
|------|-------|
| **Professional** | Formal, feature-focused, business language |
| **Casual** | Friendly, conversational, relatable |
| **Luxury** | Elevated, aspirational, premium feel |

---

## 📊 Results & Observations

- Few-shot examples produce noticeably different outputs per tone
- Groq provides very low latency responses
- Temperature of 0.7 gives a good balance between creativity and consistency
- Model performs best on physical consumer products

---

## 🔮 Future Improvements

- [ ] Add more tone options (Minimalist, Technical, Playful)
- [ ] Support bulk generation from a CSV upload
- [ ] Add copy-to-clipboard button for each description
- [ ] Wrap generation logic in a FastAPI endpoint
- [ ] Fine-tune on a larger e-commerce dataset for better quality

---

