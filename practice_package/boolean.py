def _three_digit(n: int) -> bool:
    n = abs(n)
    return 100 <= n <= 999


def check_between_numbers(a: float, b: float, c: float) -> bool:
    return min(a, c) < b < max(a, c)


def check_odd_three(number: int) -> bool:
    if not _three_digit(abs(number)):
        return False
    return number % 2 != 0


def check_unique_digits(number: int) -> bool:
    n = abs(number)
    if not _three_digit(n):
        return False
    s = str(n)
    return len(set(s)) == 3


def check_palindrome_number(number: int) -> bool:
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number: int) -> bool:
    n = abs(number)
    if not _three_digit(n):
        return False
    a, b, c = map(int, str(n))
    return a < b < c