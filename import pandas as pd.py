import pandas as pd
import numpy as np 
import random

df_1 = pd.read_csv('danhsach.csv')
list1 = []
list2 = []
for i in range(len(df_1)):
    a = df_1.iloc[i]
    list1.append(a)
a = random.sample(list1,7)
for i in a:
    list2.append(i)
#print(len(list2))
df_2 = pd.DataFrame(list2)
df_2.reset_index(drop = True, inplace = True)
df_2.to_csv("baitap.csv")
print(df_2)

