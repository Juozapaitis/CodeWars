from math import sqrt
def is_square(arr):
    if len(arr) == 0:
        return None
    ans = ""
    for i in range(len(arr)):
        if sqrt(arr[i]).is_integer():
            ans += "+"
        else:
            ans += "-"
    return "-" not in ans