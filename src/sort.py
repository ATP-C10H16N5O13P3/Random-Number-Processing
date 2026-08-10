import time
import numpy as np
from collections import Counter

start = time.perf_counter()

with open("../Pdata/amp_diff.csv", "r") as f:
    Pdiff_amp = f.read().splitlines()

with open("../Tdata/amp_diff.csv", "r") as f:
    Tdiff_amp = f.read().splitlines()

# count each occurance of that differences and turn it into numpy array
count_Pdiff = np.array(list(Counter(Pdiff_amp).items()))
count_Tdiff = np.array(list(Counter(Tdiff_amp).items()))

# convert to int
count_Pdiff = count_Pdiff.astype(int)
count_Tdiff = count_Tdiff.astype(int)

import numpy as np

def quicksort_2d(arr):
    # Base case: 0 or 1 rows are already sorted
    if arr.shape[0] <= 1:
        return arr
    
    # Choose the middle row as pivot
    pivot = arr[arr.shape[0] // 2]
    pivot_val = pivot[0] # Sort baseline
    
    # Partition rows based on the first element
    left = np.array([row for row in arr if row[0] < pivot_val])
    middle = np.array([row for row in arr if row[0] == pivot_val])
    right = np.array([row for row in arr if row[0] > pivot_val])
    
    # Reconstruct empty arrays correctly to allow concatenation
    left = left if left.size else np.empty((0, arr.shape[1]))
    right = right if right.size else np.empty((0, arr.shape[1]))
    
    # Recursively sort and combine
    return np.vstack((quicksort_2d(left), middle, quicksort_2d(right)))

sorted_count_Pdiff = quicksort_2d(count_Pdiff).astype(int)
sorted_count_Tdiff = quicksort_2d(count_Tdiff).astype(int)

np.savetxt('../Pdata/sorted_diff.csv', sorted_count_Pdiff, delimiter=',',fmt='%.0f')
np.savetxt('../Tdata/sorted_diff.csv', sorted_count_Tdiff, delimiter=',',fmt='%.0f')

end = time.perf_counter()

print(f"Total Time: {end-start:.6f}")