# app.py

import streamlit as st
from utils import load_data, clean_data

st.title("Data Cleaning App")

# Input box to paste the file path
file_path = st.text_input("C:\\Users\linga\\Desktop\\data cleaning\\netflix_titles.csv")

# Button to trigger loading
if st.button("Load and Clean Data"):
    if file_path:
        # Load data
        df = load_data(file_path)
        
        if df is not None:
            st.subheader("Original Data")
            st.dataframe(df)
            
            # Clean data
            df_clean = clean_data(df)
            
            st.subheader("Cleaned Data")
            st.dataframe(df_clean)
            
            # Option to download cleaned data
            csv = df_clean.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download cleaned CSV",
                data=csv,
                file_name='cleaned_data.csv',
                mime='text/csv'
            )
        else:
            st.error("Failed to load the data. Check the file path and try again.")
    else:
        st.warning("Please paste a valid file path.")