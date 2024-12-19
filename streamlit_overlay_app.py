import streamlit as st
import base64
from io import BytesIO
from components.canvas import create_canvas
from components.logo import add_logo
from components.overlay import add_overlay
from components.text import add_text
from components.cropping import crop_canvas

# Constants
CANVAS_SIZE = (1000, 1000)
LOGO_PATH = "assets/logo.png"
FONT_PATH = "assets/TiroBangla-Regular.ttf"

# Function to Convert Image to Base64
def image_to_base64(img):
    """Converts a PIL image to a Base64-encoded string."""
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_bytes = buffer.getvalue()
    return base64.b64encode(img_bytes).decode("utf-8")

# App Title
st.title("Fixed Canvas Image Editor")

# Step 1: Initialize Canvas
canvas_color = st.color_picker("Canvas Background Color", "#FFFFFF")
canvas = create_canvas(CANVAS_SIZE, canvas_color)

# Step 2: Convert Canvas to Base64
canvas_base64 = image_to_base64(canvas)

# Step 3: Display Sticky Canvas Preview
st.markdown(
    f"""
    <style>
    .sticky-canvas {{
        position: -webkit-sticky; /* For Safari */
        position: sticky;
        top: 0;
        z-index: 10;
        background-color: white;
        padding: 10px 0;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }}
    </style>
    <div class="sticky-canvas">
        <img src="data:image/png;base64,{canvas_base64}" alt="Canvas Preview" style="width: 100%; max-width: 1000px;">
    </div>
    """,
    unsafe_allow_html=True,
)

# Tools Section
st.header("Editing Tools")

# Step 4: Add Overlay
st.subheader("Overlay Tools")
canvas = add_overlay(canvas)

# Step 5: Add Logo
add_logo(canvas, LOGO_PATH)

# Step 6: Add Text
st.subheader("Text Tools")
canvas = add_text(canvas, FONT_PATH)

# Step 7: Crop Canvas
st.subheader("Cropping Tools")
canvas = crop_canvas(canvas)

# Step 8: Convert Final Canvas to Base64 for Sticky Preview Update
final_canvas_base64 = image_to_base64(canvas)

# Step 9: Save and Download Final Image
final_image_path = "final_canvas.png"
canvas.save(final_image_path)
with open(final_image_path, "rb") as file:
    st.download_button("Download Final Image", data=file, file_name="final_image.png", mime="image/png")