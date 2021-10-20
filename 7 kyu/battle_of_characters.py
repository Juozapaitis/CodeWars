import string
def battle(x, y):
    xsum = 0
    ysum = 0
    for letter in x.lower():
        xsum += int(string.ascii_lowercase.index(letter))+1
    for letter in y.lower():
        ysum += int(string.ascii_lowercase.index(letter))+1
    if ysum > xsum:
        return y
    elif ysum == xsum:
        return "Tie!"
    else:
        return x