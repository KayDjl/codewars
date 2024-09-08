"""
Возвращает количество гласных в заданной строке.

Мы рассмотрим a, e, i o, u y).

Строка ввода будет состоять только из строчных букв и / или пробелов.
"""
def get_count(sentence):
    lis = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in sentence:
        for y in lis:
            if i == y:
                res.append(i)
    return len(res)