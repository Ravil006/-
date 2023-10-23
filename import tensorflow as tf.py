import tensorflow as tf
from keras.datasets import mnist
(x_train, y_train),(x_test, y_test)=tf.keras.datasets.mnist.load_data()
x_train, x_test=x_train / 255.0, x_test/255.0
model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10)
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=2)
print (f'Точность на тестовых данных:{test_acc}')