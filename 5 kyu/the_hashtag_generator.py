def generate_hashtag(s):
    new = "#"
    if not s:
        return False
    else:
        cap = s.title()
        fixed = cap.replace(" ", "")
        if (len(new) + len(fixed) > 140):
            return False;
        else:
            return new + fixed