def solution(s):
    new_str = ""
    for letter in s:
        if ord(letter) in range(65,91):
            new_str+=" "
        new_str+=letter
    
    return new_str