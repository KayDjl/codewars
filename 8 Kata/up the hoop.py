"""
Алекс только что получил новый хула-хуп, он в восторге, но чувствует себя обескураженным, потому что его младший брат лучше его.

Напишите программу, в которой Алекс сможет ввести (n), сколько раз вращается обруч, и она вернет ему ободряющее сообщение:

Если Алекс получит 10 или более обручей, верните строку "Great, now move on to tricks".
Если он не получит 10 обручей, верните строку "Keep at it until you get it".
"""
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"