import datetime
def driver(data):
    print(data)
    result = ""
    # 1-5
    if len(data[2]) >= 5:
        result += data[2][0:5]
    else:
        result += data[2][0:len(data[2])]
        result += "9" * (5 - len(data[2]))
        
    # 6   
    result += data[3].split("-")[2][2]
    
    # 7-8
    datetime_object = datetime.datetime.strptime(data[3][3:6], "%b")
    month_number = datetime_object.month
    
    if month_number < 10:
        if data[-1] == "F":
            result += "5" + str(month_number)
        else:
            result += "0" + str(month_number)
    else:
        if data[-1] == "F":
            result += str(month_number + 50)
        else:
            result += str(month_number)
        
    # 9-10
    result += data[3][0:2]
    
    #11
    result += data[3][-1]
    
    #12-13
    result += data[0][0]
    if len(data[1]) < 1:
        result += "9"
    else:
        result += data[1][0]
        
    #14
    result += "9"
    
    #15
    result += "AA"
    
    return result.upper()