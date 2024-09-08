"""
Переместите первую букву каждого слова в конец, затем добавьте "да" в конце слова. Знаки препинания оставьте нетронутыми.

Примеры
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
def pig_it(text):
    tex = text.split()
    rec = []
    for i in tex:
        if i != '!' and i != '?':
            rec.append(i[1:] + i[0] + 'ay')
        else:
            rec.append(i)
    return " ".join(rec)