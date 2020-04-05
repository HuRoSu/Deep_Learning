def PreprocessData(raw_df):
    df=raw_df.drop(['name'], axis=1)
    age_mean = df['age'].mean()
    df['age'] = df['age'].fillna(age_mean)
    fare_mean = df['fare'].mean()
    df['fare'] = df['fare'].fillna(fare_mean)
    df['sex']= df['sex'].map({'female':0, 'male': 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df,columns=["embarked" ])
    ndarray = x_OneHot_df.values
    Features = ndarray[:,1:]
    Label = ndarray[:,0]
    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures=minmax_scale.fit_transform(Features)    
    
    return scaledFeatures,Label

import numpy
import pandas as pd
from sklearn import preprocessing
numpy.random.seed(10)
all_df = pd.read_excel("data/titanic3.xls")
cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']
all_df=all_df[cols]
msk = numpy.random.rand(len(all_df)) < 0.8 #8:2 to msk
train_df = all_df[msk] #train 80%
test_df = all_df[~msk] #test 20%

train_Features,train_Label=PreprocessData(train_df)
test_Features,test_Label=PreprocessData(test_df)

from keras.models import Sequential
from keras.layers import Dense,Dropout

model=Sequential() #add model
model.add(Dense(units=40,input_dim=9,
                kernel_initializer='uniform',
                activation='relu'))
#add Dense ,Dense is connect upper layer and lower layer
#40 is Hidden layer1 quantity ;9 is Input Layer quantity
#kernel use uniform distribution ,initializer weight and bias
#activation definition 'relu'
model.add(Dense(units=30,
                kernel_initializer='uniform',
                activation='relu'))
#Hidden layer2
model.add(Dense(units=1,
                kernel_initializer='uniform',
                activation='sigmoid'))
#Output layer

model.compile(loss='binary_crossentropy',
              optimizer='adam',metrics=['accuracy'])
#loss function is cross_entropy
#optimization set adam
#assess use accuracy

train_history=model.fit(x=train_Features,
                        y=train_Label,
                        validation_split=0.1,
                        epochs=30,
                        batch_size=30,verbose=2)
#use model.fit training
#x = features, features = 9, input_dim=9
#y = Label can survive?
#set validation_split=0.1 90% train and 10% check
#train*0.9=train train*0.1=check
#train 30times
#each batch 30quantity
#ex:930train to training, 30times, one time 30quantity, ~=31times can finish
#verbose=2 is display training process

'''
import matplotlib.pyplot as plt
def show_train_history(Train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel('train')
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='center right')
    plt.show()

show_train_history(train_history,'accuracy','val_accuracy')
show_train_history(train_history,'loss','val_loss')
'''

'''
scores = model.evaluate(x=test_Features,
                       y=test_Label)
scores[1]
#check this model accuracy
#!not final accuracy
'''
