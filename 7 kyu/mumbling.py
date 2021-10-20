def accum(s):
    new_str = ""
#     new_str = [(s[i] * (i + 1)).title() for i in range(len(s))]
    for i in range(0, len(s)):
        new_str += (s[i] * (i + 1)).title()
        if i != len(s) - 1:
            new_str += '-'
    return new_str