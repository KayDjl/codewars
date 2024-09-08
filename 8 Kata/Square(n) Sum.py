"""
Завершите функцию square sum так, чтобы она возводила в квадрат каждое переданное в нее число, а затем суммировала результаты вместе.
"""
def square_sum(numbers):
    y = []
    s = 0
    for i in numbers:
        s = i ** 2
        y.append(s)
    return sum(y)   