def square_digits(num):
    ans = [int(digit) ** 2 for digit in str(num)]
    return int(''.join(str(v) for v in ans))