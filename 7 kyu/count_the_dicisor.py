def divisors(n):
    how_many = 0
    for i in range(1, n+1):
        if n % i == 0:
            how_many += 1
    return how_many