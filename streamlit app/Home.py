import streamlit as st
import base64


st.set_page_config(page_title="MIMIC-III Readmission Predictor",layout="wide", initial_sidebar_state="collapsed")
# Function to set background image

def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # Set background image (replace 'background.jpg' with your image file path)
set_background("background.png")


st.text("        ")
st.text("        ")
st.text("        ")
#st.image("hospital_banner.png", use_container_width=True)
st.title("🏥 MIMIC-III Hospital Readmission Predictor")
st.markdown("Analyze patient records, assess readmission risk, and analyze clinical notes using AI and LLMs.")
st.text("        ")
st.text("        ")
st.text("        ")
# Search bar at the center

search_query = st.text_input("", placeholder="Search here...", key="search", help="Type and press Enter")

st.markdown("<br><br>", unsafe_allow_html=True)

# Three clickable bubbles
col1, col2, col3, col4, col5 = st.columns(5,gap="medium")

with col1:
    st.text("        ")
with col2:
    if st.button("🚀 Patient Portal",use_container_width=True):
        st.switch_page("pages/Patient_Data.py")

with col3:
    if st.button("🏥 Departments", use_container_width=True):
        st.switch_page("pages/Department.py")

with col4:
    if st.button("📊 Overview", use_container_width=True):
        st.switch_page("pages/Overview.py")
with col5:
    st.text("        ")