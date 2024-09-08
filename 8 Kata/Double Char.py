"""
Учитывая строку, вы должны вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.

Примеры (Ввод -> Вывод):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""
def double_char(s):
    list = []
    for i in s:
        x = i * 2
        list.append(x)
    return "".join(list)