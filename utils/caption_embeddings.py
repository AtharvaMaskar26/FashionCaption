from sentence_transformers import SentenceTransformer


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embeddings(caption: str) -> list:
    """
    Description:
        - This function generates embeddings for a given caption using the sentence-transformers

    Parameters:
        - caption (str): Caption to embed.

    Returns:    
        - caption_encoding (list): Encoding of the caption
    """
    return model.encode(caption)