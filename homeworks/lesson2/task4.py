"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.

"""
while True:
    input_list = input('Введите через пробел элементы списка')
    if input_list:
        result_list = input_list.split(' ')
        break
    print('Чтобы продолжить, надо что-то ввести')

i = 0
j = 0
len_list = len(result_list)
while i < (len_list):
    list_word = len(result_list[i])
    if list_word > 10:
        j += 1
        print(f"{j}.{result_list[i][:10]}")
    else:
        j += 1
        print(f"{j}.{result_list[i]}")
    i += 1
