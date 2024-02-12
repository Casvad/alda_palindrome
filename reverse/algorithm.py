def reverse_pal(s):
    to_compare = ""
    for i in range(len(s) - 1, -1, -1):
        to_compare += s[i]
    return s == to_compare
