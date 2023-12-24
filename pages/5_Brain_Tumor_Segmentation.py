import streamlit as st
import os
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
from keras.models import load_model
import tempfile
import shutil
from constant import *

# Initialize the Streamlit app
st.title('Brain Tumor Classifier')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")
st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)



# Load the pre-trained model
model = load_model('braintumor.h5')
class_labels = [
    "Glioma Tumor",
    "Meningioma Tumor",
    "No Brain Tumor",
    "Pituitary Tumor",
    "Unknown Tumor"  # Handle cases outside the defined categories
]

def get_class_name(class_no):
    return class_labels[class_no]

def classify_image(img):
    image = cv2.imread(img)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((150, 150))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    class_probabilities = model.predict(input_img)[0]
    predicted_class = int(np.argmax(class_probabilities))
    
    return predicted_class

# Create a file uploader to upload an MRI image
uploaded_image = st.file_uploader('Upload an MRI image', type=['jpg', 'jpeg', 'png'])

if uploaded_image:
    st.image(uploaded_image, caption='Uploaded MRI Image', use_column_width=True)
    
    if st.button('Classify'):
        with st.spinner('Classifying...'):
            try:
                # Create a temporary directory
                temp_dir = tempfile.mkdtemp()
                img_path = os.path.join(temp_dir, 'temp_image.jpg')
                uploaded_image.seek(0)
                with open(img_path, 'wb') as out_file:
                    shutil.copyfileobj(uploaded_image, out_file)
                predicted_class = classify_image(img_path)
                result = get_class_name(predicted_class)
                st.success(f'Predicted Tumor Type: {result}')
            except Exception as e:
                st.error(f'An error occurred: {str(e)}')
            finally:
                shutil.rmtree(temp_dir)
