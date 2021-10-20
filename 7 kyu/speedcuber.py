### Find the Speedcuber's times!

def cube_times(times):
    sorted_times = sorted(times)
    return (float("{:.2f}".format(sum(sorted_times[1:4]) / 3)), sorted_times[0])