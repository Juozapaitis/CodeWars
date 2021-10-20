def likes(names):

    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    return d[min(4, length)].format(*names, others = length - 2)

# def likes(names):
#     # your code here
#     num = len(names) - 2
#     if len(names) == 0:
#         return "no one likes this"
#     if len(names) == 1:
#         return names[0] + " likes this"
#     if (len(names) == 2):
#         return names[0] + " and " + names[1] + " like this"
#     if (len(names) == 3):
#         return names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     if (len(names) > 3):
#         return names[0 ]+ ", " + names[1] + " and " + str(num) + " others like this"