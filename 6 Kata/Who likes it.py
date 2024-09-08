"""
Вы, наверное, знаете систему "лайков" на Facebook и других страницах. Люди могут ставить "лайки" публикациям в блоге, картинкам или другим элементам. Мы хотим создать текст, который должен отображаться рядом с таким элементом.

Реализуйте функцию, которая принимает массив, содержащий имена людей, которым понравился элемент. Он должен возвращать отображаемый текст, как показано в примерах:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Примечание: Для 4 или более имен число в "and 2 others" просто увеличивается.
"""
def likes(names):
    p = len(names)
    sum = p - 2
    if not names:
        return 'no one likes this'
    elif p == 1:
        return f"{names[0]} likes this"
    elif p == 2:
        return f"{names[0]} and {names[1]} like this"
    elif p == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {sum} others like this"
        