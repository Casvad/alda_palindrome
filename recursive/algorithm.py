def binary_search(l, e):
    return _binary_search(l, e, 0, len(l) - 1)


def _binary_search(l, e, low, hi):
    if low > hi:
        return False

    mid = (low + hi) // 2

    if l[mid] == e:
        return True
    elif l[mid] > e:
        return _binary_search(l, e, low, mid - 1)
    else:
        return _binary_search(l, e, mid + 1, hi)
