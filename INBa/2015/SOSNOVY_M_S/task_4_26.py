# Задача 4. Вариант 26.
# Напишите программу, которая выводит имя, под которым скрывается Аркадий Петрович Голиков. Дополнительно необходимо вывести область интересовуказанной личности, место рождения, годы рождения и смерти (если человекумер), вычислить возраст на данный момент (или момент смерти). Для хранениявсех необходимых данных требуется использовать переменные. После выводаинформации программа должна дожидаться пока пользователь нажмет Enter длявыхода.


# Sosnovy M.S.
# 01.02.2016


print("Аркадий Петрович Голиков крывался под именем Арка́дий Петро́вич Гайда́р ")
print("Pусский, советский детский писатель, киносценарист. ")
bo = int (1904)
de = int (1941)
print("Родился 9 (22) января " + str (bo) + ", Льгов, Курская губерния \nУмер 26 октября " + str (de) + ", близ села Лепляво, Каневский район, Черкасская область")
yo = -(bo - de)
print("Поэт умер в возасте " + str (yo))
input("\n\nНажмите Enter для выхода.")