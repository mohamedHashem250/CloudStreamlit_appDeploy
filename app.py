import streamlit as st
import tensorflow as tf
from PIL import Image
from flower_classifier import flower_classification

# Your classifier code here
def classify_image(image):
    # Load and preprocess the image, then run your model for classification
    pass

st.title("Deep Learning Classifier")
uploaded_file = st.file_uploader("Choose an image", type="jpg")
st.header("Flower Classification Example")
st.text("Upload a Flower Image for flower classification as SunRose , Rose, Diasy")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")
    label = classify_image(image)
    st.write(f"Prediction: {label}")
    label = flower_classification(image, 'hyper_tuned_model.h5')
    if label == 'daisy':
  	    st.write("The Flower is  daisy")
    elif label ==  'dandelion':
  	    st.write("The Flower is  daisy")
    elif label ==  'rose':
  	    st.write("The Flower is  rose")
    elif label == 'sunflower':
  	    st.write("The Flower is  Sunflower")
    else:
  	    st.write("The Flower is  tulip")
