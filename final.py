import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Azure OpenAI connection details
azure_openai_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Replace with your actual key
azure_openai_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"  # Replace with your actual endpoint URL

# Function to generate images using Azure OpenAI
def generate_image(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": azure_openai_key,
    }
    
    data = {
        "prompt": prompt,
        "n": 1,  # Number of images to generate
        "size": "1024x1024"  # Image size
    }

    response = requests.post(azure_openai_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        return image_url
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Function to display the generated image
def display_image_from_url(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="Generated Image", use_column_width=True)

def main():
    st.title("Azure OpenAI Image Generator")

    # Input text prompt for image generation
    prompt = st.text_input("Enter a prompt to generate an image:")

    # Button to trigger image generation
    if st.button("Generate Image"):
        if prompt:
            st.write("Generating image, please wait...")
            image_url = generate_image(prompt)
            if image_url:
                st.write("Image generated successfully!")
                display_image_from_url(image_url)
        else:
            st.warning("Please enter a prompt to generate an image.")

if __name__ == "__main__":
    main()
