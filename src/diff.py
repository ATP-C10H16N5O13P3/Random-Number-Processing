import multiprocessing
import os
import time
import pandas as pd
import numpy as np

start = time.perf_counter()

df_P = pd.read_csv("../Pdata/count.csv")
df_T = pd.read_csv("../Tdata/count.csv")

# print(df_P)
# print(df_T)

countP = df_P.drop(columns=["file_num"])
countT = df_T.drop(columns=["file_num"])

arr_P = countP.to_numpy()
arr_T = countT.to_numpy()

sqrt_diff = False
if sqrt_diff == True:
    diffP = (arr_P - 1000) ** 2
    diffT = (arr_T - 1000) ** 2
else:
    diffP = np.abs(arr_P - 1000)
    diffT = np.abs(arr_T - 1000)

# print(diffP)
# print(diffT)

with open("../Pdata/diff.csv", "w") as f:
    f.write("file_num,1,2,3,4,5,6,7,8,9,10\n") # csv header
    for idx, i in enumerate(diffP):
        f.write(f"{idx},{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]}")

with open("../Tdata/diff.csv", "w") as f:
    f.write("file_num,1,2,3,4,5,6,7,8,9,10\n") # csv header
    for idx, i in enumerate(diffT):
        f.write(f"{idx},{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]}")

end = time.perf_counter()

print(f"Total Time: {end-start:.6f}")