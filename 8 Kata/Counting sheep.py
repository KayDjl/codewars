"""
Рассмотрим массив/список овец, в котором некоторые овцы могут отсутствовать. Нам нужна функция, которая подсчитывает количество овец в массиве (истина означает наличие).

Например,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
Правильным ответом было бы 17.

Подсказка: не забудьте проверить наличие недопустимых значений, таких как null/undefined
"""
def count_sheeps(sheep):
    return sum([x for x in sheep if x is not None])