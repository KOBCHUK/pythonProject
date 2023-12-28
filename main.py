try:
    number_task = int(input("Enter the task: "))
    if number_task == 1:
        print("Ex_1:")
        row = 0
        while row < n:
            col = 0
            while col < n:
                if row <= col and row + col <= n - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                col += 1
            print()
            row += 1
    elif triangle_number == 2:
        print("Правый треугольник (2):")
        row = 0
        while row < n:
            col = 0
            while col < n:
                if row <= col and row + col >= n - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                col += 1
            print()
            row += 1
    elif triangle_number == 3:
        print("Нижний треугольник (3):")
        row = 0
        while row < n:
            col = 0
            while col < n:
                if row >= col and row + col >= n - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                col += 1
            print()
            row += 1
    elif triangle_number == 4:
        print("Левый треугольник (4):")
        row = 0
        while row < n:
            col = 0
            while col < n:
                if row >= col and row + col <= n - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
                col += 1
            print()
            row += 1
    else:
        print("Неверный номер треугольника. Введите число от 1 до 4.")
except Exception as e:
    print(e)
    print('Error importing modules')

