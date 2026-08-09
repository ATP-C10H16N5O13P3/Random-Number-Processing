from collections import Counter
import multiprocessing
import os
import time
import pandas as pd

df_P = pd.read_csv("Pdata/count.csv")
df_T = pd.read_csv("Tdata/count.csv")

print(df_P)
print(df_T)