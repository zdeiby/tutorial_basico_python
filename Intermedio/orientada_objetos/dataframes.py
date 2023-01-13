#instalar antes pip install pandas

import pandas as pd

data={"x": [1,2,3,4,5],
      "y":[2,4,6,8,10]}
df1 = pd.DataFrame(data=data)
print(df1)

df2 = pd.DataFrame(data= [[1,2], [2,4],[3,6],[4,8],[5,10]],
                   columns=["x","y"])
print(df2)

df3=pd.DataFrame(data = data, index=["obs1","obs2","obs3","obs4","obs5"])
print(df3)

#creando dataframes a partir de una lista de diccionarios
data=[{"x":1, "y":2,"z":2},
      {"x":2, "y":4,"z":2},
      {"x":3, "y":6,"z":2},
      {"x":4, "y":8,"z":2},
      {"x":5, "y":10,"z":2}]
df4= pd.DataFrame(data= data)
print(df4)

x=[1,2,3,4,5]
y=[2,4,6,8,10]

data=list(zip(x,y))
print(data)

df5=pd.DataFrame(data, columns=["x","y"],index=["obs1","obs2","obs3","obs4","obs5"])
print(df5)

#dataframe from diccionario 

data={"x": [1,2,3,4,5],
      "y":[2,4,6,8,10]}

df5=pd.DataFrame.from_dict(data)
print(df5)

df6=pd.DataFrame.from_dict(data, orient="index", columns = ["a","b","c","d","e"])
print(df6)