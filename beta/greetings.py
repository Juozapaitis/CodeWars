def greetings(time, name):
    if time == None or type(name) != str:
        return "Hey dude greet someone"
    return f"Good {time} {name}"


# def greetings(time, name):
#     if time == None:
#         if type(name) == str:
#             return "Hey" + str(name)
#         else:
#             return "Hey dude greet someone"
#     else:
#         return f"Good {time} {name}"