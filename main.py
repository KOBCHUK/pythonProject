try:
    n = int(input("Enter numder: "))
    if n <= 0:
        raise Exception('Number must be greater than 0')
    if n % 2 == 0:
        raise Exception('Number must be odd')
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i >= j and i + j <= n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')
