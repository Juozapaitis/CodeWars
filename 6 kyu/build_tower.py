def tower_builder(n_floors):
    tower = []
    floor = ''

    for f in range(n_floors):
        stars = '*' * (f*2 + 1)
        spaces = ' ' * (n_floors - f - 1)
        floor = spaces + stars + spaces
        tower.append(floor)
        
    return tower