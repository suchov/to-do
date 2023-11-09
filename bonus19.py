import streamlit as st
from PIL import Image


with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render gray scale image on the web page
    st.image(gray_img)
