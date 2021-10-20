def descending_order(num):
    converted_num = str(num)
    li = list(converted_num)
    li.sort(reverse=True)
    maxNumStr = ''.join(li)
    #toStr = str(li)
    #print(toStr)
    maxNum = int(maxNumStr)
    return maxNum