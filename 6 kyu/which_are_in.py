def in_array(array1, array2):
    
    combined_list = []
    for i in range(len(array1)):
        if any(array1[i] in s for s in array2) and array1[i] not in combined_list:
            combined_list.append(array1[i])
    return sorted(combined_list)

# def in_array(array1, array2):
#     array3 = []
#     for i in range(len(array1)):
#         for j in range(len(array2)):
#             if array1[i] not in array3 and array1[i] in array2[j]:
#                 array3.append(array1[i])
#             else: 
#                 continue
#     return sorted(array3)