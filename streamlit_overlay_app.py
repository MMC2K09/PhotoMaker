import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Function to add text to an image
def add_text_to_image(image, text, position, font_size=50, font_color=(255, 255, 255)):
    draw = ImageDraw.Draw(image)
    try:
        # Load your custom font
        font = ImageFont.truetype("assets/TiroBangla-Regular.ttf", font_size)
    except IOError:
        # Fallback if the font file is not found
        st.warning("Font file not found. Please ensure TiroBangla-Regular.ttf is in the assets folder.")
        font = ImageFont.load_default()
    
    # Calculate text size
    text_width, text_height = draw.textsize(text, font=font)
    
    # Adjust position for centered alignment
    position = (position[0] - text_width // 2, position[1])
    
    # Draw text
    draw.text(position, text, font=font, fill=font_color)
    return image

# App title and description
st.title("🎨 Image Overlay Tool")
st.write(
    """
    Upload a base image (PNG, JPG, or JPEG) and one or more overlay images (PNG, JPG, or JPEG). 
    Adjust their size and position to create a new combined image. Add text to the bottom as a heading!
    """
)

# File uploader for the base image
st.header("Step 1: Upload the Base Image")
base_image_file = st.file_uploader(
    "Upload a Base Image (PNG, JPG, or JPEG)", type=["png", "jpg", "jpeg"]
)

# Check if the base image is uploaded
if base_image_file:
    base_image = Image.open(base_image_file).convert("RGBA")
    st.image(base_image, caption="Base Image", use_container_width=True)

    # File uploader for overlay images
    st.header("Step 2: Upload Overlay Images")
    overlay_files = st.file_uploader(
        "Upload Overlay Images (PNG, JPG, or JPEG)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
    )

    # Load the app's logo (from file, not uploaded by the user)
    logo = Image.open("assets/logo.png").convert("RGBA")  # Adjust path as needed

    # Resize the logo
    logo_size = (100, 100)  # Customize the size of the logo
    logo = logo.resize(logo_size)

    # Check if overlay images are uploaded
    if overlay_files:
        overlays = [Image.open(file).convert("RGBA") for file in overlay_files]

        # Add the first overlay in the top portion
        second_overlay = overlays[0]
        max_height = base_image.height // 2  # Limiting to top portion
        second_overlay = second_overlay.resize(
            (base_image.width, min(second_overlay.height, max_height))
        )
        base_image.paste(second_overlay, (0, 0), second_overlay)

        # Overlay the logo in the top-right corner
        logo_x = base_image.width - logo.width - 20  # 20px padding from right
        logo_y = 20  # 20px padding from top
        base_image.paste(logo, (logo_x, logo_y), logo)

        # Add text heading below the center line (in the bottom half)
        text = "This is a Heading!"  # Customize this text as needed
        base_image = add_text_to_image(base_image, text, (base_image.width // 2, base_image.height // 2 + 100))

        # Display the final image
        st.header("Step 3: Final Image")
        st.image(base_image, caption="Final Image", use_container_width=True)

        # Download button for the final image
        final_image_path = "final_image.png"
        base_image.save(final_image_path)
        with open(final_image_path, "rb") as file:
            st.download_button(
                label="Download Final Image",
                data=file,
                file_name="final_image.png",
                mime="image/png",
            )
    else:
        st.warning("Please upload at least one overlay image.")
else:
    st.info("Please upload a base image to start.")