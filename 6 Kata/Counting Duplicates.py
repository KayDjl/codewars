"""
Подсчитайте количество дубликатов
Напишите функцию, которая вернет количество символов без учета регистра. буквенные символы и цифровые разряды, которые встречаются более одного раза во входной строке. Можно предположить, что строка ввода содержит только алфавиты (как прописные, так и строчные) и цифровые разряды.

Пример
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"неделимость" -> 1 # 'i' occurs six times
"Неделимости" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""
def duplicate_count(text):
    res = []
    tp = text.lower()
    for i in tp:
        if tp.count(i) > 1:
            res.append(i)
        else:
            pass
    return len(set(res))