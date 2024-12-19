import streamlit as st
from PIL import Image

def add_overlay(canvas):
    """Adds an overlay image to the canvas."""
    overlay_file = st.file_uploader("Upload an Overlay Image", type=["png", "jpg", "jpeg"])
    if overlay_file:
        overlay = Image.open(overlay_file).convert("RGBA")
        resize_width = st.slider("Overlay Width", 50, canvas.width, overlay.width)
        resize_height = st.slider("Overlay Height", 50, canvas.height, overlay.height)
        overlay = overlay.resize((resize_width, resize_height))

        x = st.slider("Overlay X Position", 0, canvas.width - resize_width, 0)
        y = st.slider("Overlay Y Position", 0, canvas.height - resize_height, 0)
        opacity = st.slider("Overlay Opacity", 0.0, 1.0, 1.0)

        # Adjust opacity
        overlay = overlay.convert("RGBA")
        if opacity < 1.0:
            alpha = int(255 * opacity)
            overlay.putalpha(alpha)

        # Paste overlay onto the canvas
        canvas.paste(overlay, (x, y), overlay)

    return canvas