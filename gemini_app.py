import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

def gemini(prompt):
    genai.configure(api_key="AIzaSyAaW1FgmWvCwkouc18yZ2GeAXNyWXcc6VQ")
    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
    ]
    model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config,safety_settings=safety_settings)
    prompt_input = prompt
    prompt_parts = [
    {
        "text": prompt_input
    }
    ]
    response = model.generate_content(prompt_parts)
    # Iterate through each candidate in the response
    for candidate in response.candidates:
        # Access the parts directly from the content of the candidate
        for part in candidate.content.parts:
            # Print the text attribute of the part
            output = part.text
            print(output)
            return output
            

st.title("Gemini ChatBot")
form = st.form(key='my_form')
name = form.text_input(label='Please ask the question!')
submit_button = form.form_submit_button(label='Submit')

# function all
data = gemini(name)
# st.form_submit_button returns True upon form submit
if submit_button:
    
    st.write(data)
    
        

