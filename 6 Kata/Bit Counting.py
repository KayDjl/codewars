"""
Напишите функцию, которая принимает целое число в качестве входных данных и возвращает количество битов, равных единице в двоичном представлении этого числа. Вы можете гарантировать, что входные данные неотрицательны.

Пример: Двоичное представление 1234 равно 10011010010, поэтому функция должна возвращать 5 в этом случае
"""
def count_bits(n):
    x = bin(n)
    return len(x[2:].replace("0", ""))