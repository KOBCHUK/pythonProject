try:
    i = 3
    while i >= 0:
        j = 0
        while j < 4:
            if i + j < 4:
                print("*  ", end="")
            j += 1
        print()
        i -= 1
except Exception as e:
    print(e)
    print('Error importing modules')
