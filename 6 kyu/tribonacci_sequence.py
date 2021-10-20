def tribonacci(signature, n):
    #your code here
    if n == 0:
        return []
    if n == 1:
        return signature[:1]
    if n == 2:
        return signature[:2]
    else:
        for i in range(2, n-1):
            signature.append(sum(signature[i-2:i+1]))
    return signature