def hex_string_to_RGB(hex_string): 
    h = hex_string.lstrip('#')
    b = ('{}'.format( tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) )).replace("(", "").replace(")", "")
    myMap = {} 
    myMap["r"] = int(b.split(',')[0])
    myMap["g"] = int(b.split(',')[1])
    myMap["b"] = int(b.split(',')[2])
    return myMap