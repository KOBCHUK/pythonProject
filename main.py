try:
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            if (i == 0 and j == 1) or (i == 0 and j == 2) or (i == 1 and j == 2) or (i == 3 and j == 2) or (
                    i == 4 and j == 1) or (i == 4 and j == 2):
                print("  ", end=" ")
            elif (i == 0 and j == 3) or (i == 4 and j == 3):
                print("  ", end=" ")
            else:
                print("* ", end=" ")
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')
