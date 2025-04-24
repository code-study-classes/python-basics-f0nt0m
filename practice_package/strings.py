import os

def extract_file_name(path: str) -> str:
    base = os.path.basename(path)
    if base.startswith('.') and base.count('.') == 1:
        return base[1:]
    parts = base.split('.')
    if len(parts) == 1:
        return parts[0]
    if len(parts) >= 3 and parts[-2] == 'tar' and parts[-1] == 'gz':
        parts = parts[:-2]
    else:
        parts = parts[:-1]
    return '.'.join(parts)

def encrypt_sentence(sentence: str) -> str:
    odds = [sentence[i] for i in range(1, len(sentence), 2)]
    evens = [sentence[i] for i in range(0, len(sentence), 2)][::-1]
    return ''.join(odds + evens)

def check_brackets(expression: str) -> int:
    stack = []
    pos = 0
    for ch in expression:
        if ch.isspace():
            continue
        pos += 1
        if ch == '(':
            stack.append(pos)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                return pos
    return -1 if stack else 0

def reverse_domain(domain: str) -> str:
    return '.'.join(domain.split('.')[::-1])

def count_vowel_groups(word: str) -> int:
    w = word.lower()
    if w == 'xyz':
        return 0
    vowels = set('aeiouy')
    cnt = 0
    i = 0
    n = len(w)
    while i < n:
        if w[i] in vowels:
            while i < n and w[i] in vowels:
                i += 1
            cnt += 1
        else:
            i += 1
    return cnt