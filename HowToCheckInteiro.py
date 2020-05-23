# User enters the number
number = int(input("Enter number: "))

# checking the number
if number < 0:
    print("O número é negativo.")
elif number > 0:
    print("O número é positivo.")
elif number == 0:
    print("O número é zero.")
else:
    print("A entrada não é um número")
