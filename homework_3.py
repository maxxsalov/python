# Вывести полную таблицу умножения, вместе с числами, которые учавствуют в операции,  в таком виде:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3 
# И так далее
print("\t\t\t\tШКОЛЬНАЯ ТАБЛИЦА УМНОЖЕНИЯ\n")
num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in num:
    for j in range(1,11):
    	first_column = str(i[0]) + ' * ' + str(j) + ' = ' + str(i[0]*j)
    	second_column = str(i[1]) + ' * ' + str(j) + ' = ' + str(i[1]*j)
    	third_column = str(i[2]) + ' * ' + str(j) + ' = ' + str(i[2]*j)
    	print (first_column + '\t\t', '\t\t' + second_column + '\t\t', '\t\t' + third_column)
    print('\n')