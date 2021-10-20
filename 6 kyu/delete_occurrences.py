def delete_nth(order,max_e):
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order