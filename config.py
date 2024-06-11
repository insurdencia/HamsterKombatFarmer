"""
    FEATURES:
        1. buy_upgrades -> отключение покупки карточек
        2. buy_decision_method -> метод покупки карточек (
            - price -> покупать самую дешевую
            - payback -> покупать ту, что быстрей всего окупится
            - profit -> покупать самую прибыльну
            - profitness -> покупать самую профитную (сколько добыча на каждый потраченный хома-рубль)
            )
        3. delay_between_attempts -> Задержка между заходами в секундах
    
    TOKENS:
        name -> Название аккаунта. Так он будет виден в логе
        token -> токен аккаунта
        proxies -> настройки прокси, "кто знает - тот поймет". Если не нужен прокси, лучше убрать
"""


FEATURES = {
    "buy_upgrades": True,
    "buy_decision_method": "payback",
    "delay_between_attempts": 60 * 10,
}


TOKENS = [
    {"name": "samir", "token": "1717857293288LE5FyVDMJ8u0GIxbybkaR5rKJnUVWbfnKgxqKIGY3ntbEYaPvvio6fkLeJ09eJWm6856018611", },
    {"name": "dildora", "token": "1717857581837QYAUst7vgRQF8hwNf1gVPHtS3oblBrcdHBvhitIfEgotaOYtzdxpY4wEfkFU0K10284452911", },
    {"name": "clousse", "token": "1717858156775nvrur4nmn95TnyC6sbS2YgJFqugtRLwDcWvLRsJIGNksb1sJNSKHKTRjfB4GUSgP6584103352", },
    {"name": "sanjrka", "token": "1717589217733rFf70NH2y21tbaVSjWmArn1X0UIkSWGiHejEpkaKdiQ9PMpoCB9J4DF1pZQBRffp6377724229", },
]
