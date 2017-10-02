def quick_sort(lists):
    if len(lists) < 2:
        return lists

    else:
        key = lists[0]
        less = []
        greater = []
        for item in lists[1:]:
            if item <= key:
                less.append(item)
            else:
                greater.append(item)
        return quick_sort(less) + [key] + quick_sort(greater)


test = eval(input('please input a list: '))
print(quick_sort(test))
