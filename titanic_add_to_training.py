Jack = pd.Series([0, 'Jack', 3, 'male', 23, 1, 0, 5.0000, 'S']) #pandas series add Jack
Rose = pd.Series([1, 'Rose', 1, 'female', 20, 1, 0, 100.0000, 'S'])  
JR_df = pd.DataFrame([list(Jack), list(Rose)], 
                     columns=['survived','name', 'pclass','sex',
                              'age','sibsp','parch','fare','embarked'])  
#add Jack Rose to DataFrame list

all_df=pd.concat([all_df,JR_df]) #JR add to all
all_Features,Label=PreprocessData(all_df) #all_df give PreprocessData def to one more Preprocess ,and to all_Featurers
all_probability=model.predict(all_Features) #start predict

pd=all_df
pd.insert(len(all_df.columns),
         'probability',all_probability) #add Jack and Rose insert pd
         #insert(loc,column,value)
         #insert(loc is where we want to insert new column(len is add to final column),
         #add 'probability' this name to columns,add all_probability to value(inside))

'''
pd[-2:]
'''




