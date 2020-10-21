import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir("/media/sf_Projects/Machine Learning/dogs-vs-cats")
print(os.getcwd())

# if os.path.isdir('train/dog') is False:
#     os.makedirs('train/dog')
#     os.makedirs('train/cat')
#     os.makedirs('valid/dog')
#     os.makedirs('valid/cat')
#     os.makedirs('test/dog')
#     os.makedirs('test/cat')

# for f in random.sample(glob.glob('dog*'), 500):
#     shutil.move(f, 'train/dog')
# for f in random.sample(glob.glob('cat*'), 500):
#     shutil.move(f, 'train/cat')
# for f in random.sample(glob.glob('dog*'), 100):
#     shutil.move(f, 'valid/dog')
# for f in random.sample(glob.glob('cat*'), 100):
#     shutil.move(f, 'valid/cat')
# for f in random.sample(glob.glob('dog*'), 50):
#     shutil.move(f, 'test/dog')
# for f in random.sample(glob.glob('cat*'), 50):
#     shutil.move(f, 'test/cat')

# path, dirs, files = next(os.walk("/media/sf_Projects/Machine Learning/train"))
# print('\n', path, '\n', dirs, '\n', 'number of files: ', len(files))

os.chdir('../')

print(os.getcwd())

train_path = 'dogs-vs-cats/train'
valid_path = 'dogs-vs-cats/valid'
test_path = 'dogs-vs-cats/test'

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=train_path, target_size=(224, 224), classes=['cat', 'dog'], batch_size=5)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=valid_path, target_size=(224, 224), classes=['cat', 'dog'], batch_size=5)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=test_path, target_size=(224, 224), classes=['cat', 'dog'], batch_size=5,
                         shuffle=False)

assert train_batches.n == 1000
assert valid_batches.n == 200
assert test_batches.n == 100
assert train_batches.num_classes == valid_batches.num_classes == test_batches.num_classes == 2

imgs, labels = next(train_batches)

print(imgs.shape)




plotImages(imgs)
print(labels)

model = Sequential([Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)),
                   MaxPool2D(pool_size=(2, 2), strides=2),
                   Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'),
                   MaxPool2D(pool_size=(2, 2), strides=2),
                   Flatten(),
                   Dense(units=2, activation='softmax')])

print(model.summary())

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x=train_batches,
          steps_per_epoch=len(train_batches),
          validation_data=valid_batches,
          validation_steps=len(valid_batches),
          epochs=10,
          verbose=2
          )


def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

test_imgs, test_labels = next(test_batches)
plotImages(test_imgs)
print(test_labels)

predictions = model.predict(x=test_batches, steps=len(test_batches), verbose=0)

print(np.round(predictions))

print(test_batches.classes)
print(test_batches.class_indices)

cm = confusion_matrix(y_true=test_batches.classes, y_pred=np.argmax(predictions, axis=-1))

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

cm_plot_labels = ['cat', 'dog']
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')
plt.show()

# build fine-tuned VGG16 model

vgg16_model = tf.keras.applications.vgg16.VGG16()
print(vgg16_model.summary())
print(type(vgg16_model))

model = Sequential()
for layer in vgg16_model.layers[:-1]:
    model.add(layer)

for layer in model.layers:
    layer.trainable = False

model.add(Dense(units=2, activation='softmax'))

print(model.summary())