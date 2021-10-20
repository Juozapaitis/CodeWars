def street_fighter_selection(fighters, initial_position, moves):
    ans = []
    fight = list(fighters)
    initial = list(initial_position)
    for i in range(len(moves)):
        if (moves[i] == 'left'):
            if initial[1] == 0:
                initial[1] = 5
            else:
                initial[1] -= 1
            ans.append(fight[initial[0]][initial[1]])
        if (moves[i] == 'right'):
            if initial[1] == 5:
                initial[1] = 0
            else:
                initial[1] += 1
            ans.append(fight[initial[0]][initial[1]])
        if (moves[i] == 'down'):
            if initial[0] == 1:
                initial[0] = 1
            else:
                initial[0] += 1
            ans.append(fight[initial[0]][initial[1]])
        if (moves[i] == 'up'):
            if initial[0] == 0:
                initial[0] = 0
            else:
                initial[0] -= 1
            ans.append(fight[initial[0]][initial[1]])
        
    return ans