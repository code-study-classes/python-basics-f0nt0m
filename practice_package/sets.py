from typing import Any, Iterable, List, Set


def find_common_elements(set1: Set[Any], set2: Set[Any]) -> Set[Any]:
    return set1 & set2


def find_shared_items(*sets: Iterable[Set[Any]]) -> Set[Any]:
    if not sets:
        return set()
    res = set(sets[0])
    for s in sets[1:]:
        res &= set(s)
    return res


def is_superset(set_a: Set[Any], set_b: Set[Any]) -> bool:
    return set_a.issuperset(set_b)


def remove_duplicates(items: List[Any]) -> List[Any]:
    seen = set()
    out: List[Any] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def count_unique_words(text: str) -> int:
    words = text.lower().split()
    return len(set(words))