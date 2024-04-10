from fastapi import FastAPI, UploadFile, File
from typing import Union
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model('mymodel.keras')

# Define a function to process the uploaded image
def process_image(file) -> np.ndarray:
    img = tf.image.decode_image(file.read(), channels=3)
    img = tf.image.rgb_to_grayscale(img)  # Convert to grayscale
    img = tf.image.resize(img, (28, 28))
    img = img / 255.0
    img = img.numpy()
    print(img.shape,type(img))
    return img

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def read_item(img:UploadFile = File(...)):
    
    processed_img = process_image(img.file)
    processed_img = np.expand_dims(processed_img, axis=0)    
    prediction = model.predict(processed_img)
    print(prediction)
    predicted_class = np.argmax(prediction) 
    print(predicted_class)
    return {"predicted_number": int(predicted_class)}
