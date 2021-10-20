def triple_x(s):
    index = s.find('x')
    if (s[index:index+3]) == "xxx":
        return True
    return False