def solution(s):
    li = []
    if (len(s) % 2 != 0):
        s += '_'
    for i in range(0, len(s), 2):
        li.append(s[i:i+2])
    return li