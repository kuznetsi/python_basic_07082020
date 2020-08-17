"""1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(dividend, divider):
    quotient = dividend / divider
    return quotient


inp_num_1 = input('Введите число, которое хотите разделить: ')
inp_num_2 = input('Введите число, на которое хотите разделить: ')

inp_num_1 = int(inp_num_1)
inp_num_2 = int(inp_num_2)

print('Результат', division(inp_num_1, inp_num_2))