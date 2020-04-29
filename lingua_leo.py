import random

print("Сейчас можно будете ввести слова в наш словарик")
print("Если хотите остановить ввод слов, напишите q в английском")
print("Если не хотите вводить слова, то можете воспользоваться готовым словарем")
choise = input("Воспользоваться готовым словарем? (ведите да, yes или y) ").lower().strip()

slovar = {}
if choise == "да" or choise == "yes" or choise == "y":
    slovar = {'zoo': 'зоопарк', 'book': 'книга', 'dog': 'собака', 'cat': 'кошка', 'man':'мужчина', 'woman':'женщина'}
else:
    while True:
        key = input("Введите слово на английском\n:").lower().strip()
        if key == 'q':
            break
        value = input("Введите слово на русском\n:").lower().strip()
        slovar[key] = value

print(slovar)
print("Пора потренироваться, ошибок у нас не более 3")

errors = 0
bonus = 0

list_keys = list(slovar.keys())

random.shuffle(list_keys)

for key in list_keys:
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как\n :").lower().strip()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично! Ваш счет составляет: ", bonus)
    elif errors > 3:
        print("Game over")
        break
    else:
        errors += 1
        print('Количество ошибок', errors)