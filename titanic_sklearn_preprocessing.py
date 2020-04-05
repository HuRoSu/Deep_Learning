import numpy
import pandas as pd
filepath="data/titanic3.xls"
all_df = pd.read_excel(filepath)
cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']
all_df=all_df[cols]
df = all_df.drop(['name'],axis=1)
age_mean = df['age'].mean() #average null age
df['age'] = df['age'].fillna(age_mean) #fill the null
fare_mean = df['fare'].mean() #average null fare
df['fare'] = df['fare'].fillna(fare_mean) #fill the null
df['sex'] = df['sex'].map({'female':0,'male':1}).astype(int)
x_OneHot_df = pd.get_dummies(data=df,columns=["embarked"]) #embarked classification convert
ndarray = x_OneHot_df.values #dataframe convert array
Label=ndarray[:0] #:=all 0=number 0 data field
Features=ndarray[:,1:] #:=all 1:=number 1 data field to the last

#preprocessing

from sklearn import preprocessing
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1)) #preprocessing.MinMaxScalerSet is preprocessing Min and Max
#feature range between 0 and 1
scaledFeatures=minmax_scale.fit_transform(Features) #import Features to minmax_scale.fit_transform to preprocessing
msk = numpy.random.rand(len(all_df)) < 0.8 #8:2 to msk
train_df = all_df[msk] #train 80%
test_df = all_df[~msk] #test 20%


'''
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
'''

