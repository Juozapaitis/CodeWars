def even_or_odd(s):
    n = int(s)
    even_sum = 0
    odd_sum = 0
    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            even_sum += int(s[i])
        else:
            odd_sum += int(s[i])
    if even_sum > odd_sum:
        return 'Even is greater than Odd'
    elif odd_sum > even_sum:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'