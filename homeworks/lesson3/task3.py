"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def summaxlist(summand: list):
    """Возвращает сумму наибольших аргументов кроме самого наименьшего

    Именованные параметры:
    summand -- список чисел для обработки
    """
    summand.remove(min(summand))  # удаляем из списка минимальный элемент

    return sum(summand)  # возвращаем сумму оставшихся элементов


def chk_digit(number_input: str):
    while True:
        if number_input.isdigit():
            user_num: int = int(number_input)
            break
        print('Ошибка ввода, это не число')
    return user_num


def minlist(min_num: list):
    return min(min_num)  # возвращаем сумму оставшихся элементов

i = 1
num_list = []


num_steps: str = input('Введите количество чисел для ввода: ')
steps = chk_digit(num_steps)

while i <= steps:
    user_input: str = input(f'Введите {i} число из {steps}: ')
    user_number = chk_digit(user_input)
    num_list.append(user_number)
    i += 1

print(f'Исходный список чисел: {num_list}')
print(f'Минимальное число: {minlist(num_list)}')
print(f'Преобразованный список: ')

summaxlist(num_list)
print(summaxlist(num_list))
