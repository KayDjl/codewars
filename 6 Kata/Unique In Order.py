"""
Реализуем функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список элементов без каких-либо элементов с одинаковым значением рядом друг с другом и сохранением исходного порядка элементов.

Например:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""
def unique_in_order(string):
    new_list = []
    for i in string:
        if not new_list:
            new_list.append(i)
        elif new_list[-1] != i:
            new_list.append(i)
    return new_list