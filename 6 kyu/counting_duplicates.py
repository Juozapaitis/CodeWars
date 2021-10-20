def duplicate_count(text):
    text = text.lower()
    how_many = 0
    freq = {c: text.count(c) for c in set(text)}
    ans = [how_many + 1 for k, v in freq.items() if v > 1]
    return sum(ans)