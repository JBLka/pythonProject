import random, csv
from string import ascii_letters, digits


def create_password():   # Создаём пароль
    letter_digit = ascii_letters + digits
    password = ''.join(random.choices(letter_digit, k=8))
    return password


def create_login(name):  # Создаём логин
    name = name.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


with open('students.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader = list(reader)
    for person in reader:
        person['login'] = create_login(person['Name'])   # Создаем и сохраняем логин и пароль
        person['password'] = create_password()

with open('students_password.csv', 'w', encoding='utf-8') as file:
    names = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    writer = csv.DictWriter(file, fieldnames=names)      # Записываем все данные в новый файл
    writer.writerows(reader)
