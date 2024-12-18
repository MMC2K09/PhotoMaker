import streamlit as st

def crop_canvas(canvas):
    crop_left = st.slider("Crop Left", 0, canvas.width // 2, 0)
    crop_top = st.slider("Crop Top", 0, canvas.height // 2, 0)
    crop_right = st.slider("Crop Right", canvas.width // 2, canvas.width, canvas.width)
    crop_bottom = st.slider("Crop Bottom", canvas.height // 2, canvas.height, canvas.height)
    if st.button("Apply Crop"):
        canvas = canvas.crop((crop_left, crop_top, crop_right, crop_bottom))
    return canvas