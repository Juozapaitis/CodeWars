def create_phone_number(n):
    st = ''.join(map(str, n))
    return ("(" + st[:3] + ") " + st[3:6] + "-" + st[6:])