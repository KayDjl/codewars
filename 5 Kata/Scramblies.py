"""
Завершите функцию, scramble(str1, str2) которая возвращает, true если часть str1 символов может быть переставлена для соответствия str2, в противном случае возвращает false.

Примечания:

Будут использоваться только строчные буквы (a-z). Знаки препинания или цифры не будут включены.
Необходимо учитывать производительность.
"""
def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True