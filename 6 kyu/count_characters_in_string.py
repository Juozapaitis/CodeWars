def count(string):
    return {e:string.count(e) for e in set(string)}