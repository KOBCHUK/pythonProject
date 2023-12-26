try:
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            if (i == 0 and j == 4) or (i == 1 and j in [3, 4]) or (i == 2 and j in [2, 3, 4]) or (
                    i == 3 and j in [3, 4]) or (i == 4 and j == 4):
                print("* ", end=" ")
            else:
                print("  ", end=" ")
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')