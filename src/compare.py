import time
import numpy as np

start = time.perf_counter()

# read data
with open("../Pdata/sorted_diff.csv", "r") as f:
    Pdiff_sorted = f.read().splitlines()

with open("../Tdata/sorted_diff.csv", "r") as f:
    Tdiff_sorted = f.read().splitlines()

for i in range(len(Pdiff_sorted)):
    Pdiff_sorted[i] = Pdiff_sorted[i].split(',')

for i in range(len(Tdiff_sorted)):
    Tdiff_sorted[i] = Tdiff_sorted[i].split(',')

# format data to int
Pdiff_sorted = np.array(Pdiff_sorted).astype(int)
Tdiff_sorted = np.array(Tdiff_sorted).astype(int)

# read data to find sum
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

# find total score
sum = len(Pdiff_amp) * len(Tdiff_amp)

Pdiff_amp,Tdiff_amp = None,None

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
    return left

# comparing Pdiff and Tdiff
with open("../Pdata/score.csv", "w") as f:
    for i in (range(len(Pdiff_sorted[:,0]))):
        arr_idx = binary_search(Tdiff_sorted[:, 0], Pdiff_sorted[i,0])
        f.write(f"{np.sum(Tdiff_sorted[:arr_idx,1]) * Pdiff_sorted[i,1]}\n")

with open("../Tdata/score.csv", "w") as f:
    for i in (range(len(Tdiff_sorted[:,0]))):
        arr_idx = binary_search(Pdiff_sorted[:, 0], Tdiff_sorted[i,0])
        f.write(f"{np.sum(Pdiff_sorted[:arr_idx,1]) * Tdiff_sorted[i,1]}\n")

# resign unused variable to None
Pdiff_sorted,Tdiff_sorted = None,None

# calculate each scores
scoreP = np.sum(np.loadtxt('../Pdata/score.csv', delimiter=',', dtype=int))
scoreT = np.sum(np.loadtxt('../Tdata/score.csv', delimiter=',', dtype=int))

scoreEqual = sum - (scoreP + scoreT)

# print result
print("=" * 60)
print(f"All: {sum}")
print(f"ScoreP: {scoreP}")
print(f"ScoreT: {scoreT}")
print(f"Equal: {scoreEqual}")
print("=" * 60)
print("Comparing with old program")
print(f"All: {sum*2}")
print(f"ScoreP: {scoreP*2}")
print(f"ScoreT: {scoreT*2}")
print(f"Equal: {scoreEqual*2}")
print("=" * 60)

# print to file
with open("result.txt", "a") as f:
    print("=" * 60, file=f)
    print(f"All: {sum}", file=f)
    print(f"ScoreP: {scoreP}", file=f)
    print(f"ScoreT: {scoreT}", file=f)
    print(f"Equal: {scoreEqual}", file=f)
    print("=" * 60, file=f)
    print("Comparing with old program", file=f)
    print(f"All: {sum*2}", file=f)
    print(f"ScoreP: {scoreP*2}", file=f)
    print(f"ScoreT: {scoreT*2}", file=f)
    print(f"Equal: {scoreEqual*2}", file=f)
    print("=" * 60, file=f)

end = time.perf_counter()

print(f"Total Time: {end-start:.6f}")