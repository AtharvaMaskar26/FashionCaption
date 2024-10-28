import streamlit as st
import pandas as pd
def show_table():
    st.title("Captions sheet.")
    df = pd.read_excel("D:\Fashion Captioning\captions.xlsx")
    st.table(df.iloc[:, :-1])