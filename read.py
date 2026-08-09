from collections import Counter
import multiprocessing
import os
import time

# use lambda
def count_file(i, dir_path):
    with open(dir_path, "r") as f:
        data = f.read().split()
        count = Counter(data)
        # print(data)
        # print('=' * 60)
        # print(count)
        return count

def count_folder(folder_path):
    i = 0
    with open(f"{folder_path}/count.csv", "w") as f:
        f.write("file_num,1,2,3,4,5,6,7,8,9,10\n")
        while(True):
            try:
                count = count_file(i, f"{folder_path}/data/data-{i}.txt")
                f.write(str(i) + ',')
                for i in range(9):
                    f.write(str(count[f"{i+1}"]) + ',')
                f.write(f"{count[f"10"]}\n")
            except FileNotFoundError:
                print(f"total file: {i+1}")
                break
            i+=1
# dir_path = "/path/to/directory"
# Checks and creates the directory (and parent folders) if missing
# os.makedirs(dir_path, exist_ok=True)

os.makedirs("Pdata/data", exist_ok=True)
os.makedirs("Tdata/data", exist_ok=True)

if __name__ == "__main__":
    start = time.perf_counter()

    count_folder("Pdata")
    count_folder("Tdata")

    end = time.perf_counter()
    print(f"Count Total Time: {end-start:.6f}")