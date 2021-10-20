### Sum of Digits / Digital Root

def digital_root(n):
    ans = n
    while ans >= 10:
        to_count = 0
        for digit in str(ans):
            to_count += int(digit)
        ans = to_count
    return ans