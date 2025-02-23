"""
Субботник

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В классе учатся N человек. Классный руководитель получил указание направить на
субботник R бригад по С человек в каждой.

Все бригады на субботнике будут заниматься переноской брёвен. Каждое бревно
одновременно несут все члены одной бригады. При этом бревно нести тем удобнее,
чем менее различается рост членов этой бригады.

Числом неудобства бригады будем называть разность между ростом самого высокого и
ростом самого низкого членов этой бригады (если в бригаде только один человек,
то эта разница равна 0). Классный руководитель решил сформировать бригады так,
чтобы максимальное из чисел неудобства сформированных бригад было минимально.
Помогите ему в этом!

Рассмотрим следующий пример. Пусть в классе 8 человек, рост которых в
сантиметрах равен 170, 205, 225, 190, 260, 130, 225, 160, и необходимо
сформировать две бригады по три человека в каждой. Тогда одним из вариантов
является такой:
1 бригада: люди с ростом 225, 205, 225
2 бригада: люди с ростом 160, 190, 170

При этом число неудобства первой бригады будет равно 20, а число неудобства
второй — 30. Максимальное из чисел неудобств будет 30, и это будет наилучший
возможный результат.


Формат ввода:
Сначала вводятся натуральные числа N, R и C — количество человек в классе,
количество бригад и количество человек в каждой бригаде (1 ≤ R∙C ≤ N ≤ 100_000).
Далее вводятся N целых чисел — рост каждого из N учеников. Рост ученика —
натуральное число, не превышающее 1_000_000_000.


Формат вывода:
Выведите одно число — наименьше возможное значение максимального числа
неудобства сформированных бригад.


Пример:
input: 8 2 3
input: 170
input: 205
input: 225
input: 190
input: 260
input: 130
input: 225
input: 160
output: 30
"""
