from recursive.tail_recursive import tail_call_optimized


@tail_call_optimized
def recursive_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    return recursive_pal(s[1 : len(s) - 1])
