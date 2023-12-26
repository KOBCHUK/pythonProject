try:
    size = int(input("Enter the number: "))
    if size % 2 == 0:
        print("Number must be even")
    else:
        top = size // 2 + 1
        bottom = size - top

        for i in range(size):
            if i < top:
                stars = "* " * (size - 2 * i)
                spaces = "  " * i
            else:
                stars = "* " * (size - 2 * (bottom - (i - top + 1)))
                spaces = "  " * (size - i - 1)

            line = spaces + stars
            print(line)
except Exception as e:
    print(e)
    print('Error importing modules')