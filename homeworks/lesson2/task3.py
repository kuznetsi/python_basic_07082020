"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

"""
while True:
    input_list = input('Введите номер месяца от 1 до 12')
    if (input_list.isdigit() & 1 <= int(input_list) <= 12):
        result_list = int(input_list)
        break
    print('Чтобы продолжить, надо что-то соответствующее условию')

seasons = ['Зима', 'Весна', 'Лето', 'Осень']
if (result_list <= 2 or result_list == 12):
    print(seasons[0])
elif result_list <= 5:
    print(seasons[1])
elif result_list <= 8:
    print(seasons[2])
else:
    print(seasons[3])

seasons_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for key in seasons_dict.keys():
    if result_list in seasons_dict.get(key):
        print(key)
