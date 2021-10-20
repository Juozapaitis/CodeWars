def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    st = ""
    sum = 0
    for i in range(0, n+1):
        if i != n:
            sum += i
            st += str(i) + "+"
        else:
            sum += i
            st += str(i) + " = " + str(sum)
    return st