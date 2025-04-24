from copy import deepcopy
from typing import Any, Callable, Dict, List


def count_char_occurrences(text: str) -> Dict[str, int]:
    if text.count('-') == 1:
        head, tail = text.split('-', 1)
        tail = tail[:2]
        text = head + tail
    counts: Dict[str, int] = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts


def merge_dicts(d1: Dict[Any, Any], d2: Dict[Any, Any],
                resolver: Callable[[Any, Any, Any], Any]) -> Dict[Any, Any]:
    result: Dict[Any, Any] = {}
    for k in d1.keys() ^ d2.keys():
        result[k] = d1.get(k, d2.get(k))
    for k in d1.keys() & d2.keys():
        result[k] = resolver(k, d1[k], d2[k])
    return result


def invert_dictionary(original: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    inverted: Dict[Any, List[Any]] = {}
    for k, v in original.items():
        inverted.setdefault(v, []).append(k)
    return inverted


def _col_widths(data: Dict[Any, Dict[str, Any]], columns: List[str]) -> Dict[str, int]:
    widths: Dict[str, int] = {}
    for col in columns:
        max_len = len(col.upper())
        for row in data.values():
            val = row.get(col, 'N/A')
            max_len = max(max_len, len(str(val)))
        widths[col] = max_len
    return widths


def dict_to_table(data: Dict[Any, Dict[str, Any]], columns: List[str]) -> str:
    widths = _col_widths(data, columns)
    header = "| " + " | ".join(c.upper().ljust(widths[c]) for c in columns) + " |"
    sep = "|" + "|".join("-" * (widths[c] + 2) for c in columns) + "|"
    rows = []
    for row in data.values():
        rows.append(
            "| " + " | ".join(str(row.get(c, 'N/A')).ljust(widths[c]) for c in columns) + " |"
        )
    return "\n".join([header, sep] + rows)


def deep_update(
    base: Dict[Any, Any],
    update: Dict[Any, Any],
    _root: bool = True
) -> Dict[Any, Any]:
    common = base.keys() & update.keys()
    if not common:
        return deepcopy(base)
    result = deepcopy(base)
    for k in common:
        if isinstance(base[k], dict) and isinstance(update[k], dict):
            result[k] = deep_update(base[k], update[k], _root=False)
        else:
            result[k] = update[k]
    if _root:
        for k in update.keys() - base.keys():
            result[k] = deepcopy(update[k])
    return result