# Написать классическую игру на условных конструкциях: угадай, какое число.
# Пользователя вначале спрашивают, какой уровень сложности он готов выбрать: низкий, средний и высокий.
# На низком уровне у человека будет 12 попыток,  на среднем - 9, на высоком - только 6.
# Если человек вводит слишком большое число, ему говорится, что “нужно поменьше”, 
# если маленькое - пишет “ нужно побольше”. 
# Если человек угадал, тогда ему нужно написать, что он победил. Если проиграл, утешить.

import random
levels = ['низкий', 'средний', 'высокий']
trials = [12, 9, 6]
name_player = input("Привет! Как тебя зовут? ")
name_player = name_player.strip().title()
print("Привет, {name_player}! Я хочу сыграть с тобой в игру".format(name_player=name_player))
level = int(input("""
	Введи уровень сложности:
	0 - низкий, 1 - средний или 2 - высокий
	"""))
for k in range(len(levels)):
	if k != level:
		continue
	else:
		print("Ты выбрал {level} уровень".format(level=levels[k]))
		for l in range(len(trials)):
			if l == level:
				print("У тебя {trial} попыток".format(trial=trials[l]))
				j = 0		
				random_number = random.randint(1, 99)
				while j < trials[k]:
					player_answer = int(input("Введи число от 1 до 99: " ))
					if player_answer < 1 or player_answer > 99:
						j += 1
						print("Введено неккоректное число! У тебя минус одна попытка. Осталось {trial} попыток".format(trial=(trials[l]-j)))
					elif j == trials[l]-1 and player_answer != random_number:
						print("""
							Ты проиграл. Загаданное число - {random_number}. 
							Но не огорчайся!
							Не везет в играх - повезет в другом!
							""".format(random_number=random_number))
						break
					else:
						if player_answer > random_number:
							j += 1
							print("Нужно число поменьше! Осталось {trial} попыток".format(trial=(trials[l]-j)))							
						elif player_answer < random_number:
							j += 1
							print("Нужно число побольше! Осталось {trial} попыток".format(trial=(trials[l]-j)))
						else:
							print("Ты выиграл! Поздравляю!")
							break