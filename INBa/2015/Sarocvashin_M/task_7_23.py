# Задача 6. Вариант 23
#1-50. Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# Сароквашин Максим
# 13.05.2016


import random

print("Компьютер загадал название одного из семи дней недели, а Вы должны его угадать.\n")

days = ('Понедельник','Вторник','Срела','Четверг','Пятница','Суббота','Воскресенье')
day = random.randint(0,6)
x = 0
i = 0
score = 0


while(x != 7):
	print(day[x])
	x += 1

answer = input("\nВведите день: ")

while(answer != days[day]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите день: ")
    i += 1

if i == 0:
	score = 10
	
elif 0<i<6:
	score = 10 - i*2
	
else:
	score = 0

print("Верно, Вы победили!")
print("Число попыток: "+str(i))
print("Вы заработали "+str(score)+" баллов")

input("\nДля выхода нажмите Enter.")