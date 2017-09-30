def recursive_sum(lists):
    if len(lists) == 0:
        return 0
    else:
        max_index = len(lists) - 1
        result = lists.pop(max_index) + recursive_sum(lists)
        return result


li = eval(input('\ninput a list with [] around and , in between: \n'))
print(recursive_sum(li))
