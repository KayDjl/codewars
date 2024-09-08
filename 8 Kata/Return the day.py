"""
Завершите работу функции, которая возвращает день недели в соответствии с введенным номером:

1 ВОЗВРАТ "Sunday"
2 ВОЗВРАТ "Monday"
3 ВОЗВРАТ "Tuesday"
4 ВОЗВРАТ "Wednesday"
5 ВОЗВРАТ "Thursday"
6 ВОЗВРАТ "Friday"
7 ВОЗВРАТ "Saturday"
В противном случае возвращает "Wrong, please enter a number between 1 and 7"
"""
WEEKDAY = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday' }
ERROR = 'Wrong, please enter a number between 1 and 7'


def whatday(n):
    return WEEKDAY.get(n, ERROR)