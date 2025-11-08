import pandas as pd
data=pd.read_csv("/home/harisanker/Downloads/movies.csv",header=None,sep=",")
data.columns=["id","movie_name","year","rating","duration"]

# 14) a. 1975 - 2000 and rating above 3.5 count
#     b. row count

# 14.a)
data1=data.loc[(data["year"]>1975) & (data["year"]<2000) & (data["rating"]>3.5)]
print(data1)

print("*"*100)

# 14.b)
print(len(data1))




