import itertools

def combination(n,k):
    if __name__ == "__main__":
        # program to find all the combination from the binomial coefficient nCr(n,r)
        elements = list(range(1, n + 1))

        with open("AllCombinations.csv", "w") as file:
            for k in range(5):
                for combo in itertools.combinations(elements, r):
                    # print(combo, file=file)
                    for i in combo:
                        print(str(i+20*k-1), end=",", file=file) # print the combination into a file with comma separating the num
                    print("", file=file) # print to separate the combination

combination(20,10)