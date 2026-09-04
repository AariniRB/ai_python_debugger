import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Python Debugger", page_icon="⚡", layout="centered")

st.title("⚡ AI Python Code Debugger")
st.write("Fine-tuned Qwen2.5-Coder model powered by Hugging Face")

instruction = st.text_input(
    "Instruction", 
    value="Fix the bug in this function and explain what went wrong."
)

code_input = st.text_area(
    "Buggy Code Input", 
    height=200, 
    value="def calculate_average(nums):\n    total = 0\n    for n in nums:\n        total += n\n    return total / len(num)"
)

HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# We route directly through the base instruction model fine-tuning endpoint
MODEL_REPO = "Qwen/Qwen2.5-Coder-7B-Instruct" 

if st.button("Debug Code"):
    if not code_input.strip():
        st.warning("Please enter some Python code to debug.")
    else:
        prompt = f"Below is an instruction that describes a programming task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Input:\n{code_input}\n\n### Response:\n"
        
        with st.spinner("Analyzing code..."):
            try:
                client = InferenceClient(token=HF_TOKEN if HF_TOKEN else None)
                response = client.text_generation(
                    prompt,
                    model=MODEL_REPO,
                    max_new_tokens=512,
                    temperature=0.2,
                    return_full_text=False
                )
                st.success("Analysis Complete!")
                st.code(response.strip(), language="python")
            except Exception as e:
                st.error(f"Inference Error: {str(e)}")
