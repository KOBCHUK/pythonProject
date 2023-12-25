try:

    n = int(input("Enter the height of the triangle: "))

    i = 0
    while i <= n:
        print(" " * (n - i), "*" * (2 * i + 1))
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')