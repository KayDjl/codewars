"""
Учитывая массив целых чисел, найдите то, которое встречается нечетное количество раз.

Всегда будет только одно целое число, которое появляется нечетное количество раз.

Примеры
[7] должен вернуться 7, потому что это происходит 1 раз (что странно).
[0] должен вернуться 0, потому что это происходит 1 раз (что странно).
[1,1,2] должен вернуться 2, потому что это происходит 1 раз (что странно).
[0,1,0,1,0] должен вернуться 0, потому что это происходит 3 раза (что странно).
[1,2,2,3,3,3,4,3,3,3,2,2,1] должен вернуться 4, потому что он появляется 1 раз (что странно).
"""
def find_it(seq):
    f = [x for x in set(seq) if seq.count(x) % 2 != 0]
    return f[0]