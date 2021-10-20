from itertools import chain
def sort_sequence(sequence):
    x, y = [], []
    for i in sequence:
        if i == 0:
            x+=[sorted(y) + [0]]
            y=[]
        else:
            y+=[i]
    return list(chain.from_iterable(sorted(x, key=lambda n: sum(n))))  