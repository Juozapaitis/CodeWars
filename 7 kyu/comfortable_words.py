def comfortable_word(word):
    left = "q, w, e, r, t, a, s, d, f, g, z, x, c, v, b"
    right = "y, u, i, o, p, h, j, k, l, n, m"
    ans = ""
    for char in word:
        if char in left:
            ans += "l"
        else:
            ans += "r"
    if "ll" in ans or "rr" in ans:
        return False
    return True