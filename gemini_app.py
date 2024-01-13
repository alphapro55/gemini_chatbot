import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound

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
            


# form = st.form(key='my_form')
# name = form.text_input(label='Please ask the question!')
# submit_button = form.form_submit_button(label='Submit')

# # function all
# data = gemini(name)
# # st.form_submit_button returns True upon form submit
# if submit_button:
    
#     st.write(data)
    
        

# def text_to_speech(text):
#     """
#     Converts text to speech using gTTS and plays the audio file.

#     Args:
#         text: The text to convert to speech.
#     """

#     # Create a gTTS object
#     tts = gTTS(text=text, lang='en')

#     # Save the audio file
#     audio_file = 'audio.mp3'
#     tts.save(audio_file)

#     # Play the audio file
#     playsound(audio_file)
    
# form = st.form(key='my_form')
# name = form.text_input(label='Please ask the question!')
# submit_button = form.form_submit_button(label='Submit')

# # function all
# data = gemini(name)
# # st.form_submit_button returns True upon form submit
# # if submit_button:
#     # st.write(data)
#     # Add a button to play the audio
# if st.button('Hear the response'):
#     text_to_speech(data)
# # Add a speaker icon to the button
# hear_button = st.button('Hear the response')
# hear_button.button_html("""
# <button type="button" class="btn btn-primary">
# <i class="fa fa-volume-up"></i>
# Hear the response
# </button>
# """)


# -------------------------------------------------new one



from pydub import AudioSegment
from pydub.playback import play

# Define the text-to-speech function
def text_to_speech(text):
    """
    Converts text to speech using gTTS and plays the audio file.

    Args:
        text: The text to convert to speech.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Convert the audio to an in-memory file
    audio_data = tts.get_audio_data()

    # Play the in-memory audio
    play(AudioSegment.from_file_in_memory(audio_data, format="mp3"))

# Streamlit app code
st.title("Text-to-Speech App")

# Create a form to take user input
form = st.form(key='my_form')
name = form.text_input(label='Please ask the question!')
submit_button = form.form_submit_button(label='Submit')

# Process the data on form submission
if submit_button:
    # Call the function to get the response data
    data = gemini(name)
    
    # Display the response data
    st.write("Response:", data)

    # Add a button to play the audio
    if st.button('Hear the response'):
        text_to_speech(data)