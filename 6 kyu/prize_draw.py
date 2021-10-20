# import string
# def rank(st, we, n):
#     if len(st) == 0:
#         return "No participants"
#     str = st.lower()
#     li = list(str.split(","))
#     if n > len(li):
#         return "Not enough participants"
#     sum_index_name = {}
#     i = 0
#     for name in li:
#         sum_index = 0
#         for letter in name:
#             letter_index = 0
#             letter_index += string.ascii_lowercase.index(letter) + 1
#             sum_index += letter_index
#             print(f"{letter} is {sum_index}")
#             sorted_name = sorted(name)
#         print(''.join(sorted_name))
#         som = len(name) + sum_index
#         winning_number = som + we[i]
#         sum_index_name[name] = winning_number
#         i+= 1
        
def rank(st, we, n):
    sum_index_name = {}
    if len(st) == 0:
        return "No participants"
    st = st.split(',')
    k = 0

    for name in st:
        s = 0
        for letter in name:
            s += ord(letter.lower()) - 97 + 1
        s += len(name)
        sum_index_name[name] = s*we[k]
        k += 1
    sum_index_name = sorted(sorted(sum_index_name), key=sum_index_name.get, reverse=True)

    if len(sum_index_name) < n:
        return "Not enough participants"
    else:
        return sum_index_name[n-1]