"""
Полиглоты

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Каждый из N школьников некоторой школы знает M_i языков. Определите, какие
языки знают все школьники и языки, которые знает хотя бы один из школьников.


Формат ввода:
Первая строка входных данных содержит количество школьников N. Далее идёт
N чисел M_i, после каждого из чисел идет M_i строк, содержащих названия языков,
которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
количество различных языков не более 1000. 1 ≤ N ≤ 1000, 1 ≤ Mi ≤ 500.


Формат вывода:
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков.


Пример
input: 3
input: 3
input: Russian
input: English
input: Japanese
input: 2
input: Russian
input: English
input: 1
input: English
output: 1
output: English
output: 3
output: Russian
output: Japanese
output: English
"""
if __name__ == "__main__":

    allknown_langs = set()
    all_langs = set()

    n = int(input())
    for i in range(n):
        m = int(input())
        current_langs = set()
        for _ in range(m):
            lang = input()
            current_langs.add(lang)
        all_langs |= current_langs
        if i == 0:
            allknown_langs = current_langs
        else:
            allknown_langs &= current_langs

    print(len(allknown_langs))
    print(*allknown_langs, sep="\n")
    print(len(all_langs))
    print(*all_langs, sep="\n")
