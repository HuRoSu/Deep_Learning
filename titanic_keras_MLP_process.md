`import numpy`<br>
`import pandas as pd`<br>
`from sklearn import preprocessing`<br>
`numpy.random.seed(10)`<br>
`all_df = pd.read_excel("data/titanic3.xls")`<br>
`cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']`<br>
`all_df=all_df[cols]`<br>
`msk = numpy.random.rand(len(all_df)) < 0.8 #8:2 to msk`<br>
`train_df = all_df[msk] #train 80%`<br>
`test_df = all_df[~msk] #test 20%`<br>
<br>
`print('total:',len(all_df),`<br>
`      'train:',len(train_df),`<br>
`      'test:',len(test_df))`<br>
Out:<br>
total: 1309 train: 1034 test: 275<br>
<br>
<br>
`train_Features,train_Label=PreprocessData(train_df)`<br>
`test_Features,test_Label=PreprocessData(test_df)`<br>
`from keras.models import Sequential`<br>
`from keras.layers import Dense,Dropout`<br>
<br>
if`from keras.models import Sequential`<br>
`from keras.layers import Dense,Dropout`error dump<br>
`h5py\_init_.py:26：FutureWarning: Conversion of the second argument of issubdtype from 'float' to 'np.floating' is deprecated. `<br>
`In future, it will be treated as 'np.float64 == np.dtype(float).type.'` <br>
`  from ._conv import register_converters as _register_converters`<br>
<br>
Solution is pip install h5py==2.8.0rc1
<br>
<br>
`model=Sequential() #add model`<br>
`model.add(Dense(units=40,input_dim=9,`<br>
`                kernel_initializer='uniform',`<br>
`                activation='relu'))`<br>
`#add Dense ,Dense is connect upper layer and lower layer`<br>
`#40 is Hidden layer1 quantity ;9 is Input Layer quantity`<br>
`#kernel use uniform distribution ,initializer weight and bias`<br>
`#activation definition 'relu'`<br>
`model.add(Dense(units=30,`<br>
`                kernel_initializer='uniform',`<br>
`                activation='relu'))`<br>
`#Hidden layer2`<br>
`model.add(Dense(units=1,`<br>
`                kernel_initializer='uniform',`<br>
`                activation='sigmoid'))`<br>
`#Output layer`<br>
<br>
`model.compile(loss='binary_crossentropy',`<br>
`              optimizer='adam',metrics=['accuracy'])`<br>
`#loss function is cross_entropy`<br>
`#optimization set adam`<br>
`#assess use accuracy`<br>
<br>
`train_history=model.fit(x=train_Features,`<br>
`                        y=train_Label,`<br>
`                        validation_split=0.1,`<br>
`                        epochs=30,`<br>
`                        batch_size=30,verbose=2)`<br>
`#use model.fit training`<br>
`#x = features, features = 9, input_dim=9`<br>
`#y = Label can survive?`<br>
`#set validation_split=0.1 90% train and 10% check`<br>
`#train*0.9=train train*0.1=check`<br>
`#train 30times`<br>
`#each batch 30quantity`<br>
`#ex:930train to training, 30times, one time 30quantity, ~=31times can finish`<br>
`#verbose=2 is display training process`<br>
Out:<br>
Train on 930 samples, validate on 104 samples<br>
Epoch 1/30<br>
  1s - loss: 0.6899 - accuracy: 0.5774 - val_loss: 0.6707 - val_accuracy: 0.7885<br>
Epoch 2/30<br>
  0s - loss: 0.6679 - accuracy: 0.5957 - val_loss: 0.5919 - val_accuracy: 0.7885<br>
 ......<br>
 Epoch 29/30<br>
  0s - loss: 0.4455 - accuracy: 0.7946 - val_loss: 0.4165 - val_accuracy: 0.8173<br>
Epoch 30/30<br>
  0s - loss: 0.4522 - accuracy: 0.7914 - val_loss: 0.4162 - val_accuracy: 0.8173<br>

#Check  
scores = model.evaluate(x=test_Features,  
                       y=test_Label)  
Out:  
275/275 [==============================] - 0s 18us/step  
scores[1]  
Out:  
0.807272732257843  
