import multiprocessing
import os
import time
import pandas as pd
import numpy as np
from combination import combination

start = time.perf_counter()

# load data frame
df_P = pd.read_csv("../Pdata/diff.csv")
df_T = pd.read_csv("../Tdata/diff.csv")

# drop file number
diffP = df_P.drop(columns=["file_num"])
diffT = df_T.drop(columns=["file_num"])

# data frame into numpy array
arr_P = diffP.to_numpy()
arr_T = diffT.to_numpy()

# find total difference in each file
Ptotal_arr = np.array([np.sum(arr_P[i]) for i in range(len(arr_P))])
Ttotal_arr = np.array([np.sum(arr_T[i]) for i in range(len(arr_T))])

# print(Ptotal_arr)
# print(Ttotal_arr)

# amplifying the total difference by grouping each total in 10 groups with 5 blocks (each 20)
''' e.g. (file number)
0,1,2,3,4,5,6,7,8,9
0,1,2,3,4,5,6,7,8,10
0,1,2,3,4,5,6,7,8,11
0,1,2,3,4,5,6,7,8,12
...
40,41,43,47,49,50,51,55,57,59
40,41,43,47,49,50,51,55,58,59
40,41,43,47,49,50,51,56,57,58
40,41,43,47,49,50,51,56,57,59
40,41,43,47,49,50,51,56,58,59
40,41,43,47,49,50,51,57,58,59
... '''

# run function of the the groups (combination) from combination.py
# combination(20,10)

# read groups from combinations into array
with open("AllCombinations.csv", "r") as f:
    combination = f.read().splitlines()
    for i in range(len(combination)):
        combination[i] = combination[i].split(",")
        del combination[i][-1]
    print(combination[0])

# continue

end = time.perf_counter()

print(f"Total Time: {end-start:.6f}")