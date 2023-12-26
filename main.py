try:
    x = 5
    y = 5
    i = j = 0
    while i < x:
        j = 0
        while j < y:
            if i <= j:
                print('*  ', end='')
            else:
                print('   ', end='')
            j += 1
        print()
        i += 1

except Exception as e:
    print(e)
    print('Error importing modules')