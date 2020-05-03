# taking user input
ch = input("Entre um caracter: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(ch, "é alfabética")
else:
    print(ch, "não é alfabética")