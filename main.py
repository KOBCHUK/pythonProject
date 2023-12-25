try:
    size = int(input("Введите размер песочных часов (нечетное число): "))

    if size % 2 == 0:
        print("Размер должен быть нечетным!")
    else:
        i = 1

        while i <= size:
            if i <= size // 2 + 1:
                spaces = " " * (i - 1)
                stars = "*" * ((size - i * 2) + 2)
            else:
                spaces = " " * (size - i)
                stars = "*" * ((i - size // 2) * 2)

            line = spaces + stars
            print(line)
            i += 1
except Exception as e:
    print(e)
    print('Error importing modules')