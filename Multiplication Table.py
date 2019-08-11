def mult_table(lo, hi):
    for i in range(lo, hi + 1):
        print("\t" + str(i), end="  ")
    for i in range(lo, hi + 1):
        print("\n" + str(i) + "\t", end="")
        for j in range(lo, hi + 1):
            print(str(i*j) + "\t", end=" ")
low = int(input("Input the lower range: "))
high = int(input("Input the higher range: "))
mult_table(low, high)

