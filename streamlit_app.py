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
st.title("Modular Image Overlay Tool")

# Step 1: Create Base Canvas
canvas_color = st.color_picker("Canvas Background", "#FFFFFF")
canvas = create_canvas(CANVAS_SIZE, canvas_color)

# Step 2: Add Overlay
st.header("Add Overlay Image")
canvas = add_overlay(canvas)

# Step 3: Add Logo
add_logo(canvas, LOGO_PATH)

# Step 4: Add Text
st.header("Add Text")
canvas = add_text(canvas, FONT_PATH)

# Step 5: Crop Canvas
st.header("Crop Canvas")
canvas = crop_canvas(canvas)

# Step 6: Display and Download
st.image(canvas, caption="Final Image", use_container_width=True)
canvas.save("final_image.png")
with open("final_image.png", "rb") as file:
    st.download_button("Download Image", data=file, file_name="final_image.png", mime="image/png")
