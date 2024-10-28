import streamlit as st
import pandas as pd
from PIL import Image
import os

from utils import image_caption_and_embedding
from utils import generate_embeddings

# Page 1: Upload Images and Generate Captions
def upload_page():
    st.title("Upload Images")
    
    # Create directory for processed images if it doesn't exist
    image_directory = 'processed_images'
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    # Uploading images
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if uploaded_files:
        captions = []
        embeddings = []
        image_paths = []
        
        for uploaded_file in uploaded_files:
            # Save the uploaded image to the processed_images directory
            image = Image.open(uploaded_file)
            image_path = os.path.join(image_directory, uploaded_file.name)
            image.save(image_path)
            image_paths.append(image_path)
            
            # Implement your caption generation logic here
            caption = image_caption_and_embedding(image_path)
            captions.append(caption)

            # Generate embeddings
            embedding = generate_embeddings(caption)
            embeddings.append(embedding)

        # Create a DataFrame and save to Excel
        data = {
            'Sr. No': list(range(1, len(uploaded_files) + 1)),
            'Image Name': [file.name for file in uploaded_files],
            'Image Path': image_paths,
            'Caption Generated': captions,
            'Embeddings': [embedding.tolist() for embedding in embeddings]  # Convert to list for Excel
        }
        df = pd.DataFrame(data)
        df.to_excel('captions.xlsx', index=False)
        st.success("Captions generated and saved successfully!")
