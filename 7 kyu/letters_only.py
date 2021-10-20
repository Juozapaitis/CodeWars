def remove_chars(s):
    ans = ""
    for char in s:
        if char.isalpha() or char == " ":
            ans += char
    return ans