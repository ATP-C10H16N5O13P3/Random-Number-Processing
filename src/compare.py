import time
import numpy as np

start = time.perf_counter()

with open("../Pdata/sorted_diff.csv", "r") as f:
    Pdiff_sorted = f.read().splitlines()

with open("../Tdata/sorted_diff.csv", "r") as f:
    Tdiff_sorted = f.read().splitlines()

for i in range(len(Pdiff_sorted)):
    Pdiff_sorted[i] = Pdiff_sorted[i].split(',')

for i in range(len(Tdiff_sorted)):
    Tdiff_sorted[i] = Tdiff_sorted[i].split(',')

Pdiff_sorted = np.array(Pdiff_sorted).astype(int)
Tdiff_sorted = np.array(Tdiff_sorted).astype(int)

with open("../Pdata/amp_diff.csv", "r") as f:
    temp = f.read().splitlines()
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    Pdiff_amp = np.array(temp)

with open("../Tdata/amp_diff.csv", "r") as f:
    f.read().splitlines()
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    Tdiff_amp = np.array(temp)

def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if value is present at mid
        if arr[mid] == value:
            return mid

        # If value is greater, ignore the left half
        elif arr[mid] < value:
            left = mid + 1

        # If value is smaller, ignore the right half
        else:
            right = mid - 1

    # Return -1 if the value is not in the array
    return -1

def sum_arr_before(before_idx):
    pass

print(binary_search(Pdiff_sorted[:, 0], Pdiff_amp[0]))

end = time.perf_counter()

print(f"Total Time: {end-start:.6f}")