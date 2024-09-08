"""
Функция rgb является неполной. Завершите ее так, чтобы передача десятичных значений RGB привела к возвращению шестнадцатеричного представления. Допустимые десятичные значения для RGB - 0 - 255. Любые значения, выходящие за этот диапазон, должны быть округлены до ближайшего допустимого значения.

Примечание: Ваш ответ всегда должен состоять из 6 символов, сокращение с 3 здесь не сработает.

Примеры (ввод -> вывод):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""
def rgb(r, g, b):
    rec = [r, g, b]
    dex = []
    md = []
    for i, en in enumerate(rec):
        if en < 0:
            rec[i] = 0
        elif en > 255:
            rec[i] = 255
        else:
            pass
    dl = [hex(i) for i in rec]
    for i, id in enumerate(dl):
        dl[i] = id[2:]
    for i in dl: 
        if i.isdigit():
            dex.append("{:02}".format(int(i)))
        elif int(i, 16) <= 15:
            x = "{:02}".format(i)
            b = x[-1] + x[0]
            dex.append(b)
        else:
            dex.append(i)
    return "".join(dex).upper()

    #Refactor
    def rgb(r, g, b):
    rec = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rec(r), rec(g), rec(b))