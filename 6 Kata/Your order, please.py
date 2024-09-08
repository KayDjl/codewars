"""
Ваша задача - отсортировать заданную строку. Каждое слово в строке будет содержать единственное число. Это число - позиция, которую слово должно занимать в результате.

Примечание: Числа могут быть от 1 до 9. Таким образом, 1 будет первым словом (не 0).

Если входная строка пуста, верните пустую строку. Слова во входной строке будут содержать только допустимые последовательные числа.

Примеры
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
"""
def order(sentence):
    words = sentence.split()
    ordered = sorted(words, key=int_from_word)
    return " ".join(ordered)

def int_from_word(word):
    for char in word:
        if char.isdigit():
            return int(char)