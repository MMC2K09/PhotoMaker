import streamlit as st
from components.canvas import create_canvas
from components.logo import add_logo
from components.overlay import add_overlay
from components.text import add_text
from components.cropping import crop_canvas

# Constants
CANVAS_SIZE = (1000, 1000)
LOGO_PATH = "assets/logo.png"
FONT_PATH = "assets/TiroBangla-Regular.ttf"

# App Title
st.title("Fixed Canvas Image Editor")

# Step 1: Initialize Canvas
canvas_color = st.color_picker("Canvas Background Color", "#FFFFFF")
canvas = create_canvas(CANVAS_SIZE, canvas_color)

# Step 2: Display Initial Canvas
st.image(canvas, caption="Canvas Preview", use_container_width=True)

# Step 3: Add Overlay
st.header("Overlay Tools")
canvas = add_overlay(canvas)

# Step 4: Add Logo
add_logo(canvas, LOGO_PATH)

# Step 5: Add Text
st.header("Text Tools")
canvas = add_text(canvas, FONT_PATH)

# Step 6: Crop Canvas
st.header("Cropping Tools")
canvas = crop_canvas(canvas)

# Step 7: Updated Canvas Preview
st.image(canvas, caption="Updated Canvas Preview", use_container_width=True)

# Step 8: Download Final Image
final_image_path = "final_canvas.png"
canvas.save(final_image_path)
with open(final_image_path, "rb") as file:
    st.download_button("Download Final Image", data=file, file_name="final_image.png", mime="image/png")