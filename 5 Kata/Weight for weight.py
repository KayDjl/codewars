"""
Мы с моим другом Джоном являемся членами клуба "Fat to Fit Club (FFC)". Джон - woзатруднительно, потому что каждый месяц публикуется список с весами участников, и каждый месяц он последний в списке, что означает, что он самый тяжелый.

Я тот, кто устанавливает список, поэтому я сказал ему: "Больше не волнуйся, я изменю порядок списка". Было решено присвоить числам "вес". Вес числа wiотныне будет равен сумме его цифр.

Например, 99 будет иметь "вес" 18, 100 будет иметь "вес" 1, поэтому в списке 100 будет стоять перед 99.

Учитывая строку с весами участников FFC в обычном порядке, можете ли вы упорядочить эту строку по «весам» этих чисел?

Пример:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
Если два числа имеют одинаковый «вес», давайте классифицировать их как строки (в алфавитном порядке), а не как числа:

180 стоит перед 90 так как, имея тот же «вес» (9), он стоит перед строкой.

Все числа в списке являются положительными числами, и список может быть пустым.

Примечания
может случиться так, что во входной строке будут ведущие и конечные пробелы, а также более одного пробела между двумя последовательными числами
Для C: результат освобождается.
"""
def order_weight(strng):
    clss = strng.split()
    sorted_list = sorted(clss, key = lambda x: (sum_digit(x), x))
    return " ".join(sorted_list)
    
def sum_digit(s):
    return sum(int(x) for x in s)
    