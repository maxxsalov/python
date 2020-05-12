s = input("Введите строку: ")


def polindrom(str):
    i = 0
    j = len(str) - 1
    palindrom = True
    while i < j:
        if s[i] != s[j]:
            palindrom = False
        i += 1
        j -= 1
    if palindrom == True:
        print("Строка явялется палиндромом")
    else:
        print("Строка не является палиндромом")


polindrom(s)
