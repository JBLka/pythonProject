import csv

with open('students.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader = list(reader)
    request = input()
    while request != 'СТОП':   # Ожидаем остановку
        is_real_project = False
        for i in range(len(reader)):
            if reader[i]['titleProject_id'] == request:    # Если введеный номер равен номеру проекта
                project_id = reader[i]['titleProject_id']
                name = reader[i]['Name'].split()
                score = reader[i]['score']
                print(f'Проект № {project_id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}')
                is_real_project = True   # Проект найден
                break
        if not is_real_project:          # Если проект не найден
            print('Ничего не найдено')
        request = input()
