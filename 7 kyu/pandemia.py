def infected(s):
    noOfNo = 0
    sick = 0
    if '0' and '1' not in s:
        return 0
    arr = s.split("X")
    for world in arr:
        if '1' in world:
            sick += len(world)
            noOfNo += len(world)
        else:
            noOfNo += len(world)
    return (sick / noOfNo * 100)