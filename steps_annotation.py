import streamlit as st

num_steps = st.number_input("Enter the number of steps to evaluate", min_value=1, max_value=10)
for i in range(num_steps):
    st.write(f"Step {i+1}:")
    accuracy = st.radio(f"Is step {i+1} correct?", ('Yes', 'No'))
    llm_or_python = st.radio(f"Should step {i+1} be solved by LLM or Python?", ('LLM', 'Python'))
    if accuracy == 'No':
        original_step = st.text_area(f"Original step for step {i+1}")
        rewrite = st.text_area(f"Rewrite for step {i+1}")
        rewrite_reason = st.text_area(f"Reason for rewrite for step {i+1}")
