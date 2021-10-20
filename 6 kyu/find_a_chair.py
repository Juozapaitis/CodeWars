def meeting(rooms, number):
    if number == 0:
        return "Game On"
    ans = []
    i = 0
    is_on = True
    while is_on and i != len(rooms):
        if sum(ans) >= number:
            is_on = False
        elif len(rooms[i][0]) >= rooms[i][1]:
            ans.append(0)
            i += 1
        else:
            if abs(len(rooms[i][0]) - rooms[i][1]) > number:
                ans.append(number - sum(ans))
            else:
                ans.append(abs(len(rooms[i][0]) - rooms[i][1]))
                i += 1
    if sum(ans) < number:
        return "Not enough!"
    if sum(ans) > number:
        kiek = sum(ans) - number
        ans[-1] -= kiek
        return ans
    else:
        return ans