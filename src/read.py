from collections import Counter
import os
import time

def count_file(dir_path):
    with open(dir_path, "r") as f:
        data = f.read().split() # data into array
        count = Counter(data) # count each occurances of data points
        return count

def count_folder(folder_path):
    with open(f"{folder_path}/count.csv", "w") as f: # output file
        f.write("file_num,1,2,3,4,5,6,7,8,9,10\n") # csv header
        i = 0
        while(True):
            try:
                count = count_file(f"{folder_path}/data/data-{i}.txt")

                # write result to output file
                f.write(str(i) + ',') # file number
                for j in range(9):
                    f.write(str(count[f"{j+1}"]) + ',') # each count of data point
                f.write(f"{count[f"10"]}\n") # no comma at the last count

            except FileNotFoundError: # final / last file
                print(f"Total file: {i}")
                break
            i+=1 # Go to next file

# Check Required Directory
os.makedirs("../Pdata/data", exist_ok=True)
os.makedirs("../Tdata/data", exist_ok=True)

if __name__ == "__main__":
    start = time.perf_counter()

    # count both Pdata and Tdata
    count_folder("../Pdata")
    count_folder("../Tdata")

    end = time.perf_counter()
    print(f"Count Total Time: {end-start:.6f}")