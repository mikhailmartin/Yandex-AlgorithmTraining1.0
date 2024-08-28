"""
Сумма номеров

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Вася очень любит везде искать своё счастливое число K. Каждый день он ходит в
школу по улице, вдоль которой припарковано N машин. Он заинтересовался вопросом,
сколько существует наборов машин, стоящих подряд на местах с L до R, что сумма
их номеров равна K. Помогите Васе узнать ответ на его вопрос.

Например, если число N = 5, K = 17, а номера машин равны 17, 7, 10, 7, 10, то
существует 4 набора машин:
17 (L = 1, R = 1),
7, 10 (L = 2, R = 3),
10, 7 (L = 3, R = 4),
7, 10 (L = 4, R = 5).


Формат ввода:
В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 100 000, 1 ≤ K ≤ 10^9).
Во второй строке содержится N чисел, задающих номера машин. Номера машин могут
принимать значения от 1 до 999 включительно.


Пример 1
input: 5 17
input: 17 7 10 7 10
output: 4

Пример 2
input: 5 10
input: 1 2 3 4 1
output: 2
"""
