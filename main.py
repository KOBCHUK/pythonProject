try:
    n = int(input("Enter number: "))
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
except Exception as e:
    print(e)
    print('Error importing modules')


# try:
#     size = int(input("Enter the number: "))
#     if size % 2 == 0:
#         print("Number must be even")
#     else:
#         top = size // 2 + 1
#         bottom = size - top
#
#         for i in range(size):
#             if i < top:
#                 stars = "* " * (size - 2 * i)
#                 spaces = "  " * i
#             else:
#                 stars = "* " * (size - 2 * (bottom - (i - top + 1)))
#                 spaces = "  " * (size - i - 1)
#
#             line = spaces + stars
#             print(line)
# except Exception as e:
#     print(e)
#     print('Error importing modules')