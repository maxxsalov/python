# dz На основе предыдущих занятий создайте класс User, у которого реализовано несколько методов и атрибутов:
# атрибут login
# атрибут password
# атрибут uniq_id
# любые другие атрибуты на ваше усмотрение
# есть метод greet, который спрашивает User,  зарегистрирован он ли в этой системе. Если нет,тогда он предлагает
# зарегистрироваться(login и пароль проверяются на регулярных выражениях, а атрибут uniq_id генерируется программно).
# При правильной регистрации создается его профайл в файле login[рандомное число].txt.
# После этого можно войти на ресурс, в котором можно сыграть в любую из двух предложенных игр,
# которые можно найти здесь: http://pythonicway.com/component/tags/tag/4-python-games
# (проблемная ситуация в том, что эти игры написаны на Python 2 и их надо переписать)
#
# * валидизация должна происходить с помощью методов validate_login  validate_password у отдельного класса Validate
from random import choice
from string import digits
from re import search
import snake_game


class Validate:
    @staticmethod
    def validate_login(login):
        if search(r'^[!-~]{8,32}$', login):
            return True
        return False

    @staticmethod
    def validate_password(password):
        if search(r'^[!-~]{8,32}$', password):
            return True
        return False

    def uniq_id():
        id = ''.join(choice(digits) for i in range(10))
        return id


class User:
    def __init__(self, login, password, id):
        self.login = login
        self.password = password
        self.id = id

    def new_user(self):
        with open("email_data.txt", 'a') as file:
            file.write("ID " + self.id + ", l: " + self.login + ", p: " + self.password + "\n")


filename = "email_data.txt"
usr_str = ''
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        usr_str += line.strip()


def greet():
    are_u_user = input('Зарегистрированы ли вы в нашей системе? ')
    if are_u_user.lower().strip() == 'да':
        if usr_str != '':
            usr = input('Введите свой логин: ')
            if usr in usr_str:
                print("Вы зарегистрированы и больше не можете сыграть в нашу игру")
                return 0
        else:
            print("В нашей системе нет ещё пользователей")
            return 0
    else:
        created = False
        while not created:
            usr = input('Введите логин: ')
            if usr in usr_str:
                print("Такой пользователь существует")
                exit()
            else:
                pass_word = input("Введите пароль для завершения регистрации " + usr + ": ")
                if Validate.validate_login(usr) and Validate.validate_password(pass_word):
                    id_usr = Validate.uniq_id()
                    new_usr = User(usr, pass_word, id_usr)
                    new_usr.new_user()
                    print("Время для игры!")
                    created = True
                else:
                    print("Введены некорректные значения логина/пароля! Повторите ввод")


if (greet() == 0):
    exit()
else:
    snake_game.start()
