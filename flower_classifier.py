from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
#import matplotlib.pyplot as plt

import numpy as np
from PIL import Image

def resize_image(image, target_size=(100, 100)):
    # Convert the image (PIL or NumPy) to a PIL Image if necessary
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    
    # Resize the image
    resized_image = image.resize(target_size)
    
    # Convert back to NumPy array
    return np.array(resized_image)

# Example usage



def flower_classification(img, weights_file):
    # Load the model
    #class labels from the iterator
    class_labels = {'daisy': 0, 'dandelion': 1, 'rose': 2, 'sunflower': 3, 'tulip': 4}
    model = load_model( weights_file)

    # Create the array of the right shape to feed into the keras model
    #data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    #data = np.ndarray(shape=(224, 224, 3), dtype=np.float32)
    #image = img
    #img = load_img(img, target_size=(100,100))
    img = resize_image(img, target_size=(100, 100))
    img = img_to_array(img)
    img = img.reshape(1,100,100,3)
    result = model.predict(img)
    result = np.argmax(result) # return position of the highest probability
    prediction = [key for key in class_labels][result]
    return prediction
