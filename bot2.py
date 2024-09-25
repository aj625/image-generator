#import necessary modules
import openai  # Correct import for OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

# Initialize your image generation client
openai.api_key = apikey  # Correctly set the API key for the client

def generate_images(image_description, num_images):
    img_responder = openai.Image.create(
        prompt=image_description,
        size="1024x1024",  # Ensure this is formatted correctly
        n=num_images  # Use the `num_images` parameter
    )
    image_urls = [data['url'] for data in img_responder['data']]  # Extract URLs from response
    return image_urls

# Set page configuration
st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")

# Create a title
st.title("DALL-E-3 Image Generation Tool")

# Create a subheader
st.subheader("POWERED BY The World's Most Powerful Image Generation API - DALL-E")

# Input for image description
img_description = st.text_input("Enter a description for the image you want to generate")

# Number input for selecting the number of images
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=10, value=1)

# Create a button for image generation
if st.button("Generate Images"):
    if img_description:
        image_urls = generate_images(img_description, num_of_images)
        for image_url in image_urls:
            st.image(image_url)  # Display each generated image
    else:
        st.error("Please enter a description for the image!")
