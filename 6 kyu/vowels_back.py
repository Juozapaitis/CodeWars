import string
def vowel_back(st):
    print(st)
    newStr = ""
    for letter in st:
        if letter == "c" or letter == "o":
            newLetterIndex = string.ascii_lowercase.index(letter)
            newLetter = string.ascii_lowercase[newLetterIndex - 1]
            if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                newStr += letter
            else:
                newStr += newLetter
        elif letter == "d":
            newLetterIndex = string.ascii_lowercase.index(letter)
            newLetter = string.ascii_lowercase[newLetterIndex - 3]
            if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                newStr += letter
            else:
                newStr += newLetter
        
        elif letter == "e":
            newLetterIndex = string.ascii_lowercase.index(letter)
            newLetter = string.ascii_lowercase[newLetterIndex - 4]
            if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                newStr += letter
            else:
                newStr += newLetter
                
        elif letter == "a" or letter == "i" or letter == "o" or letter == "u":
            newLetterIndex = string.ascii_lowercase.index(letter)
            if newLetterIndex - 5 > 0:
                newLetter = string.ascii_lowercase[newLetterIndex - 5]
                if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                    newStr += letter
                else:
                    newStr += newLetter
            else:
                newLetter = string.ascii_lowercase[21]
                newStr += newLetter
                
        else:
            newLetterIndex = string.ascii_lowercase.index(letter)
            if newLetterIndex + 9 >= 26:
                left = 26 - newLetterIndex
                newLetterIndex = 9 - left
#                 newLetterIndex = string.ascii_lowercase.index(start)
                newLetter = string.ascii_lowercase[newLetterIndex]
                if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                    newStr += letter
                else:
                    newStr += newLetter
            else:
                newLetter = string.ascii_lowercase[newLetterIndex + 9]
                if newLetter == "c" or newLetter == "o" or newLetter == "d" or newLetter == "e":
                    newStr += letter
                else:
                    newStr += newLetter
    return newStr