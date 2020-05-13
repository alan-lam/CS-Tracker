import os, cv2, random, re
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

NUM_IMAGES = 350
TRAINING_DATA_DIR = os.path.join('CS Numbers', 'Training')
TESTING_DATA_DIR = os.path.join('CS Numbers', 'Testing')
DATA_DIR = os.path.join('CS Numbers', 'Data')
CATEGORIES = [str(i) for i in range(NUM_IMAGES)]
IMG_WIDTH = 38
IMG_HEIGHT = 21
BATCH_SIZE = 20
EPOCHS = 20

def createTrainingData():
    for category in CATEGORIES:
        path = os.path.join(TRAINING_DATA_DIR, category)
        for img_file in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img_file))
            training_data.append([img_array, category])

def testModel():
    for i in range(20):
        randomNumber = random.randrange(NUM_IMAGES)
        print(f'Testing {randomNumber}.png')
        img = cv2.imread(os.path.join(TESTING_DATA_DIR, f'{randomNumber}.png'))
        img_array = img.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)
        prediction = model.predict(img_array)
        prediction = list(prediction[0])
        print(f'Prediction: {CATEGORIES[prediction.index(max(prediction))]}')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def evaluateResults():
    p = re.compile('\d+')
    for img_file in os.listdir(DATA_DIR):
        mins = p.match(img_file).group()
        img_array = cv2.imread(os.path.join(DATA_DIR, img_file)).reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)
        cs = model.predict(img_array)
        cs = list(cs[0])
        cs = CATEGORIES[cs.index(max(cs))]
        csPer5.append((cs,mins))

training_data = []
createTrainingData()

X = []
y = []
for features, label in training_data:
    X.append(features)
    y.append(int(label))
X = np.array(X).reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)
y = np.asarray(y)

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=X.shape[1:]),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(NUM_IMAGES)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

print('Training model...')
history = model.fit(X, y, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=False)
print(f'Accuracy: {history.history["accuracy"][-1]}')
testModel()
print('Evaluating results...')
csPer5 = []
evaluateResults()
print(csPer5)
