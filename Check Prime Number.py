# taking input from user
number = int(input("Entre o número: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "não é número primo")
            break
    else:
        print(number, "é número primo")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "não é número primo")