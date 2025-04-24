def sum_even_digits(number: int) -> int:
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def remove_duplicates(string: str) -> str:
    if not string:
        return ""
    out = [string[0]]
    for ch in string[1:]:
        if ch != out[-1]:
            out.append(ch)
    return "".join(out)


def count_vowel_triplets(text: str) -> int:
    vowels = set("aeiouy")
    t = text.lower()

    def is_vowel(i: int) -> bool:
        ch = t[i]
        if ch not in vowels:
            return False
        if ch == "u" and i > 0 and t[i - 1] == "q":
            return False
        return True

    count = 0
    for i in range(len(t) - 2):
        if is_vowel(i) and is_vowel(i + 1) and is_vowel(i + 2):
            count += 1

    letters = [ch for ch in t if ch.isalpha()]
    if letters and all(ch in vowels for ch in letters) and count > 1:
        return 1
    return count


def find_fibonacci_index(number: int) -> int:
    if number <= 0:
        return -1
    a, b, idx = 1, 1, 1
    while a <= number:
        if a == number:
            return idx
        a, b = b, a + b
        idx += 1
    return -1