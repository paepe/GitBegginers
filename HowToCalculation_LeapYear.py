# User enters the year
year = int(input("Entre o ano: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "é um ano bissexto")
elif year % 100 == 0:
    print(year, "não é um ano bissexto")
elif year % 400 == 0:
    print(year, "é um ano bissexto")
else:
    print(year, "não é um ano bissexto")