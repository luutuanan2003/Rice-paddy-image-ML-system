from tensorflow.keras.preprocessing import image
import numpy as np
import io

def preprocess(image_bytes, target_size):
    img = image.load_img(io.BytesIO(image_bytes), target_size=target_size)
    x = image.img_to_array(img) / 255.0
    return x
