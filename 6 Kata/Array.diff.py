"""
Ваша цель в этом ката - реализовать функцию разности, которая вычитает один список из другого и возвращает результат.

Это должно удалить все значения из списка a, которые присутствуют в списке b сохраняя их порядок.

array_diff([1,2],[1]) == [2]
Если значение присутствует в b, все его вхождения должны быть удалены из другого:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""

#Refactor
def array_diff(a, b):
    return [x for x in a if x not in b]

#on
def array_diff(a, b):
    for i in b: 
        if i == None:
            return a
            break  
        elif i in a:
            for item in range(a.count(i)):
                a.remove(i)
    return a