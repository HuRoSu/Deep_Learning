`Jack = pd.Series([0, 'Jack', 3, 'male', 23, 1, 0, 5.0000, 'S'])`    
`Rose = pd.Series([1, 'Rose', 1, 'female', 20, 1, 0, 100.0000, 'S'])  `  
`JR_df = pd.DataFrame([list(Jack), list(Rose)], `  
　　　　　　　　　　　　`columns=['survived','name', 'pclass','sex',`  
　　　　　　　　　　　　　　　　　`'age','sibsp','parch','fare','embarked'])  `  

`all_df=pd.concat([all_df,JR_df])`  
`all_df[:]`  
Out:  
	survived	name	pclass	sex	age	sibsp	parch	fare	embarked  
0	1	Allen, Miss. Elisabeth Walton	1	female	29.0000	0	0	211.3375	S  
1	1	Allison, Master. Hudson Trevor	1	male	0.9167	1	2	151.5500	S  
2	0	Allison, Miss. Helen Loraine	1	female	2.0000	1	2	151.5500	S  
3	0	Allison, Mr. Hudson Joshua Creighton	1	male	30.0000	1	2	151.5500	S  
......  
0	0	Jack	3	male	23.0000	1	0	5.0000	S  
1	1	Rose	1	female	20.0000	1	0	100.0000	S  
1311 rows × 9 columns  
  
  
`all_Features,Label=PreprocessData(all_df)`  
`all_probability=model.predict(all_Features)`  
`all_probability[:]`  
Out:  
array([[0.97713214],  
       [0.60914594],  
       [0.97245204],  
       ...,  
       [0.14470536],  
       [0.15035556],  
       [0.96961963]], dtype=float32)  
  
  
`pd=all_df`  
`pd.insert(len(all_df.columns),`  
　　　　　`'probability',all_probability)`  
`pd[:]`  
Out:  
	survived	name	pclass	sex	age	sibsp	parch	fare	embarked	probability  
0	1	Allen, Miss. Elisabeth Walton	1	female	29.0000	0	0	211.3375	S	0.977132  
1	1	Allison, Master. Hudson Trevor	1	male	0.9167	1	2	151.5500	S	0.609146  
2	0	Allison, Miss. Helen Loraine	1	female	2.0000	1	2	151.5500	S	0.972452  
......  
0	0	Jack	3	male	23.0000	1	0	5.0000	S	0.150356  
1	1	Rose	1	female	20.0000	1	0	100.0000	S	0.969620  
1311 rows × 10 columns  


