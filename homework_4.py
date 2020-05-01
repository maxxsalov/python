#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машиной той же марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

#  д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом
all_people = shevrole_owner | work_near | live_near

people_who_live_n_work = live_near | work_near
print("И живут и работают рядом", end=' ')
print(people_who_live_n_work)

work_n_live_n_shevrole = shevrole_owner & people_who_live_n_work
print("И владеют авто, и живут и работают рядом", end=' ')
print(work_n_live_n_shevrole)

killer = shevrole_owner - live_near - work_near
print("Убийца", end=' ')
print(killer)