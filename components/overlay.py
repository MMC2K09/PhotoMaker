import streamlit as st
from PIL import Image

def add_overlay(canvas):
    overlay_file = st.file_uploader("Upload Overlay", type=["png", "jpg", "jpeg"])
    if overlay_file:
        overlay = Image.open(overlay_file).convert("RGBA")
        resize_width = st.slider("Width", 50, canvas.width, overlay.width)
        resize_height = st.slider("Height", 50, canvas.height, overlay.height)
        overlay = overlay.resize((resize_width, resize_height))
        x = st.slider("X Position", 0, canvas.width - resize_width, 0)
        y = st.slider("Y Position", 0, canvas.height - resize_height, 0)
        opacity = st.slider("Opacity", 0.0, 1.0, 1.0)
        if opacity < 1.0:
            overlay.putalpha(int(255 * opacity))
        canvas.paste(overlay, (x, y), overlay)
    return canvas