def find_senior(lst): 
    max = -1
    answer = []
    for i in range(len(lst)):
        if lst[i]['age'] == max:
            answer.append(lst[i])
        if lst[i]['age'] > max:
            max = lst[i]['age']
            answer.clear()
            answer.append(lst[i])
        
    return answer
    
    # your code here