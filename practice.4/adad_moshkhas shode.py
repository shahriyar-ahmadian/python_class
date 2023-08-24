number = float(input("enter youre number:\n"))
if number < 0:
    print("is number zero")
else:
    if (number // 2) * 2 == number:
        if (number % 10) > 6:
            print("lower")
        elif number < 4:
            print("yuor number lower 4")
        else:
            print("yuor number uper 4")
    else:
        print("yuor number uper 4")
