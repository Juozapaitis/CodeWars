def get_middle(s):
    odd = len(s) % 2
    mid = int(len(s) / 2)
    if (odd == 1):
        return s[mid]
    else:
        return s[mid-1] + s[mid]