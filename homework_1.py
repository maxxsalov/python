# сколько тебе будет лет в таком то году?
# Программа,  которая спрашивает сколько тебе лет, потом ты вбиваешь год.
# Программа отвечает сколько тебе лет.
question_1 = int(input("Сколько тебе лет?: "))
question_2 = int(input("Сколько лет тебе будет в "))

# question_1 = question_1.strip()
# question_2 = question_2.strip()

year_of_birth = 2020 - question_1
result = question_2 - year_of_birth

print("Тебе будет - " + str(result))