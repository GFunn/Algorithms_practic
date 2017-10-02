import random
random.seed(1)


def quick_sort(lists):
    if len(lists) < 2:
        return lists

    else:
        key_idx = random.randint(0, len(lists) - 1)
        key = lists.pop(key_idx)
        less = []
        greater = []
        for item in lists:
            if item <= key:
                less.append(item)
            else:
                greater.append(item)
        return quick_sort(less) + [key] + quick_sort(greater)


test = eval(input('please input a list: '))
print(quick_sort(test))
