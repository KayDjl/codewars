"""
Напишите алгоритм, который принимает массив и перемещает все нули в конец, сохраняя порядок расположения остальных элементов.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
def move_zeros(lst):
    li = []
    li2 = []
    for i in lst:     
        if i == 0:
            li.append(i)
    for i in lst:
        if i != 0:
            li2.append(i)
    return li2 + li