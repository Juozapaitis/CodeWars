def death_star(week, attack): 
    sumIron = 100
    sumSteel = 75
    sumChromium = 50
    for i in range(attack):
        sumIron -= week[i][0]
        sumSteel -= week[i][1]
        sumChromium -= week[i][2]
    
    if sumIron < 0:
        sumIron = 0
    if sumSteel < 0:
        sumSteel = 0
    if sumChromium < 0:
        sumChromium = 0
    
    if sumIron > 0 or sumSteel > 0 or sumChromium > 0:
        return "The station is destroyed! It needed {} iron, {} steel and {} chromium for completion.".format(sumIron, sumSteel, sumChromium)
    else:
        return "The station is completed!"
    # your code here
    pass