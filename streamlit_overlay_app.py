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

# Initialize Canvas
canvas_color = st.color_picker("Canvas Background Color", "#FFFFFF")
canvas = create_canvas(CANVAS_SIZE, canvas_color)

# Display Sticky Canvas Preview
st.markdown(
    """
    <style>
    .sticky-canvas {
        position: -webkit-sticky; /* For Safari */
        position: sticky;
        top: 0;
        z-index: 10;
        background-color: white;
        padding: 10px 0;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="sticky-canvas">
        <img src="data:image/png;base64,{}" alt="Canvas Preview" style="width: 100%; max-width: 1000px;">
    </div>
    """.format(canvas._repr_png_().decode("utf-8")),
    unsafe_allow_html=True,
)

# Tools Section
st.header("Editing Tools")

# Add Overlay
st.subheader("Overlay Tools")
canvas = add_overlay(canvas)

# Add Logo
add_logo(canvas, LOGO_PATH)

# Add Text
st.subheader("Text Tools")
canvas = add_text(canvas, FONT_PATH)

# Crop Canvas
st.subheader("Cropping Tools")
canvas = crop_canvas(canvas)

# Save and Download Final Image
final_image_path = "final_canvas.png"
canvas.save(final_image_path)
with open(final_image_path, "rb") as file:
    st.download_button("Download Final Image", data=file, file_name="final_image.png", mime="image/png")