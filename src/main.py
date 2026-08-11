import subprocess
import sys
import os

def run(file_name):
    # sys.executable ensures you use the exact same Python environment
    result = subprocess.run([sys.executable, file_name], capture_output=True, text=True)

    print(result.stdout)
    print('-'*60)

run("read.py")
run("diff.py")
run("amplify.py")
run("sort.py")
run("compare.py")

def rm(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
# optional
if True:
    rm("AllCombinations.csv")
    folder_path = ["../Pdata","../Tdata"]
    for i in folder_path:
        rm(f"{i}/count.csv")
        rm(f"{i}/diff.csv")
        rm(f"{i}/amp_diff.csv")
        rm(f"{i}/sorted_diff.csv")
        rm(f"{i}/score.csv")