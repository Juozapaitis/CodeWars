def narcissistic( value ):
    num = value
    num1 = value
    i = 0
    while num > 0:
        num //= 10
        i+=1
    s = 0
    while num1 > 0:
        digit = num1 % 10
        num1 //= 10
        s += pow(digit, i)
    if s == value:
        return True
    else:
        return False