def remove_rotten(bag_of_fruits):
    if bag_of_fruits == None:
        return []
    new = []
    for i in range(len(bag_of_fruits)):
        if 'rotten' in bag_of_fruits[i]:
            new.append(bag_of_fruits[i].replace('rotten', '').lower())
        else:
            new.append(bag_of_fruits[i].lower())
    return new