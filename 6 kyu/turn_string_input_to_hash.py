def str_to_hash(st): 
    ans_dict = {}
    if len(st) == 0:
        return ans_dict
    ans1 = st.replace(" ", "").split(",")
    for ans in ans1:
        k = ans.split("=")[0]
        v = int(ans.split("=")[1])
        ans_dict[k] = v
    return ans_dict