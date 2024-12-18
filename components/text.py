import streamlit as st
from PIL import ImageDraw, ImageFont

def add_text(canvas, font_path):
    text = st.text_input("Text", "Add your text here")
    font_size = st.slider("Font Size", 10, 100, 40)
    color = st.color_picker("Text Color", "#000000")
    y_position_below_center = st.slider("Position Below Center", 0, canvas.height // 2, 100)
    
    if text:
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]
        x = (canvas.width - text_width) // 2
        y = canvas.height // 2 + y_position_below_center
        draw.text((x, y), text, fill=color, font=font)
    return canvas