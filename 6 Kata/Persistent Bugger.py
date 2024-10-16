"""
Напишите функцию persistence, которая принимает положительный параметр num и возвращает его мультипликативную устойчивость, то есть количество раз, которое нужно умножить цифры в num до тех пор, пока не получится одна цифра.

Например (Ввод --> Вывод):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""
def persistence(n):
    if n < 10:
        return 0
    multiplier = 1
    while(n > 0):
        multiplier = (n % 10) * multiplier
        n = n // 10
    return persistence(multiplier) + 1