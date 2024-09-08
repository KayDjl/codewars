"""
Завершите решение так, чтобы оно разбило строку на пары по два символа. Если строка содержит нечетное количество символов, то следует заменить отсутствующий второй символ последней пары символом подчеркивания ('_').

Примеры:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
def solution(s):
    step = 2
    list = []
    for i in range(0, len(s), step):
        element = s[i:i+step]
        if len(element) == 1:
            list.append(element + '_')
        else:
            list.append(element)
    return list