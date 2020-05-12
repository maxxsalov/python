# Сделать программу, которая собирает данные пользователей - в нем можно ввести логин пользователя и почту,
# и если с помощью проверки регулярными выражениями валидны, тогда они записываются в файл. В другом случае,
# пользователю говорится, что у него ошибка в введеных данных и нужно заново ввести данные.
from re import search


def login_check(login):
    if search(r'^[!-~]{8,32}$', login):
        return login
    return 0


def email_check(email):
    if search(r'[a-z0-9\._]+@\w+\.\w+', email):
        return email
    return 0


print("""
    Сейчас Вам потребуется ввести логин и почту.
    Если данные валидны, то они сохранятся, иначе потребуется ввести почту еще раз.
    Для выхода введите !q
    """)
filename = "email_data.txt"
while True:
    log_in = input("Введите логин: ")
    e_mail = input("Введите почту: ")
    if log_in == '!q':
        break
    else:
        login_res = login_check(log_in)
        email_res = email_check(e_mail)
        if login_res == 0 or email_res == 0:
            print("Введено некорректное значение. Повторите ввод")
            continue
        else:
            with open(filename, 'a') as file:
                file.write("Логин: " + str(login_res) + ", почта: " + str(email_res) + "\n")
