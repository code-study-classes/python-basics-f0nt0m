import math

def calculate_distance(x1: float, x2: float) -> float:
    return abs(x1 - x2)

def calculate_segments(a: int, b: int) -> int:
    if b == 0:
        return 0
    return a // b

def calculate_digit_sum(number: int) -> int:
    return sum(int(d) for d in str(abs(number)))

def calculate_rect_area(x1: float, y1: float, x2: float, y2: float) -> float:
    return abs(x2 - x1) * abs(y2 - y1)

def round_to_multiple(number: int, multiple: int) -> int:
    if multiple == 0:
        return number
    lower = (number // multiple) * multiple
    upper = lower + (multiple if multiple > 0 else -multiple)
    if abs(number - lower) <= abs(upper - number):
        return lower
    return upper