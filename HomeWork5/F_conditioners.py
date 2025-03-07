"""
Кондиционеры

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

При реализации проекта «Умная школа» было решено в каждый учебный класс
выбранной для этого школы установить по кондиционеру нового поколения для
автоматического охлаждения и вентиляции воздуха. По проекту в каждом классе
должен быть установлен только один кондиционер и мощность кондиционера должна
быть достаточной для размеров класса. Чем больше класс, тем мощнее должен быть
кондиционер.

Все классы школы пронумерованы последовательно от 1 до n. Известно, что для
каждого класса с номером i, требуется ровно один кондиционер, мощность которого
больше или равна a_i ватт.

Администрации школы предоставили список из m различных моделей кондиционеров,
которые можно закупить. Для каждой модели кондиционера известна его мощность и
стоимость. Требуется написать программу, которая определит, за какую минимальную
суммарную стоимость кондиционеров можно оснастить все классы школы.


Формат ввода:
Первая строка входного файла содержит одно целое число n (1 ≤ n ≤ 50 000)
количество классов в школе.

Вторая строка содержит n целых чисел ai (1 ≤ a_i ≤ 1000) — минимальная мощность
кондиционера в ваттах, который можно установить в классе с номером i.

Третья строка содержит одно целое число m (1 ≤ m ≤ 50 000) — количество
предложенных моделей кондиционеров.

Далее, в каждой из m строк содержится пара целых чисел b_j и c_j
(1 ≤ b_j ≤ 1000, 1 ≤ c_j ≤ 1000) мощность в ваттах j-й модели кондиционера и его
цена в рублях соответственно.


Формат вывода:
Выходной файл должен содержать одно число минимальную суммарную стоимость
кондиционеров в рублях. Гарантируется, что хотя бы один корректный выбор
кондиционеров существует, и во всех классах можно установить подходящий
кондиционер.


Пример 1
input: 1
input: 800
input: 1
input: 800 1000
output: 1000

Пример 2
input: 3
input: 1 2 3
input: 4
input: 1 10
input: 1 5
input: 10 7
input: 2 3
output: 13


Примечания:
В первом примере нужно купить один единственно возможный кондиционер за
1000 рублей.

Во втором примере оптимально будет установить в первом и втором классах
кондиционеры четвертого типа, а в третьем классе – кондиционер третьего типа.
Суммарная стоимость этих кондиционеров будет составлять 13 рублей (3 + 3 + 7).
"""


def parse_input() -> tuple[list[int], list[tuple[int, int]]]:

    n = int(input())
    powers = list(map(int, input().split(" ")))
    m = int(input())
    power_price = [tuple(map(int, input().split(" "))) for _ in range(m)]

    return powers, power_price


def main(powers: list[int], power_price: list[tuple[int, int]]) -> int:

    power_price = preprocessed(power_price)

    total_cost = 0
    for power in powers:
        for power_, price_ in power_price:
            if power_ < power:
                continue
            else:
                total_cost += price_
                break

    return total_cost


def preprocessed(old_power_price: list[tuple[int, int]]) -> list[tuple[int, int]]:

    old_power_price = sorted(old_power_price, reverse=True)
    for i in range(1, len(old_power_price)):
        current_power, current_price = old_power_price[i]
        previous_power, previous_price = old_power_price[i - 1]
        old_power_price[i] = (current_power, min(current_price, previous_price))

    old_power_price = sorted(old_power_price)
    new_power_price = [old_power_price[0]]
    previous_power = old_power_price[0][0]
    for power, price in old_power_price:
        if power != previous_power:
            new_power_price.append((power, price))
            previous_power = power

    return new_power_price


if __name__ == "__main__":

    powers, power_price = parse_input()

    result = main(powers, power_price)
    print(result)
