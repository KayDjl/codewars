"""
ROT13 - это простой шифр замены букв, который заменяет букву буквой, следующей за ней в алфавите на 13 букв. ROT13 - это пример шифра Цезаря.

Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку включены числа или специальные символы, они должны быть возвращены в том виде, в каком они есть. Сдвигать следует только буквы латинского / английского алфавита, как в оригинальной Rot13 "реализации".

Пожалуйста, обратите внимание, что использование encode считается мошенничеством.
"""
def rot13(message):
    alf = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rot13 = ''
    for i in message:
        if i in alf:
            if i.isalpha() == True:
                rot13 += alf[alf.index(i) + 13]
        else:
            rot13 += i
    return rot13