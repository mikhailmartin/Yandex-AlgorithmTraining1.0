"""
Детали

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Имеется N кг металлического сплава. Из него изготавливают заготовки массой K кг
каждая. После этого из каждой заготовки вытачиваются детали массой M кг каждая
(из каждой заготовки вытачивают максимально возможное количество деталей). Если
от заготовок после этого что-то остается, то этот материал возвращают к началу
производственного цикла и сплавляют с тем, что осталось при изготовлении
заготовок. Если того сплава, который получился, достаточно для изготовления
хотя бы одной заготовки, то из него снова изготавливают заготовки, из них –
детали и т.д. Напишите программу, которая вычислит, какое количество деталей
может быть получено по этой технологии из имеющихся исходно N кг сплава.


Формат ввода:
Вводятся N, K, M. Все числа натуральные и не превосходят 200.


Формат вывода:
Выведите одно число — количество деталей, которое может получиться по такой
технологии.


Пример 1
input: 10 5 2
output: 4

Пример 2
input: 13 5 3
output: 3

Пример 3
input: 14 5 3
output: 4
"""


def recursive(n: int, k: int, m: int) -> int:

    blank_num, blank_residual = divmod(n, k)
    component_num, component_residual = divmod(k, m)

    residual = blank_residual + (blank_num * component_residual)

    if residual < k:
        return blank_num * component_num
    else:
        return (blank_num * component_num) + recursive(residual, k, m)


def not_recursive(n: int, k: int, m: int) -> int:

    component_num_total = 0
    material = n

    while True:
        blank_num_t, blank_residual_t = divmod(material, k)
        if not blank_num_t:
            break

        component_num, component_residual = divmod(k, m)
        if not component_num:
            break

        component_num_total += blank_num_t * component_num
        material = blank_residual_t + blank_num_t * component_residual

    return component_num_total


if __name__ == "__main__":

    # n, k, m = map(int, input().split())
    # n, k, m = 10, 5, 2
    # n, k, m = 13, 5, 3
    n, k, m = 14, 5, 3
    component_num = not_recursive(n, k, m)
    print(component_num)
