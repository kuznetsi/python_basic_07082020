"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def about_user(name, surname, year_birth, city_residence, email, telephone):
    string_user = name + ' ' + surname + ' ' + year_birth + ' ' + city_residence + ' ' + email + ' ' + telephone
    return string_user


# name, surname, year of birth, city of residence, email, telephone

inp_name = input('Введите имя пользователя: ')
inp_surname = input('Введите фамилия пользователя: ')
inp_year_birth = input('Введите год рождения пользователя: ')
inp_city_residence = input('Введите город проживания пользователя: ')
inp_email = input('Введите email пользователя: ')
inp_telephone = input('Введите телефон пользователя: ')


print('Результат', about_user(name=inp_name, surname=inp_surname, year_birth=inp_year_birth, city_residence=inp_city_residence, email=inp_email, telephone=inp_telephone))
