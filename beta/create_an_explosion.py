def boom_intensity(n):
    if n < 2:
        return "boom"
    if n % 2 == 0:
        if n % 5 == 0:
            return "B" + n * "O" + "M!"
        else:
            return "B" + n * "o" + "m!"
    elif n % 5 == 0:
        return "B" + n * "O" + "M"