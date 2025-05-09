"""
43. Форматирование календаря
Решена
Лёгкая
Для отрисовки календаря в студенческом проекте было решено выделить функциональность форматирования в отдельный модуль.

Параметрами модуля (формально для функции, которую можно будет импортировать из модуля) будут количество дней в месяце и название дня недели, на который приходится первое число месяца, записанное на английском языке.

Выведите все дни месяца по неделям, дополнив первую неделю пустыми значениями, если это требуется.

Формат ввода
В единственной строке входных данных записаны две величины:

n
D
a
y
s
nDays (
28
≤
n
D
a
y
s
≤
31
28≤nDays≤31) - количество дней в месяце;
w
e
e
k
d
a
y
∈
[
M
o
n
d
a
y
,
T
u
e
s
d
a
y
,
W
e
d
n
e
s
d
a
y
,
T
h
u
r
s
d
a
y
,
F
r
i
d
a
y
,
S
a
t
u
r
d
a
y
,
S
u
n
d
a
y
]
weekday∈[Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday] — день недели, на который приходится первое число месяца.
Формат вывода
Выведите
k
k строк (
4
≤
k
≤
6
4≤k≤6), в
i
i-й строке выведите даты, которые попадают на
i
i-ю неделю месяца.

При выводе следуйте следующим правилам:

все строки, кроме последней, должны иметь ровно 7 элементов (в последней строке также может оказаться 7 элементов);
при выводе дней с номерами от 1 до 9 следует добавить символ точки (.) перед цифрой;
при выводе дней первой недели перед первым числом используйте две точки (..).
"""

import sys
from itertools import tee


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    count, day_name = input().split()
    count = int(count)
    day_index = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ].index(day_name)
    insert_day = [0] * day_index
    insert_day.extend(range(1, count + 1, 1))
    for index in range(len(insert_day) // 7 + 1):
        text = " ".join(
            map(
                lambda num: ".." if num == 0 else f".{num}" if num < 10 else str(num),
                insert_day[index * 7 : (index + 1) * 7],
            )
        )
        if text:
            print(text)


if __name__ == "__main__":
    main()
