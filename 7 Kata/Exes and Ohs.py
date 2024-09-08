"""
Проверьте, содержит ли строка одинаковое количество символов "x" и "o". Метод должен возвращать логическое значение и не учитывать регистр. Строка может содержать любой символ.

Примеры ввода / вывода:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    s = s.lower()
    x = s.count('o')
    y = s.count('x')
    if x == y:
        return True
    else:
        return False