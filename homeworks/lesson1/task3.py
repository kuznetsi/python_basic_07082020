"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
number = int(input('Привет дружок! Введи число и программа посчитает n + nn + nnn: '))
move = 3
n = 0
number_join = number
while move:
    n = n + number_join
    number_join = int(str(number_join) + str(number))
    move -= 1
print('n + nn + nnn: ', n)