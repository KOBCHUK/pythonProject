try:
    i = 0
    while i < 5:
        j = 0
        while j <= i:
            if (i == 0 and j == 0) or (i == 1 and j <= 1) or (i == 2 and j <= 2) or (i == 3 and j <= 1) or (
                    i == 4 and j == 0):
                print("*", end="\t")
            else:
                print("\t", end="\t")
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')