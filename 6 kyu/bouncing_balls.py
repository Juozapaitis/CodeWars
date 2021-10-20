def bouncing_ball(h, bounce, window):
    # your code
    times = 0
    if (h < 0 or bounce <= 0 or bounce >=1  or window > h):
        return -1

    while (h > window):
        times += 2
        h = h * bounce 
    
    return times-1