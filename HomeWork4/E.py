"""
Пирамида

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Для строительства двумерной пирамиды используются прямоугольные блоки, каждый из
которых характеризуется шириной и высотой.

Можно поставить один блок на другой, только если ширина верхнего блока строго
меньше ширины нижнего (блоки нельзя поворачивать). Самым нижним в пирамиде может
быть блок любой ширины.

По заданному набору блоков определите, пирамиду какой наибольшей высоты можно
построить из них.


Формат ввода:
В первой строке входных данных задается число N — количество блоков
(1 ≤ N ≤ 100000). В следующих N строках задаются пары натуральных чисел w_i
и h_i (1 ≤ w_i, h_i ≤ 10^9) — ширина и высота блока соответственно.


Формат вывода:
Выведите одно целое число — максимальную высоту пирамиды.


Пример
input: 3
input: 3 1
input: 2 2
input: 3 3
output: 5

Примечания:
В примере пирамида будет состоять из двух блоков: нижним блоком будет блок
номер 3, а верхним — блок номер 2. Блок номер 1 нельзя использовать вместе с
блоком номер 3.
"""
