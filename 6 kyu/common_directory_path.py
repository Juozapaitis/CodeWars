import os
def get_common_directory_path(pathes):
    new_l = []
    [new_l.append(pathes[i]) for i in range(len(pathes))]
    try:
        a =  os.path.dirname(os.path.commonprefix(new_l))
        if a != '/' and a != '':
            a += '/'
        return a
    except ValueError:
        return ''