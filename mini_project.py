import numpy as np

import pandas as pd
import matplotlib.pyplot as plt


#Numpy

 # arr = np.array([12, 35, 5,6, 7, 8, 56])
# print(arr)

# print(arr[0])
#print(arr[-1])
#print(arr[1:3])

#print(arr.min())
#print(arr.mean())


#Pandas - data frame

data ={
    "ID" : [1, 2, 3],
    "Name":["Ram", "Hari", "Shyam"],
    "Age": [13, 14, 15]
}

df = pd.DataFrame(data)
print(df)

data1= pd.read_csv('students.csv')
df1 = pd.DataFrame(data1)
print(df1)

print(df1.info())