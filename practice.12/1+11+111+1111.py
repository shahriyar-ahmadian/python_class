def number(num):
    num = str(num)
    n1 = num
    n2 = num+num
    n3 = num+num+num
    return int(n1) + int(n2) + int(n3)
number_user = int(input("enter youre number: "))
print(number(number_user))