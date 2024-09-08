"""
Учитывая 2 строки, a и b, верните строку вида short + long + short, с более короткой строкой снаружи и более длинной строкой внутри. Строки не будут одинаковой длины, но они могут быть пустыми ( zero длина ).

Подсказка для пользователей R:

Длина строки не всегда совпадает с количеством символов
Например: (Input1, Input2) --> вывод

("1", "22") --> "1221"
("22", "1") --> "1221"
ShortLongShort.solution("1", "22"); // returns "1221"
ShortLongShort.solution("22", "1"); // returns "1221"
"""
def solution(a, b):
    if len(a) > len(b):
        list = [b, a, b]
        return ''.join(list)
    else:
        list = [a, b, a]
        return ''.join(list)