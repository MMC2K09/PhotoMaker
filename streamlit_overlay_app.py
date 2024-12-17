import streamlit as st
from PIL import Image

# Title of the app
st.title("🎨 PNG Overlay Tool")

st.write(
    """
    Upload a base image and one or more PNG overlays, adjust their size and position, 
    and generate a new combined image.
    """
)

# Sidebar for image uploads
st.sidebar.header("Upload Images")
base_image_file = st.sidebar.file_uploader("Upload Base Image (PNG)", type="png")
overlay_files = st.sidebar.file_uploader(
    "Upload Overlay Images (PNG, multiple allowed)", type="png", accept_multiple_files=True
)

if base_image_file:
    # Display the base image
    base_image = Image.open(base_image_file).convert("RGBA")
    st.image(base_image, caption="Base Image", use_column_width=True)

    if overlay_files:
        overlays = [Image.open(file).convert("RGBA") for file in overlay_files]

        # Prepare user inputs for adjustments
        st.sidebar.header("Overlay Adjustments")
        overlayed_images = []

        for i, overlay in enumerate(overlays):
            st.sidebar.subheader(f"Overlay {i + 1}")
            x = st.sidebar.slider(f"X Position (Overlay {i + 1})", 0, base_image.width, 0)
            y = st.sidebar.slider(f"Y Position (Overlay {i + 1})", 0, base_image.height, 0)
            scale = st.sidebar.slider(f"Scale % (Overlay {i + 1})", 10, 200, 100)

            # Resize the overlay based on scale
            overlay_resized = overlay.resize(
                (
                    int(overlay.width * scale / 100),
                    int(overlay.height * scale / 100),
                )
            )
            overlayed_images.append((overlay_resized, (x, y)))

        # Merge overlays onto the base image
        base_image_copy = base_image.copy()
        for overlay_resized, position in overlayed_images:
            base_image_copy.paste(overlay_resized, position, overlay_resized)

        # Display the final image
        st.image(base_image_copy, caption="Final Image", use_column_width=True)

        # Download option
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