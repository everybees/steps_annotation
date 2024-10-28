import streamlit as st

# Initialize a list to store the steps data
steps_data = []

# Input: Number of steps to evaluate
num_steps = st.number_input("Enter the number of steps to evaluate", min_value=1, max_value=10)

# Loop through the number of steps
for i in range(num_steps):
    st.write(f"### Step {i+1}:")
    
    # Accuracy input for the current step
    accuracy = st.radio(f"Is step {i+1} correct?", ('Yes', 'No'), key=f'accuracy_{i}')
    
    # LLM or Python decision for the current step
    llm_or_python = st.radio(f"Should step {i+1} be solved by LLM or Python?", ('LLM', 'Python'), key=f'llm_or_python_{i}')
    
    # If the step is not correct, collect more data
    if accuracy == 'No':
        original_step = st.text_area(f"Original step for step {i+1}", key=f'original_step_{i}')
        rewrite = st.text_area(f"Rewrite for step {i+1}", key=f'rewrite_{i}')
        rewrite_reason = st.text_area(f"Reason for rewrite for step {i+1}", key=f'rewrite_reason_{i}')
        
        # Append the step information as a dictionary to the list
        steps_data.append({
            'accuracy': accuracy,
            'llm_or_python': llm_or_python,
            'original_step': original_step,
            'rewrite': rewrite,
            'rewrite_reason': rewrite_reason
        })
    else:
        # Append only the basic step information if the step is correct
        steps_data.append({
            'accuracy': accuracy,
            'llm_or_python': llm_or_python
        })

# Display the list of steps data as a copyable text
if steps_data:
    st.write("### Copyable List of Objects:")
    
    # Convert the list of objects (steps_data) to a string format
    copyable_output = "\n".join([str(step) for step in steps_data])
    
    # Show the output in a text area that the user can copy
    st.text_area("Generated Steps Data (Copy below):", value=copyable_output, height=200)
