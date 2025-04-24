import re
from typing import List


def square_odds(numbers: List[int]) -> List[int]:
    return [n * n for n in numbers if n % 2 != 0]


def normalize_names(names: List[str]) -> List[str]:
    out: List[str] = []
    for name in names:
        if name.strip() == "":
            out.append(name)
        else:
            out.append(name.strip().capitalize())
    return out


def remove_invalid_emails(emails: List[str]) -> List[str]:
    pat = re.compile(r'^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$')
    return [e for e in emails if pat.match(e)]


def filter_palindromes(words: List[str]) -> List[str]:
    res: List[str] = []
    for w in words:
        lw = w.lower()
        if lw == lw[::-1]:
            res.append(w)
    return res


def calculate_factorial(n: int) -> int:
    if n < 2:
        return 1
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def find_common_prefix(strings: List[str]) -> str:
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix