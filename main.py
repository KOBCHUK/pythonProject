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

    elif number_task == 4:
        print("Ex_4:")

    else:
        print("Wrong number. Enter a number from 1 to 10.")
except Exception as e:
    print(e)
    print('Error importing modules')

