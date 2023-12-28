try:
    number_task = int(input("Enter the task 1-10: "))
    if number_task == 1:
        print("Ex_1:")
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
    elif number_task == 2:
        print("Ex_2:")
        i = 3
        while i >= 0:
            j = 0
            while j < 4:
                if i + j < 4:
                    print("*  ", end="")
                j += 1
            print()
            i -= 1
    elif number_task == 3:
        print("Ex_3:")
        n = int(input("Enter the height of the triangle: "))
        i = 1
        while i <= n:
            print("  " * (i - 1), "* " * (2 * (n - i) - 1))
            i += 1
    elif number_task == 4:
        print("Ex_4:")
        n = int(input("Enter the height of the triangle: "))
        i = 0
        while i <= n:
            print("  " * (n - i), "* " * (2 * i + 1))
            i += 1
    elif number_task == 5:
        n = int(input("Enter the height of triangle: "))
        if n <= 0:
            raise Exception('Number should be greater than 0')
        if n % 2 == 0:
            raise Exception('Number should be odd')
        i = 0
        while i < n:
            j = 0
            while j < n:
                if (i <= j and i + j <= n - 1) or (i >= j and i + j >= n - 1):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                j += 1
            print()
            i += 1
    elif number_task == 6:
        n = int(input("Enter the height of triangle: "))
        if n < 0:
            raise Exception('Number cannot be negative')
        if n % 2 == 0:
            raise Exception('Number cannot be even')
        i = 0
        while i < n:
            j = 0
            while j < n:
                if (i <= j and i + j >= n - 1) or (i >= j and i + j <= n - 1):
                    print('* ', end=' ')
                else:
                    print('  ', end=' ')
                j += 1
            print()
            i += 1
    elif number_task == 7:
        n = int(input("Enter the height of triangle: "))
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
    elif number_task == 8:
        n = int(input("Enter the height of triangle: "))
        if n < 0:
            raise Exception('Number must be positive')
        if n % 2 == 0:
            raise Exception('Number must be odd')
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i <= j and i + j >= n - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                j += 1
            print()
            i += 1
    elif number_task == 9:
        i = 0
        while i < 4:
            j = 0
            while j < 4:
                if i + j < 4:
                    print('*  ', end='')
                j += 1
            print()
            i += 1
    elif number_task == 10:
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
    else:
        print("Wrong number. Enter a number from 1 to 10.")
except Exception as e:
    print(e)
    print('Error importing modules')

