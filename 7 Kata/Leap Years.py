"""
В этом ката вы должны просто определить, является ли данный год високосным или нет. На случай, если вы не знаете правил, вот они:

Годы, кратные 4, являются високосными,
но годы, кратные 100, не являются не високосными годами,
но годы, кратные 400, являются високосными.
Проверенные годы находятся в пределах допустимого 1600 ≤ year ≤ 4000.
"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False