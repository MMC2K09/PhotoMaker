import streamlit as st
from PIL import Image

# App title and description
st.title("🎨 PNG Overlay Tool")
st.write(
    """
    Upload a base image and one or more PNG overlays. Adjust their size and position 
    to create a new image. Download your final result.
    """
)

# File uploader for the base image
st.header("Step 1: Upload the Base Image")
base_image_file = st.file_uploader("Upload a Base Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Check if the base image is uploaded
if base_image_file:
    base_image = Image.open(base_image_file).convert("RGBA")
    st.image(base_image, caption="Base Image", use_column_width=True)

    # File uploader for overlay images
    st.header("Step 2: Upload Overlay Images")
    overlay_files = st.file_uploader("Upload Overlay Images (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if overlay_files:
        # Process overlays
        overlays = [Image.open(file).convert("RGBA") for file in overlay_files]
        
        # Sidebar for adjustments
        st.sidebar.header("Adjust Overlays")
        overlayed_images = []

        for i, overlay in enumerate(overlays):
            st.sidebar.subheader(f"Overlay {i + 1}")
            x = st.sidebar.slider(f"X Position (Overlay {i + 1})", 0, base_image.width, 0)
            y = st.sidebar.slider(f"Y Position (Overlay {i + 1})", 0, base_image.height, 0)
            scale = st.sidebar.slider(f"Scale % (Overlay {i + 1})", 10, 200, 100)

            # Resize overlay
            overlay_resized = overlay.resize(
                (
                    int(overlay.width * scale / 100),
                    int(overlay.height * scale / 100),
                )
            )
            overlayed_images.append((overlay_resized, (x, y)))

        # Merge overlays with the base image
        base_image_copy = base_image.copy()
        for overlay_resized, position in overlayed_images:
            base_image_copy.paste(overlay_resized, position, overlay_resized)

        # Display the final image
        st.header("Step 3: Final Image")
        st.image(base_image_copy, caption="Final Image", use_column_width=True)

        # Download button for the final image
        final_image_path = "final_image.png"
        base_image_copy.save(final_image_path)
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