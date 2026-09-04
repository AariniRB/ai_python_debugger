# ai_python_debugger
# ⚡ AI Python Code Debugger

An end-to-end Machine Learning web application designed to automatically detect, explain, and fix bugs in Python code.

🚀 **Live Web App:** [Try the Live App](https://enxhjf6zhm27emvzqszvut.streamlit.app)  
🤗 **Fine-Tuned Adapter Weights:** [AariniRB/qwen2.5-coder-python-debugger](https://huggingface.co/AariniRB/qwen2.5-coder-python-debugger)

---

## 📌 Project Overview
This application leverages open-source Large Language Models fine-tuned specifically on programming instruction sets. It provides developer-friendly bug analysis, suggested code fixes, and detailed explanations in real time.

## 🛠️ Tech Stack & Tools
* **LLM Architecture:** Qwen2.5-Coder-7B-Instruct
* **Fine-Tuning:** Unsloth, QLoRA (4-bit quantization), PyTorch, Hugging Face `peft`
* **Dataset:** `flytech/python-codes-25k`
* **Frontend & Hosting:** Streamlit Community Cloud

## ⚡ Key Engineering Features
* **Efficient QLoRA Fine-Tuning:** Parameter-efficient fine-tuning with rank $r=16$, targeting linear projection layers while keeping memory footprint minimal.
* **Instruction Formatting:** Custom prompt templates structuring code inputs and instructions into dedicated evaluation tokens.
* **Cloud Infrastructure:** Secure API key management via environment secrets and automated CI/CD deployment through GitHub.
