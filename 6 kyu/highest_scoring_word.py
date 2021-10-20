import string
def high(x):
    txt = x.split(" ")
    print(txt)
    scores = []
    for _ in txt:
        score = 0
        for letter in _:
            score += string.ascii_lowercase.index(letter) + 1
        scores.append(score)
    max_value = max(scores)
    max_index = scores.index(max_value)
    return txt[max_index]