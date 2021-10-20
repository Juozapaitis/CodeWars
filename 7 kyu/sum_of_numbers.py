def get_sum(a,b):
    sum = 0
    if a < b:
        for num in range(a, b+1):
            sum = sum+num
        return sum
    else:
        for num in range(b, a+1):
            sum = sum+num
        return sum