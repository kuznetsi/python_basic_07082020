"""Задание № 1. Поработайте с переменными, создайте несколько, выведите
на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""
name = input('Привет дружок! Как мне к тебе обращаться? Представься: ')
print('Привет, ', name)
print('Сегодня мы будем заниматься переменными: ввод, ввывод, сохранение и т.д...')
print("""Если тебе интересно, вводи 1 и ты отправишься \"в страну чудес. Я покажу тебе, глубока ли кроличья нора.\"
или вводи 0 и \"сказке конец. Ты проснешься в своей постели и поверишь, что это был сон.\"
""")
play_ans = input('Выбор за тобой! 1 или 0? ')


def find_int(test_str, number_key, start_key):
    print('---', test_str[number_key])
    while test_str[number_key].isdigit():
        if number_key < len(test_str):
            number_key += 1
    print('Найденные числа: ', test_str[start_key:number_key])
    return number_key


if int(play_ans):
    print(':-)', 'А ты рисковый! \nПродолжаем...')
    text_for_analize = input('Введи что-нибудь в строку: буквы, цифры т.д.')
    print('Введенная строка: ', text_for_analize)
    len_str = len(text_for_analize)
    var_text = 0
    str_int = []
    while var_text < len_str:
        print('Буква/цифра: ', text_for_analize[var_text])
        if text_for_analize[var_text].isdigit():
            print('Отправляем:', text_for_analize, int(var_text), int(var_text))
            var_text = find_int(text_for_analize, int(var_text), int(var_text))
            print('Найдено число: ', var_text)
        else:
            var_text += 1
            print('else: var_text', var_text)

else:
    print(':-(', 'Звук будильника')
