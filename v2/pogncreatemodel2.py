import pandas as pd 
import keras
from keras.models import load_model
import sklearn.model_selection
import numpy as np



#df = pd.read_csv("pongdata.csv")
df = pd.read_csv("pongdata2.csv")

input_data = np.array(df.drop(["currentaction"],1))
output_data = np.array(df["currentaction"])

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(input_data,output_data,test_size=0.2)



print(x_train.shape)


model = keras.Sequential([
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(256,activation='relu'),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(64,activation='relu'),
    keras.layers.Dense(2,activation='softmax')
])


model.compile(optimizer = 'adam',loss = 'sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=24)


test_loss, test_acc = model.evaluate(x_test,y_test)


print("Accuracy:",str(test_acc*100))

#model.save("pongmodel.h5")
model.save("pongmodel2.h5")