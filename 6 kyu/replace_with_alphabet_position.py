import string
def alphabet_position(text):
    ans = []
    final = ""
    for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'', ' ']:
        text = text.replace(ch,"")
    for letter in text.lower():
        a = string.ascii_lowercase.index(letter) + 1
        ans.append(a)
    for number in ans:
        final += str(number) + " "
    return final[:-1]