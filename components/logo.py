from PIL import Image

def add_logo(canvas, logo_path, padding=(20, 20)):
    """Adds a logo to the top-right corner of the canvas."""
    try:
        logo = Image.open(logo_path).convert("RGBA")
        logo_width, logo_height = logo.size
        position = (canvas.width - logo_width - padding[0], padding[1])
        canvas.paste(logo, position, logo)
    except IOError:
        return canvas  # Return unchanged canvas if the logo file is missing