# Воспользоваться кодом из нашей функции assert
# прогнать все товары в словарь из файла  data.txt
# через скидки в discount.txt
# и итоговой товар с названием и ценником должен генерироваться программно
# наша задача не допустить отрицательной скидки
data = {}
with open("data.txt", encoding='utf-8') as file:
    for line in file:
        key, value = line.strip().split(',')
        data[key] = value
print("Список товаров до скидки: ")
for k in data.keys():
    print(k + ' - ' + data[k])

discount = []
with open("discount.txt") as file:
    for line in file:
        key = line.split()
        discount += key


def apply_discount(product, discount):
    """ продукт на вход приходит в виде словаря, а функция возвращает его имя и скидку"""
    i = 0
    for price in product.keys():
        amount = int(product[price]) * (1.0 - float(discount[i]))
        try:
            assert 0 <= amount <= int(product[price])
        except AssertionError:
            print("Протри глаза! ")
        else:
            data[price] = str("%.2f" % amount)
        i += 1
    return data


res = apply_discount(data, discount)
print("\nСписок товаров после скидки: ")
for key in res.keys():
    print(key + ' - ' + res[key])