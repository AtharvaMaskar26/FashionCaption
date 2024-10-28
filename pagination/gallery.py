import streamlit as st
import os 
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from utils import generate_embeddings

# Page 2: Gallery View
def gallery_page():
    st.title("Browse Our Collections")

    if os.path.exists('captions.xlsx'):
        df = pd.read_excel('captions.xlsx')

        # Initialize Similarity column if it doesn't exist
        if 'Similarity' not in df.columns:
            df['Similarity'] = 0.0  # Default to zero if not calculated

        # Search functionality with a unique key
        query = st.text_input("What are you looking for today?", "", key="search_input")  # Add a unique key here
        
        if query:
            query_embedding = generate_embeddings(query)
            similarities = []

            # Convert the embeddings back to numpy arrays
            for emb in df['Embeddings']:
                emb_array = np.fromstring(emb[1:-1], sep=',')  # Convert string back to numpy array
                similarity = cosine_similarity([query_embedding], [emb_array])[0][0]
                similarities.append(similarity)

            df['Similarity'] = similarities
            
            # Filter based on a threshold
            df = df[df['Similarity'] > 0.4  ]  
            if df.empty:
                st.write("No results found for your search.")
                return  # Exit early if no results

            df = df.sort_values(by='Similarity', ascending=False)

        # Create a grid layout for the gallery
        st.subheader("Gallery View")
        cols = st.columns(3)  # Create 3 columns for the gallery

        for index, row in df.iterrows():
            col_index = index % 3  # Cycle through columns
            with cols[col_index]:
                st.image(row['Image Path'], use_column_width=True)
                st.write(f"**Caption:** {row['Caption Generated']}")
                
                # Display the cosine similarity score
                st.write(f"**Cosine Similarity:** {row['Similarity']:.4f}")  # Format the similarity to 4 decimal places
