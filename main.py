import streamlit as st

# Importing processing modules
import has_con
import image_proc
import text_proc
import recom

# Streamlit app title
st.title("Multi-Process Streamlit App")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio(
    "Select a Page", 
    ["Home", "E-commerce Conversion", "Image Processing", "Text Processing", "Recommendation System"]
)

# Home Page
if selected_page == "Home":
    st.header("Welcome to the Multi-Processing App")
    st.write("Select an option from the sidebar to proceed.")

# E-commerce Conversion Page
elif selected_page == "E-commerce Conversion":
    st.header("E-commerce Conversion Analysis")
    
    # File uploader only appears on this page
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"], key="ecommerce_upload")
    
    if uploaded_file is not None:
        has_con.process_file(uploaded_file)  # Calls function in has_con.py to handle processing

# Image Processing Page
elif selected_page == "Image Processing":
    #st.header("Image Processing")
    image_proc.process_image()

# Text Processing Page
elif selected_page == "Text Processing":
   # st.header("Text Processing")
    text_proc.process_text()

# Recommendation System Page
elif selected_page == "Recommendation System":
    #st.header("Recommendation System")
    recom.process_recommendation()
