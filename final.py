import streamlit as st
import openai
import requests
import speech_recognition as sr
from io import BytesIO

# Define Azure OpenAI connection details
azure_openai_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Replace with your actual key
azure_openai_endpoint = 'https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview'  # Replace with your actual endpoint URL

# Function to get GPT-4 response for correcting errors in extracted text
def get_response_from_openai(user_input):
    headers = {
        "Content-Type": "application/json",
        "api-key": azure_openai_key,
    }
    
    data = {
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": f"Please correct the following text: {user_input}"}],
        "max_tokens": 4096,  # Adjust token limit if needed
    }
    
    # Send the request to Azure OpenAI
    response = requests.post(azure_openai_endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Convert audio to text using speech recognition (Google/Whisper API)
def extract_text_from_audio(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Recognize speech using Google Web Speech API (or another service)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
    return None

def main():
    st.title("Correct Errors in Speech Using Azure OpenAI GPT-4")
    
    # Upload .wav file
    uploaded_file = st.file_uploader("Upload a .wav audio file", type=["wav"])
    
    if uploaded_file is not None:
        st.write(f"Processing uploaded audio file: {uploaded_file.name}")
        
        # Convert the uploaded file to a format that can be read by speech recognition
        audio_bytes = uploaded_file.read()
        audio_data = BytesIO(audio_bytes)
        
        # Extract text from the uploaded audio file
        extracted_text = extract_text_from_audio(audio_data)
        
        if extracted_text:
            st.write("**Extracted Text from Audio:**")
            st.write(extracted_text)
            
            # Button to send the extracted text to GPT-4 for correction
            if st.button("Correct Text"):
                # Get the response from OpenAI for correction
                corrected_text = get_response_from_openai(extracted_text)
                
                if corrected_text:
                    st.write("**Corrected Text:**")
                    st.write(corrected_text)
    else:
        st.write("Please upload a .wav file to proceed.")

if __name__ == "__main__":
    main()
