"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


def salary():
    """
    Расчет заработной платы сотрудника.
    Чтобы запусть функцию необходимо написать: python task1.py salary.
    Запрашивается количество часов, ставку в час, премию.
    Успешным завершением работы программы является расчет зарплаты!
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
