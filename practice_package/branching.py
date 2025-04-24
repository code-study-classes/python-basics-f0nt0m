_NUMS_1_19 = {
    0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
    5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
    10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
    13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
    16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'
}

_TENS = {
    20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
    60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
    90: 'девяносто', 100: 'сто'
}


def is_weekend(day: int) -> bool:
    return day in (6, 7)


def get_discount(amount: float) -> float:
    if amount >= 5000:
        rate = 0.10
    elif amount >= 1000:
        rate = 0.05
    else:
        rate = 0.0
    return round(amount * rate, 2)


def convert_to_meters(unit: int, length: float) -> float:
    factors = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01
    }
    return length * factors.get(unit, 0)


def describe_number(number: int) -> str:
    parity = 'четное' if number % 2 == 0 else 'нечетное'
    n = abs(number)
    if n <= 9:
        size = 'однозначное'
    elif n <= 99:
        size = 'двузначное'
    elif n <= 999:
        size = 'трехзначное'
    else:
        size = 'многозначное'
    return f"{parity} {size} число"


def _russian_number(n: int) -> str:
    if n in _NUMS_1_19:
        return _NUMS_1_19[n]
    if n in _TENS:
        return _TENS[n]
    tens, ones = divmod(n, 10)
    return f"{_TENS[tens * 10]} {_NUMS_1_19[ones]}"


def _age_suffix(n: int) -> str:
    if 11 <= n % 100 <= 14:
        return 'лет'
    last = n % 10
    if last == 1:
        return 'год'
    if last in (2, 3, 4):
        return 'года'
    return 'лет'


def describe_age(age: int) -> str:
    if age == 0:
        return 'ноль лет'
    if age == 100:
        return 'сто лет'
    return f"{_russian_number(age)} {_age_suffix(age)}"