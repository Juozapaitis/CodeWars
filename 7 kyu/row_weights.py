def row_weights(array):
    weight1 = 0
    weight2 = 0
    for i in range(len(array)):
        if i % 2 == 0:
            weight1 += array[i]
        else:
            weight2 += array[i]
    tuple = (weight1, weight2)
    return tuple