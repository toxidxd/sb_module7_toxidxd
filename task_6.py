print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

students_count = int(input("Введите количество учеников: "))
excellent_score = 0
well_score = 0
satisfactory_score = 0

for student in range(students_count):
    score = int(input("Введите оценку: "))

    if score == 5:
        excellent_score += 1
    elif score == 4:
        well_score += 1
    elif score == 3:
        satisfactory_score += 1

if excellent_score > well_score:
    score_max = 5
else:
    score_max = 4
if satisfactory_score > score_max:
    score_max = 3

print('Больше всего оценок:', score_max)
