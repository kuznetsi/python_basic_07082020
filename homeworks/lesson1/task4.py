"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""
number = abs(int(input('Привет дружок! Введи число и программа найдет самую большую цифру в числе.: ')))
str_number = str(number)
len_str = len(str(number))
step_position = 0
max_num = int(str_number[step_position])
max_num_next = 0
while len_str > step_position:
    max_num = max(max_num, int(str_number[step_position]))
    step_position += 1
print('Самая большая цифра в числе', max_num)