import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import imageio

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(type(x_test))

print(x_test.shape)
print(y_test.shape)

x_train = x_train / 255
x_test = x_test / 255

plt.figure(figsize=(8, 8))
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.colorbar()
    plt.xlabel(y_train[i])
plt.show()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
	tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
    optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(x_train, y_train, epochs=10)

print(model.evaluate(x_test, y_test))

def model_answer(model, filename, display=True):
  image = imageio.imread(filename)
  image = np.mean(image, 2, dtype=float)
  image = image / 255
  if display:
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap=plt.cm.binary)
    plt.xlabel(filename)
    plt.show()
  image = np.expand_dims(image, 0)
  return np.argmax(model.predict(image))

for i in range(10):
  filename = f'{i}.png'
  print('Имя файла: ', filename, '\tОтвет сети: ', model_answer(model, filename, False))
print(model_answer(model, '2.png'))