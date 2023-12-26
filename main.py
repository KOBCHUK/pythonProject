try:
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if i + j >= 3:
                print('*  ', end='')
            else:
                print('   ', end='')
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')