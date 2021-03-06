# -*- coding: utf-8 -*-
"""Fashion Mnist

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WVrJJdVzlUkVf89ZLkieLggyWBK5PI-4
"""

#Load the Mnist DataSet model 
import keras
mnist=keras.datasets.fashion_mnist 
(x_train,y_train),(x_test,y_test)=mnist.load_data()

# Print the number of samples in x_train, x_test, y_train, y_test
print("Initial shape or dimensions of x_train", str(x_train.shape))
print ("Number of samples in our training data: " + str(len(x_train)))
print ("Number of labels in our training data: " + str(len(y_train)))
print ("Number of samples in our test data: " + str(len(x_test)))
print ("Number of labels in our test data: " + str(len(y_test)))
print()
print ("Dimensions of x_train:" + str(x_train[0].shape))
print ("Labels in x_train:" + str(y_train.shape))
print()
print ("Dimensions of x_test:" + str(x_test[0].shape))
print ("Labels in y_test:" + str(y_test.shape))

#Import the required Libraries for the model
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization

# Training Parameters
batch_size = 128
epochs = 3

# Lets store the number of rows and columns
img_rows = x_train[0].shape[0]
img_cols = x_train[1].shape[0]

# Getting our date in the right 'shape' needed for Keras
# We need to add a 4th dimenion to our date thereby changing our
# Our original image shape of (60000,28,28) to (60000,28,28,1)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# store the shape of a single image 
input_shape = (img_rows, img_cols, 1)

# change our image type to float32 data type
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalize our data by changing the range from (0 to 255) to (0 to 1)
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Now we one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# Let's count the number columns in our hot encoded matrix 
print ("Number of Classes: " + str(y_test.shape[1]))

num_classes = y_test.shape[1]
num_pixels = x_train.shape[1] * x_train.shape[2]

#Create model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())

model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss = 'categorical_crossentropy',
              optimizer = keras.optimizers.Adadelta(),
              metrics = ['accuracy'])

print(model.summary())

#Train the model
history = model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
mod =model.layers
print('Test loss:', score[0])
print('Test accuracy:', score[1])
print('Test Mod:',mod)

#Send mail 
if score[1]>.90:
  print ("Sending mail...") 
  import smtplib 
  #Creates SMTP session
  s=smtplib.SMTP ('smtp.gmail.com',587) 
  #Start TLS for security 
  s.starttls()
  #Authentication
  s.login ("chelsimundra@gmail.com", "tsfntqogxagexgse") 
  #Message to be sent
  messagel=str(score[1])
  message2=str(mod)
  #Send the mail 
  s.sendmail("chelsimundra@gmail.com","chelsimundra@gmail.com",messagel)
  s.sendmail("chelsimundra@gmail.com","chelsimundra@gmail.com",message2)
  #Terminate the session 
  s. quit () 
  print ("Mail sent.")

