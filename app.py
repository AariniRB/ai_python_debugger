import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="AI Python Debugger", page_icon="⚡", layout="centered")

st.title("⚡ AI Python Code Debugger")
st.write("Fine-tuned Qwen2.5-Coder model hosted via Hugging Face Serverless API")

# Input Fields
instruction = st.text_input(
    "Instruction", 
    value="Fix the bug in this function and explain what went wrong."
)

code_input = st.text_area(
    "Buggy Code Input", 
    height=200, 
    value="def calculate_average(nums):\n    total = 0\n    for n in nums:\n        total += n\n    return total / len(num)"
)

# Fetch HF API Token safely from Streamlit Secrets
HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# Update this line with your actual Hugging Face model repository path
MODEL_REPO = "aarinirb/qwen2.5-coder-python-debugger" 
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_REPO}"

if st.button("Debug Code"):
    if not code_input.strip():
        st.warning("Please enter some Python code to debug.")
    else:
        # Prompt structure matching fine-tuning format
        prompt = f"Below is an instruction that describes a programming task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Input:\n{code_input}\n\n### Response:\n"
        
        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 512,
                "temperature": 0.2,
                "return_full_text": False
            }
        }
        
        with st.spinner("Analyzing code with fine-tuned model..."):
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    # Handle API response formatting
                    if isinstance(data, list) and len(data) > 0:
                        clean_res = data[0].get("generated_text", "")
                    else:
                        clean_res = str(data)
                    
                    st.success("Analysis Complete!")
                    st.code(clean_res.strip(), language="python")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to Hugging Face API: {str(e)}")
