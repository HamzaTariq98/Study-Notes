import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
import os


def preprocessor(sample):
    img = tf.image.convert_image_dtype(sample['image'],dtype=tf.float32)
    img = img/255.
    return img,sample['label']


train_data = tfds.load('mnist', split='train', shuffle_files=True,batch_size=32)
train_data = train_data.map(preprocessor).prefetch(tf.data.AUTOTUNE)


test_images_name = os.listdir('./imgs')


test_label = [int(img[0]) for img in test_images_name]
test_label = np.array(test_label)
test_label = np.expand_dims(test_label,-1)
test_images = []

for img in test_images_name:
    with Image.open(f'./imgs/{img}') as image:
        image = ImageOps.grayscale(image)
        image = np.array(image)/255.
        image = np.expand_dims(image,-1)
        image = image.astype(np.float32)
        image = np.expand_dims(image,0)
        test_images.append(image)
test_images = np.array(test_images)
test_dataset = tf.data.Dataset.from_tensor_slices((test_images, test_label))


print(train_data)
print(test_dataset)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input([28,28,1]),
    tf.keras.layers.Conv2D(100,2,padding='same'),
    # tf.keras.layers.Conv2D(100,2,padding='same'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(100,2,padding='same'),
    # tf.keras.layers.Conv2D(100,2,padding='same'),
    tf.keras.layers.GlobalMaxPooling2D(),
    tf.keras.layers.Dense(100,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Input([28,28,1]),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(100,activation='relu'),
#     tf.keras.layers.Dense(100,activation='relu'),
#     tf.keras.layers.Dense(10,activation='softmax')
# ])


print(f"train_data len = {len(train_data)}")
print(f"test_data len = {len(test_images)}")

print(f"train_data = {train_data}")
print(f"test_data = {test_images.shape}")


model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model.summary())
model.fit(train_data,epochs=5,validation_data = test_dataset)
model.save('mymodel.keras')
