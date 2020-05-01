def calculator(first_number, second_number):
    operation = input("Выберете операцию с числами (*, /, + или -): ")
    if operation == '/':
        if second_number == 0:
            print("Делить на 0 нельзя")
            return
        else:
            result = first_number / second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    return result


while True:
    a = input("Введите 1-ое числа: ")
    b = input("Введите 2-ое числа: ")
    if (a == 'exit') or (b == 'exit'):
        break
    else:
        a = float(a)
        b = float(b)
        print(calculator(a, b))
