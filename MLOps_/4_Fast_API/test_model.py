import tensorflow as tf
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
import numpy as np

loaded_model = tf.keras.models.load_model('mymodel.keras')
print(loaded_model.summary())


for i in range(10):
    with Image.open(f'./imgs/{i}.png') as img:
        img = ImageOps.grayscale(img)
        img = np.expand_dims(img,-1)
        plt.imshow(img)
        
        my_img = np.array(img)
        my_img = np.expand_dims(my_img,0)
        prediction = loaded_model.predict(my_img)
        prediction = np.argmax(prediction,axis=1)
        plt.title(f'Model Predict ({prediction})')
        plt.show()
        


