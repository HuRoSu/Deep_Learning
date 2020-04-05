`import numpy`<br>
`import pandas as pd`<br>
`filepath="data/titanic3.xls"`<br>
`all_df=pd.read_excel(filepath)`<br>
`all_df[:]`<br>
Out:<br>
	pclass	survived	name	sex	age	sibsp	parch	ticket	fare	cabin	embarked	boat	body	home.dest<br>
0	1	1	Allen, Miss. Elisabeth Walton	female	29.0000	0	0	24160	211.3375	B5	S	2	NaN	St Louis, MO<br>
1	1	1	Allison, Master. Hudson Trevor	male	0.9167	1	2	113781	151.5500	C22 C26	S	11	NaN	Montreal, PQ / Chesterville, ON<br>
2	1	0	Allison, Miss. Helen Loraine	female	2.0000	1	2	113781	151.5500	C22 C26	S	NaN	NaN	Montreal, PQ / Chesterville, ON<br>
3	1	0	Allison, Mr. Hudson Joshua Creighton	male	30.0000	1	2	113781	151.5500	C22 C26	S	NaN	135.0	Montreal, PQ / Chesterville, ON<br>
......<br>
1309 rows × 14 columns<br>
<br>
<br>
`cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']`<br>
`all_df=all_df[cols]`<br>
`all_df[:]`<br>
Out:<br>
	survived	name	pclass	sex	age	sibsp	parch	fare	embarked<br>
0	1	Allen, Miss. Elisabeth Walton	1	female	29.0000	0	0	211.3375	S<br>
1	1	Allison, Master. Hudson Trevor	1	male	0.9167	1	2	151.5500	S<br>
2	0	Allison, Miss. Helen Loraine	1	female	2.0000	1	2	151.5500	S<br>
......<br>
1309 rows × 9 columns<br>
<br>
<br>
`df = all_df.drop(['name'],axis=1)`<br>
`all_df.isnull().sum()`<br>
Out:<br>
pclass          0<br>
survived        0<br>
name            0<br>
sex             0<br>
age           263<br>
sibsp           0<br>
parch           0<br>
ticket          0<br>
fare            1<br>
cabin        1014<br>
embarked        2<br>
boat          823<br>
body         1188<br>
home.dest     564<br>
dtype: int64<br>
<br>
<br>
`age_mean=df['age'].mean()`<br>
`df['age']=df['age'].fillna(age_mean)`<br>
`age_mean=df['fare'].mean()`<br>
`df['fare']=df['fare'].fillna(age_mean)`<br>
`df[:]`<br>
Out:<br>
	survived	pclass	sex	age	sibsp	parch	fare	embarked<br>
0	1	1	female	29.000000	0	0	211.3375	S<br>
1	1	1	male	0.916700	1	2	151.5500	S<br>
2	0	1	female	2.000000	1	2	151.5500	S<br>
......<br>
1309 rows × 8 columns<br>
<br>
<br>
`print(df['age'].mean())`<br>
`print(df['fare'].mean())`<br>
Out:<br>
29.881134512428055<br>
33.29547928134572<br>
<br>
<br>
`df['sex']=df['sex'].map({'female':0,'male':1}).astype(int)`<br>
`df[:]`<br>
Out:<br>
	survived	pclass	sex	age	sibsp	parch	fare	embarked<br>
0	1	1	0	29.000000	0	0	211.3375	S<br>
1	1	1	1	0.916700	1	2	151.5500	S<br>
2	0	1	0	2.000000	1	2	151.5500	S<br>
......<br>
1309 rows × 8 columns<br>
<br>
<br>
`x_OneHot_df=pd.get_dummies(data=df,columns=["embarked"])`<br>
`x_OneHot_df[:]`<br>
Out:<br>
	survived	pclass	sex	age	sibsp	parch	fare	embarked_C	embarked_Q	embarked_S<br>
0	1	1	0	29.000000	0	0	211.3375	0	0	1<br>
1	1	1	1	0.916700	1	2	151.5500	0	0	1<br>
2	0	1	0	2.000000	1	2	151.5500	0	0	1<br>
......<br>
1309 rows × 10 columns<br>
<br>
<br>
`ndarray=x_OneHot_df.values`<br>
`ndarray.shape`<br>
Out:<br>
(1309, 10)<br>
<br>
<br>
`Label=ndarray[:0]`<br>
`Features=ndarray[:,1:]`<br>
`Label[:]`<br>
Out:<br>
array([], shape=(0, 10), dtype=float64)<br>
<br>
<br>
`Features[:]`<br>
Out:<br>
array([[ 1.    ,  0.    , 29.    , ...,  0.    ,  0.    ,  1.    ],<br>
       [ 1.    ,  1.    ,  0.9167, ...,  0.    ,  0.    ,  1.    ],<br>
       [ 1.    ,  0.    ,  2.    , ...,  0.    ,  0.    ,  1.    ],<br>
       ...,<br>
       [ 3.    ,  1.    , 26.5   , ...,  1.    ,  0.    ,  0.    ],<br>
       [ 3.    ,  1.    , 27.    , ...,  1.    ,  0.    ,  0.    ],<br>
       [ 3.    ,  1.    , 29.    , ...,  0.    ,  0.    ,  1.    ]])<br>





