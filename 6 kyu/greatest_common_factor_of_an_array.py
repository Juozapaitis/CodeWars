from fractions import gcd
from functools import reduce
def greatest_common_factor(list):
    x = reduce(gcd, list)
    return x