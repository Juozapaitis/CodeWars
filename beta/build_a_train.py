def train(s):
    sum = 0
    info = {
        "A": 15,
        "B": 10,
        "C": 7,
        "D": 8,
        "_": 5,
    }
    for letter in s:
        sum += info.get(letter, 0)
    return sum