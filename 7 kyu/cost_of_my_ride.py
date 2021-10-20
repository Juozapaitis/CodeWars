def insurance(age, size, num_of_days): 
    if num_of_days < 0:
        return 0
    charge = 0
    if age < 25:
        charge += 10 * num_of_days
    if size == "medium":
        charge += 10 * num_of_days
    if size == "full-size" or size != "medium" and size != "economy":
        charge += 15 * num_of_days
    charge += num_of_days * 50
    return charge