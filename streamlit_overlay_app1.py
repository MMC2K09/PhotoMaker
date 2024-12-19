import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Fixed canvas size
CANVAS_SIZE = (1000, 1000)

# Load font
def load_font(font_path="assets/TiroBangla-Regular.ttf", font_size=50):
    try:
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        st.warning("Font file not found. Using default font.")
        return ImageFont.load_default()

# Create a blank canvas
def create_canvas(size, color=(255, 255, 255)):
    return Image.new("RGBA", size, color)

# Overlay an image onto the canvas
def overlay_image(canvas, overlay, position, opacity=1.0):
    overlay = overlay.convert("RGBA")
    if opacity < 1.0:
        overlay.putalpha(int(255 * opacity))
    canvas.paste(overlay, position, overlay)
    return canvas

# App title
st.title("Modern Image Overlay Tool")

# Step 1: Load base canvas
st.sidebar.header("Step 1: Base Canvas")
canvas_color = st.sidebar.color_picker("Choose Canvas Background", "#FFFFFF")
canvas_color_rgb = tuple(int(canvas_color[i:i+2], 16) for i in (1, 3, 5))  # Convert HEX to RGB
canvas = create_canvas(CANVAS_SIZE, canvas_color_rgb)

# Sidebar for adding overlays
st.sidebar.header("Step 2: Add Overlay Images")
overlay_file = st.sidebar.file_uploader("Upload an Overlay Image", type=["png", "jpg", "jpeg"])
resize_width = st.sidebar.slider("Resize Width", 50, CANVAS_SIZE[0], 200)
resize_height = st.sidebar.slider("Resize Height", 50, CANVAS_SIZE[1], 200)
overlay_x = st.sidebar.slider("X Position", 0, CANVAS_SIZE[0], 0)
overlay_y = st.sidebar.slider("Y Position", 0, CANVAS_SIZE[1], 0)
overlay_opacity = st.sidebar.slider("Opacity", 0.0, 1.0, 1.0)

if overlay_file:
    overlay = Image.open(overlay_file).convert("RGBA")
    overlay = overlay.resize((resize_width, resize_height))
    canvas = overlay_image(canvas, overlay, (overlay_x, overlay_y), overlay_opacity)

# Step 3: Add text to the canvas
st.sidebar.header("Step 3: Add Text")
text = st.sidebar.text_input("Text to Add")
text_size = st.sidebar.slider("Font Size", 10, 100, 30)
text_color = st.sidebar.color_picker("Text Color", "#000000")
text_x = st.sidebar.slider("X Position (Text)", 0, CANVAS_SIZE[0], CANVAS_SIZE[0] // 2)
text_y = st.sidebar.slider("Y Position (Text)", 0, CANVAS_SIZE[1], CANVAS_SIZE[1] - 100)

if text:
    draw = ImageDraw.Draw(canvas)
    font = load_font(font_size=text_size)
    text_position = (text_x - text_size // 2, text_y)
    draw.text(text_position, text, fill=text_color, font=font)

# Step 4: Display the final canvas
st.header("Final Canvas")
st.image(canvas, caption="Final Image", use_container_width=True)

# Step 5: Download final image
final_image_path = "final_canvas.png"
canvas.save(final_image_path)
with open(final_image_path, "rb") as file:
    st.download_button("Download Final Image", data=file, file_name="final_image.png", mime="image/png")
