import pandas as pd 

data = [[1,2,3,4], [5,6,7,8]]

dataframe = pd.DataFrame(data)

dataframe.to_csv("./ch01/pandas-save.csv", header=False, index=False)