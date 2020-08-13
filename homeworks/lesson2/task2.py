"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""
while True:
    input_list = input('Введите через пробел элементы списка')
    if input_list:
        result_list = input_list.split(' ')
        break
    print('Чтобы продолжить, надо что-то ввести')

i = 0
len_list = len(result_list)
if len_list == 1:
    print(result_list)
else:
    while i < (len_list - 1):
        result_list.insert(i, result_list[i + 1])
        result_list.pop(i + 2)
        i += 2
    print(result_list)