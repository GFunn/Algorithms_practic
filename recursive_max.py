def recursive_max(lists):
    r_idx = len(lists) - 1
    if r_idx == 0:
        return lists[r_idx]
    if lists[r_idx] < lists[0]:
        lists.pop(r_idx)
        return recursive_max(lists)
    else:
        lists.pop(0)
        return recursive_max(lists)


li = eval(input('\ninput a list with [] around and , in between: \n'))
print(recursive_max(li))
