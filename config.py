"""
    FEATURES:
        1. buy_upgrades -> управление покупкой карточек. 
            True -> Включено, 
            False -> Выключено
        2. buy_decision_method -> метод покупки карточек (
            - price -> покупать самую дешевую
            - payback -> покупать ту, что быстрей всего окупится
            - profit -> покупать самую прибыльну
            - profitness -> покупать самую профитную (сколько добыча на каждый потраченный хома-рубль)
            )
        3. delay_between_attempts -> Задержка между заходами в секундах
        4. num_purchases_per_cycle -> Кол-во покупок карточек за цикл
        5. min_cash_value_in_balance -> Если баланс меньше этого карточки не покупать

    ACCOUNTS:
        name -> Название аккаунта. Так он будет виден в логе
        token -> токен аккаунта
        proxies -> настройки прокси, "кто знает - тот поймет". Если не нужен прокси, лучше убрать
        buy_upgrades -> Описано в FEATURES, можно указать для каждого аккаунта отдельно
        buy_decision_method -> Описано в FEATURES, можно указать для каждого аккаунта отдельно
"""

try:
    from config_local import FEATURES, ACCOUNTS
except:

    FEATURES = {
        "buy_upgrades": True,
        "buy_decision_method": "profit",
        "delay_between_attempts": 60 * 10,     # эта задержка будет применятся c доп. рандомом ( +/- 60сек )
        "num_purchases_per_cycle": 5,
        "min_cash_value_in_balance": 1_000_000,
    }

    ACCOUNTS = [
        {"name": "samir", "token": "1717857293288LE5FyVDMJ8u0GIxbybkaR5rKJnUVWbfnKgxqKIGY3ntbEYaPvvio6fkLeJ09eJWm6856018611", },
        {"name": "dildora", "token": "1717857581837QYAUst7vgRQF8hwNf1gVPHtS3oblBrcdHBvhitIfEgotaOYtzdxpY4wEfkFU0K10284452911", },
        {"name": "clousse", "token": "1717858156775nvrur4nmn95TnyC6sbS2YgJFqugtRLwDcWvLRsJIGNksb1sJNSKHKTRjfB4GUSgP6584103352", },
        {"name": "sanjrka", "token": "1717589217733rFf70NH2y21tbaVSjWmArn1X0UIkSWGiHejEpkaKdiQ9PMpoCB9J4DF1pZQBRffp6377724229", },
    ]

for account in ACCOUNTS:
    account['buy_upgrades'] = account.get('buy_upgrades', FEATURES.get('buy_upgrades', True))
    account['buy_decision_method'] = account.get('buy_decision_method', FEATURES.get('buy_decision_method', 'payback'))
    account['num_purchases_per_cycle'] = account.get('num_purchases_per_cycle', FEATURES.get('num_purchases_per_cycle'))
    account['min_cash_value_in_balance'] = account.get('min_cash_value_in_balance', FEATURES.get('min_cash_value_in_balance', 0))
