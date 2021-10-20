def unlock(message):
    coded = ""
    msg = message.lower()
    for i in range(len(msg)):
        if('c' >= msg[i] >= 'a'):
            coded += '2'
        if('f' >= msg[i] >= 'd'):
            coded += '3'
        if('i' >= msg[i] >= 'g'):
            coded += '4'
        if('l' >= msg[i] >= 'j'):
            coded += '5'
        if('o' >= msg[i] >= 'm'):
            coded += '6'
        if('s' >= msg[i] >= 'p'):
            coded += '7'
        if('v' >= msg[i] >= 't'):
            coded += '8'
        if('z' >= msg[i] >= 'w'):
            coded += '9'
    return coded