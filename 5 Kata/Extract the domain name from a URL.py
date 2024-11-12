"""
Напишите функцию, которая при получении URL-адреса в виде строки анализирует только доменное имя и возвращает его в виде строки. Например:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
def domain_name(url):
    clss = "".join(url.split("http://"))
    clss = "".join(clss.split("https://"))
    clss = "".join(clss.split("www."))
    res = []
    for i in clss:
        if i == ".":
            break
        else:
            res.append(i)
    return "".join(res)