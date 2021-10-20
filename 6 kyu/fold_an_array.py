def fold_array(array, runs):
    nums = list(array)
    for _ in range(runs):
        for a in range(len(nums) // 2):
            print(a)
            nums[a] += nums.pop()
    return nums

# def fold_array(array, runs):
#     for i in range(runs):
#         new_array = []
#         if len(array) % 2 == 0:
#             start = 0
#             finish = -1
#             for i in range(int(len(array) / 2)):
#                 star = array[start]
#                 fini = array[finish]
#                 new_array.append(star + fini)
#                 start += 1
#                 finish -= 1
#         else:
#             start = 0
#             finish = -1
#             for i in range(int(len(array) / 2)):
#                 star = array[start]
#                 fini = array[finish]
#                 new_array.append(star + fini)
#                 start += 1
#                 finish -= 1
#             middle = int(len(array)/2)
#             new_array.append(array[middle])
#         array = new_array
#     return array

    