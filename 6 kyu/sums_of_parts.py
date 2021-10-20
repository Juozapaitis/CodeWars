def parts_sums(ls):
    result = [sum(ls)]
    for i in ls:
        result.append(result[-1]-i)
    return result

# def parts_sums(ls):
#     sums = [0] * (len(ls) + 1)
#     for i, e in enumerate(reversed(ls)):
#         sums[len(ls) - i - 1] += sums[len(ls) - i] + e
#     return sums