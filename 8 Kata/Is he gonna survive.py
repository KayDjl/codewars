"""
Герой направляется в замок, чтобы завершить свою миссию. Однако ему сказали, что замок окружен парой могущественных драконов! для победы над каждым драконом требуется 2 пули, наш герой понятия не имеет, сколько пуль у него должно быть.. Если предположить, что он возьмет определенное количество пуль и двинется вперед, чтобы сразиться с другим определенным количеством драконов, выживет ли он?

Верните true, если да, false в противном случае :)
"""
def hero(bullets, dragons):
    drag = dragons * 2
    if bullets >= drag:
        return True
    else:
        return False