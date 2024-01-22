import streamlit as st
from PIL import Image
import time
import threading
from constant import *

#------------------- Power BI---------------------#
# Define a list of image paths
image_paths = ["images/image1.jpg", "images/image2.JPG", "images/image3.JPG", "images/image4.JPG", "images/image5.JPG", "images/image6.JPG", "images/image7.PNG", "images/image8.PNG", "images/image9.PNG", "images/image10.PNG"]

# Create a function to display a single image within a fixed box
def image_slideshow(image_paths):
    st.subheader("Several snapshots of my work in PowerBI")
    image_placeholder = st.empty()
    idx = 0

    while True:
        image = Image.open(image_paths[idx])
        image_placeholder.image(image, use_column_width=True)
        time.sleep(3)  # Adjust the time interval (in seconds) between slides
        idx = (idx + 1) % len(image_paths)

# Start the image slideshow in a separate thread
slideshow_thread = threading.Thread(target=image_slideshow, args=(image_paths,))
slideshow_thread.daemon = True
slideshow_thread.start()

with st.container():
    # Divide the container into three columns
    col1, col2, col3 = st.columns([0.475, 0.475, 0.05])

    # Load custom CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("style/style.css")

    #st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

    # Title
    st.title("🫶 PowerBI works")

    # Display the image slideshow
    image_slideshow(image_paths)
# Gracefully stop the slideshow thread when the Streamlit app is closed
if st._is_running:
    stop_slideshow = True
    slideshow_thread.join()
