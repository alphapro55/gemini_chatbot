import streamlit as st
import google.generativeai as genai

col1, col2 = st.columns([1, 6])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.title("ChatBot By AlphaLogics")

# Configure Gemini API
genai.configure(api_key="AIzaSyAaW1FgmWvCwkouc18yZ2GeAXNyWXcc6VQ")  # Replace with your API key

# Set up model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]
model = genai.GenerativeModel(
    model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        prompt_parts = [{"text": prompt}]
        response = model.generate_content(prompt_parts)
        for candidate in response.candidates:
            for part in candidate.content.parts:
                full_response += part.text
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
