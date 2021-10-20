from numpy import diagonal
def matrix(array): 
    for x in range(len(array)) :
        for y in range(len(array[x])):
            if x == y:
                if array[x][y] < 0:
                    array[x][y] = 0
                else:
                    array[x][y] = 1
    # your code here
    return array