def sum_cubes(n):
    ans = 0
    for i in range(0,n+1):
        ans += i * i * i
    return ans