def guess_gifts(wishlist, presents): 
    got = []
    dic = {}
    for i in range(len(presents)):
        for j in range(len(wishlist)):
            if presents[i]["size"] == wishlist[j]["size"] and presents[i]["clatters"] == wishlist[j]["clatters"] and presents[i]["weight"] == wishlist[j]["weight"]:
                if ((wishlist[j]["name"] not in dic)):
                    got.append(wishlist[j]["name"]);
                    dic[wishlist[j]["name"]] = 1;     
    return got