"""
Напишите функцию, которая принимает строку из одного или нескольких слов и возвращает ту же строку, но со всеми словами, в которых пять или более букв перевернуты (точно так же, как в названии этого ката). Передаваемые строки будут состоять только из букв и пробелов. Пробелы будут включены только в том случае, если присутствует более одного слова.

Примеры:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""
def spin_words(sentence):
    res = sentence.split(' ')
    lis = []
    for i in res:
        if len(i) >= 5:
            lis.append(i[::-1])
        else:
            lis.append(i)
    return ' '.join(lis)