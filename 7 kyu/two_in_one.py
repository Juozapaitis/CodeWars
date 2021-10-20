def longest(a1, a2):
    # your code
    full = a1 + a2
    new = ''
    for i in full:
        if i not in new:
            new += i
    return ''.join(sorted(new)) 