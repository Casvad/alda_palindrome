def ternary_search(l, e):
    return _ternary_search(l, e, 0, len(l) - 1)


def _ternary_search(l, e, low, hi):
    if low > hi:
        return False

    mid1 = low + (hi - low) // 3
    mid2 = hi - (hi - low) // 3

    if l[mid1] == e or l[mid2] == e:
        return True
    elif e < l[mid1]:
        return _ternary_search(l, e, low, mid1 - 1)
    elif e > l[mid2]:
        return _ternary_search(l, e, mid2 + 1, hi)
    else:
        return _ternary_search(l, e, mid1 + 1, mid2 - 1)
