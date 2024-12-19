from PIL import Image

def create_canvas(size, color):
    """Creates a blank canvas with the given size and background color."""
    color_rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
    return Image.new("RGBA", size, color_rgb)