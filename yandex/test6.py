import sys

# Рассмотрим три числа
# a
# a,
# b
# b и
# c
# c. Упорядочим их по возрастанию.
#
# Какое число будет стоять между двумя другими?
#
# Решение этой задачи на С++ могло бы выглядеть так:
#
# #include <iostream>
# #include <algorithm>
#
# using namespace std;
#
# int main()
# {
#     int a[3];
#     for (int i = 0; i < 3; ++i) cin >> a[i];
#     sort(a, a + 3);
#     cout << a[1] << endl;
#     return 0;
# }
# Формат ввода
# В единственной строке записаны три целых числа
# a
# a,
# b
# b,
# c
# c (
# −
# 1000
# ≤
# a
# ,
# b
# ,
# c
# ≤
# 1000
# −1000≤a,b,c≤1000), числа разделены одиночными пробелами.
#
# Формат вывода
# Выведите число, которое будет стоять между двумя другими после упорядочивания.


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
    nums = sorted(map(int, input().split()))
    print(nums[1])


if __name__ == "__main__":
    main()
