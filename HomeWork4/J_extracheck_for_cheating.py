"""
Дополнительная проверка на списывание

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Преподаватель курса ОиМП заказал у одного известного психолога полное
психологическое обследование всех студентов, поступивших на ФНК с целью выяснить
их склонность к списыванию ещё до начала занятий и отчислить их за списывание
ещё до того как они приступят к занятиям и смогут позорить ФНК своими
преступлениями. Психолог, привлеченный для проведения обследования, известен
своим инновационным методом, позволяющим понять склонность к списыванию студента
по наиболее часто используемому им в программах идентификатору. Помогите
известному психологу определить, какие из студентов потенциально являются
преступниками. Напишите программу, которая по приведённой программе выяснит
наиболее часто используемый в ней идентификатор.

Поскольку разные студенты на тестировании пишут программы на разных языках
программирования, ваша программа должна уметь работать с произвольным языком.
Поскольку в разных языках используются различные ключевые слова, то список
ключевых слов в анализируемом языке предоставляется на вход программе. Все
последовательности из латинских букв, цифр и знаков подчеркивания, которые не
являются ключевыми словами и содержат хотя бы один символ, не являющийся цифрой,
могут быть идентификаторами. При этом в некоторых языках идентификаторы могут
начинаться с цифры, а в некоторых - нет. Если идентификатор не может начинаться
с цифры, то последовательность, начинающаяся с цифры, идентификатором не
является. Кроме этого, задано, является ли язык чувствительным к регистру
символов, используемых в идентификаторах и ключевых словах.


Формат ввода:
В первой строке вводятся число n - количество ключевых слов в языке
(0 <= n <= 50) и два слова C и D, каждое из которых равно либо "yes", либо "no".
Слово C равно "yes", если идентификаторы и ключевые слова в языке чувствительны
к регистру символов, и "no", если нет. Слово D равно "yes", если идентификаторы
в языке могут начинаться с цифры, и "no", если нет.

Следующие n строк содержат по одному слову, состоящему из букв латинского
алфавита и символов подчеркивания - ключевые слова. Все ключевые слова непусты,
различны, при этом, если язык не чувствителен к регистру, то различны и без
учёта регистра. Длина каждого ключевого слова не превышает 50 символов.

Далее до конца входных данных идёт текст программы. Он содержит только символы с
ASCII-кодами от 32 до 126 и переводы строки.

Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один
идентификатор.


Формат вывода:
Выведите идентификатор, встречающийся в программе максимальное число раз. Если
таких идентификаторов несколько, следует вывести тот, который встречается в
первый раз раньше. Если язык во входных данных не чувствителен к регистру, то
можно выводить идентификатор в любом регистре.


Пример 1
input: 0 yes no
input: int main() {
input:   int a;
input:   int b;
input:   scanf("%d%d", &a, &b);
input:   printf("%d", a + b);
input: }
output: int

Пример 2
input: 0 yes no
input: #define INT int
input: int main() {
input:   INT a, b;
input:   scanf("%d%d", &a, &b);
input:   printf("%d %d", a + b, 0);
input: }
output: d

Пример 3
input: 6 no no
input: program
input: var
input: begin
input: end
input: while
input: for
input: program sum;
input: var
input:   A, B: integer;
input: begin
input:   read(A, b);
input:   writeln(a + b);
input: end.
output: a

Пример 4
input: 1 yes yes
input: _
input: a = 0h
input: b = 0h
input: c = 0h
output: 0h
"""
import re


INPUT_FILE_NAME = "input.txt"


def parse_input() -> tuple[list[str], set[str], bool, bool]:

    # читаем файл в список строк
    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")
    lines = input_file.read().strip().split("\n")

    # читаем входные параметры и приводим их к нормальной форме
    n, C, D = lines[0].split()
    n = int(n)
    match C:
        case "yes":
            is_case_sensitive = True
        case "no":
            is_case_sensitive = False
    match D:
        case "yes":
            can_start_with_number = True
        case "no":
            can_start_with_number = False

    # читаем ключевые слова с проверками
    keywords = set()
    for keyword in lines[1: n + 1]:

        if not is_case_sensitive:
            keyword = keyword.lower()

        if not can_start_with_number and keyword[0].isdigit():
            continue

        keywords.add(keyword)

    # читаем слова в программе в список
    words = []
    for line in lines[n + 1:]:
        line = re.sub("[^a-zA-Z0-9_]", " ", line)
        words.extend(line.split())

    return words, keywords, is_case_sensitive, can_start_with_number


def get_identifier_count(
    words: list[str],
    keywords: set[str],
    is_case_sensitive: bool,
    can_start_with_number: bool,
) -> dict[str, int]:

    identifier_count = dict()
    for word in words:

        if not is_case_sensitive:
            word = word.lower()

        if not is_identifier(word, keywords, can_start_with_number):
            continue

        identifier_count[word] = identifier_count.get(word, 0) + 1

    return identifier_count


def is_identifier(word: str, keywords: set[str], can_start_with_number: bool) -> bool:

    if not can_start_with_number and word[0].isdigit():
        return False

    if word.isdigit():
        return False

    if word in keywords:
        return False

    return True


if __name__ == "__main__":

    identifier_count = get_identifier_count(*parse_input())

    max_count = -1
    max_identifier = None
    for identifier, count in identifier_count.items():
        if count > max_count:
            max_count = count
            max_identifier = identifier

    print(max_identifier)
