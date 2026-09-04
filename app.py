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
MODEL_REPO = "Qwen/Qwen2.5-Coder-7B-Instruct" 

if st.button("Debug Code"):
    if not code_input.strip():
        st.warning("Please enter some Python code to debug.")
    else:
        prompt = f"Instruction:\n{instruction}\n\nCode:\n{code_input}"
        
        with st.spinner("Analyzing code..."):
            try:
                client = InferenceClient(model=MODEL_REPO, token=HF_TOKEN if HF_TOKEN else None)
                
                # Using chat_completion fixes the 'nscale' provider routing issue
                response = client.chat_completion(
                    messages=[
                        {"role": "system", "content": "You are an expert Python debugger."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=512,
                    temperature=0.2
                )
                
                clean_res = response.choices[0].message.content
                st.success("Analysis Complete!")
                st.code(clean_res.strip(), language="python")
                
            except Exception as e:
                st.error(f"Inference Error: {str(e)}")
