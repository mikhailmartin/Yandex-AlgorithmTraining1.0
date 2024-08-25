"""
Номер появления слова

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных символов идущих подряд, слова
разделены одним или большим числом пробелов или символами конца строки. Для
каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом
тексте ранее.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: one two one tho three
output: 0 0 1 0 0

Пример 2
input: She sells sea shells on the sea shore;
input: The shells that she sells are sea shells I'm sure.
input: So if she sells sea shells on the sea shore,
input: I'm sure that the shells are sea shore shells.
output: 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0

Пример 3
input: aba aba; aba @?"
output: 0 0 1 0
"""
