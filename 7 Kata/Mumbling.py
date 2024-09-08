"""
На этот раз никакой истории, никакой теории. В примерах ниже показано, как написать функцию accum:

Примеры:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
Параметр accum представляет собой строку, которая включает только буквы из a..z и A..Z.
"""
def accum(st):
    num = list(st)
    strr = ''
    for i, ind in enumerate(num):
        strr = strr + '-' + ind.upper()
        for _ in range(i):
            strr = strr + ind.lower()
    return strr[1:]