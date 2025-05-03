from datetime import datetime, date, timedelta, MAXYEAR
from decimal import Decimal
from itertools import chain

DATE_TIME_FORMAT = "%Y-%m-%d"
MAX_DATE = date(MAXYEAR, 12, 31)


def get_expired(items, in_advance_days=0):
    find_datetime = datetime(2023, month=12, day=10)  # datetime.now()
    if in_advance_days != 0:
        find_datetime += timedelta(days = in_advance_days)
    find_date = find_datetime.date()

    result = []
    for name, products in items.items():
        total_amount = sum(
            product.get('amount', 0) 
            for product in products 
            if (product.get('expiration_date') or MAX_DATE) <= find_date
        )
        if total_amount > 0:
            result.append((name, total_amount))    
    return result


goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {
            'amount': Decimal('1'), 
            'expiration_date': date(2023, 12, 9)
        }
    ],
    # 'Яйца': [
    #     {
    #         'amount': Decimal('2'),
    #         'expiration_date': date(2023, 12, 12)
    #     },
    #     {
    #         'amount': Decimal('3'),
    #         'expiration_date': date(2023, 12, 11)
    #     }
    # ],
    # 'Вода': [{'amount': Decimal('100'), 'expiration_date': None}],
}
# Если функция вызвана 10 декабря 2023 года
print(get_expired(goods))
# Вывод: [('Хлеб', Decimal('1'))]
# print(get_expired(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
# print(get_expired(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))] 
