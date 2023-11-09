import streamlit as st
from PIL import Image


uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render gray scale image on the web page
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)

    gray_img = img.convert("L")

    st.image(gray_img)
