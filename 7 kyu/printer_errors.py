import string
def printer_error(s):
    hm = 0
    for i in range(len(s)):
        if string.ascii_lowercase.index("{}".format(s[i])) < 13:
            hm += 1
        else:
            continue
        howmany = len(s) - hm
    return str(howmany) + "/" + str(len(s));
        