
from utils import image_caption_and_embedding
from utils import generate_embeddings
import streamlit as st

from pagination import gallery_page, upload_page, show_table

# Main function to switch between pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Upload Images", "Browse", "Captions"])
    
    if page == "Upload Images":
        upload_page()
    elif page == "Captions":
        show_table()
    else:
        gallery_page()

if __name__ == "__main__":
    main()
