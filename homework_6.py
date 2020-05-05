file_to_work = input("Введите имя файла: ")
file_to_work += ".txt"


def stat_amount(file_name):
    amount = 0
    i = 0
    with open(file_name) as file:
        for line in file:
            amount += int(line)
    print(amount)
    middle_value = amount / len(line)
    print(middle_value)
    filename = input("Введите имя файла для записи результатов: ")
    filename += ".txt"
    with open(filename, 'w') as file:
        file.write("Сумма всех числовых значений равна: " + str(amount))
        file.write("\nСреднее значение равно: " + str(middle_value))



stat_amount(file_to_work)

