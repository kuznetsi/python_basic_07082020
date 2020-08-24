"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


def salary():
    """
    Создание файла и наполнение его информацией.
    Чтобы запусть функцию необходимо написать: python task1.py create_my_file.
    Запрашивается имя файла.
    После успешного названия файла происходит построчное заполнение файла.
    Завершение наполнения файла является пустая строка и нажатие Enter.
    Успешным завершением работы программы является сообщение Файл сохранен!
    """
    while True:
        hour_input = input('Введите количество часов: ')
        if hour_input.isdigit():
            hour_input = int(hour_input)
            break

        print('Введите число: ')
    while True:
        price_input = input('Введите ставку в час: ')
        if price_input.isdigit():
            price_input = int(price_input)
            break

        print('Введите число: ')

    while True:
        bonus_input = input('Введите премию: ')
        if bonus_input.isdigit():
            bonus_input = int(bonus_input)
            break

        print('Введите число: ')

    result = (hour_input * price_input) + bonus_input
    print(result)


if __name__ == '__main__':
    salary()
