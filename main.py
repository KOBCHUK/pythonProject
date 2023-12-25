try:
    n = int(input("Enter the height of the triangle: "))
    i = 1
    while i <= n:
        print(" " * (i - 1), "*" * (2 * (n - i) - 1))
        i += 1
except Exception as e:
    print(e)
    print('Error importing modules')