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
![Model](https://img.shields.io/badge/Model-Qwen2.5--7B--Instruct-green)

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
- ⚡ Powered by Qwen2.5-7B-Instruct via Hugging Face Inference API
- 🧩 Clean two-file architecture (`app.py` + `generator.py`)

---

## 🛠️ Technologies Used

- **Qwen2.5-7B-Instruct** — the language model powering generation
- **Hugging Face Inference API** — free serverless model hosting
- **Streamlit** — web interface
- **Python** — backend logic and prompt construction

---

## 🗂️ Project Structure

product-description-generator/

├── app.py              # Streamlit UI and session management

├── generator.py        # Prompt engineering and HF API calls

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

**3. Set your Hugging Face token**
```bash
export HF_TOKEN=your_token_here   # Mac/Linux
set HF_TOKEN=your_token_here      # Windows CMD
$env:HF_TOKEN="your_token_here"   # Windows PowerShell
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
- Lower temperature (0.1) gives more consistent, format-faithful results
- Higher temperature (0.7–0.9) produces more creative but less predictable copy
- Model performs best on physical consumer products

---

## 🔮 Future Improvements

- [ ] Add more tone options (Minimalist, Technical, Playful)
- [ ] Support bulk generation from a CSV upload
- [ ] Add copy-to-clipboard button for each description
- [ ] Wrap generation logic in a FastAPI endpoint
- [ ] Fine-tune on a larger e-commerce dataset for better quality

---

