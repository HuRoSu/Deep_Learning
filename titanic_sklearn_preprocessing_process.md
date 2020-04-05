`from sklearn import preprocessing`<br>
`minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1)) #preprocessing.MinMaxScalerSet is preprocessing Min and Max`<br>
`#feature range between 0 and 1`<br>
`scaledFeatures=minmax_scale.fit_transform(Features) #import Features to minmax_scale.fit_transform to preprocessing`<br>
`scaledFeatures[:]`<br>
Out:<br>
array([[0.        , 0.        , 0.36116884, ..., 0.        , 0.        ,<br>
        1.        ],<br>
       [0.        , 1.        , 0.00939458, ..., 0.        , 0.        ,<br>
        1.        ],<br>
       [0.        , 0.        , 0.0229641 , ..., 0.        , 0.        ,<br>
        1.        ],<br>
       ...,<br>
       [1.        , 1.        , 0.32985358, ..., 1.        , 0.        ,<br>
        0.        ],<br>
       [1.        , 1.        , 0.33611663, ..., 1.        , 0.        ,<br>
        0.        ],<br>
       [1.        , 1.        , 0.36116884, ..., 0.        , 0.        ,<br>
        1.        ]])<br>
<br>
<br>
`scaledFeatures[:2]`<br>
Out:<br>
array([[0.        , 0.        , 0.36116884, 0.        , 0.        ,<br>
        0.41250333, 0.        , 0.        , 1.        ],<br>
       [0.        , 1.        , 0.00939458, 0.125     , 0.22222222,<br>
        0.2958059 , 0.        , 0.        , 1.        ]])<br>
<br>
<br>
`msk = numpy.random.rand(len(all_df)) < 0.8 #8:2 to msk`<br>
`train_df = all_df[msk] #train 80%`<br>
`test_df = all_df[~msk] #test 20%`<br>
`print('total:',len(all_df),`<br>
`      'train:',len(train_df),`<br>
`      'test:',len(test_df))`<br>
Out:<br>
total: 1309 train: 1059 test: 250 #random<br>
<br>
<br>
`def PreprocessData(raw_df):`<br>
`    df=raw_df.drop(['name'], axis=1)`<br>
`    age_mean = df['age'].mean()`<br>
`    df['age'] = df['age'].fillna(age_mean)`<br>
`    fare_mean = df['fare'].mean()`<br>
`    df['fare'] = df['fare'].fillna(fare_mean)`<br>
`    df['sex']= df['sex'].map({'female':0, 'male': 1}).astype(int)`<br>
`    x_OneHot_df = pd.get_dummies(data=df,columns=["embarked" ])`<br>
<br>
`    ndarray = x_OneHot_df.values`<br>
`    Features = ndarray[:,1:]`<br>
`    Label = ndarray[:,0]`<br>
<br>
`    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))`<br>
`    scaledFeatures=minmax_scale.fit_transform(Features)    `<br>
    <br>
`    return scaledFeatures,Label`<br>
<br>
`train_Features,train_Label=PreprocessData(train_df)`<br>
`test_Features,test_Label=PreprocessData(test_df)`<br>
<br>
`train_Features[:]`<br>
Out:<br>
array([[0.        , 1.        , 0.00939458, ..., 0.        , 0.        ,<br>
        1.        ],<br>
       [0.        , 1.        , 0.37369494, ..., 0.        , 0.        ,<br>
        1.        ],<br>
       [0.        , 0.        , 0.31106443, ..., 0.        , 0.        ,<br>
        1.        ],<br>
       ...,<br>
       [1.        , 0.        , 0.36845843, ..., 1.        , 0.        ,<br>
        0.        ],<br>
       [1.        , 1.        , 0.32985358, ..., 1.        , 0.        ,<br>
        0.        ],<br>
       [1.        , 1.        , 0.33611663, ..., 1.        , 0.        ,<br>
        0.        ]])<br>
<br>
<br>
`train_Features[:2]`<br>
Out:<br>
array([[0.        , 1.        , 0.00939458, 0.125     , 0.22222222,<br>
        0.2958059 , 0.        , 0.        , 1.        ],<br>
       [0.        , 1.        , 0.37369494, 0.125     , 0.22222222,<br>
        0.2958059 , 0.        , 0.        , 1.        ]])<br>
<br>
<br>
`train_Label[:]`<br>
Out:<br>
array([1., 0., 0., ..., 0., 0., 0.])<br>
<br>
<br>
`train_Label[:2]`<br>
Out:<br>
array([1., 0.])<br>

