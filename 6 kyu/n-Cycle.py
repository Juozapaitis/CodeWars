def cycle(n) :
    if ( n % 2 == 0 or n % 5 == 0):
        return -1
    c = 1
    res = 10 % n
    while ( res != 1 ):
        res = res * 10 % n
        c += 1
    print(c)
    return c