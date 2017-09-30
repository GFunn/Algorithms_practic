def rec_bi_search(lists, item):
    left = 0
    right = len(lists) - 1
    mid = int((left + right) / 2)
    if lists[mid] == item:
        return lists[mid]
    if lists[mid] < item:
        lists = lists[mid + 1:]
        return rec_bi_search(lists, item)
    else:
        lists = lists[:mid]
        return rec_bi_search(lists, item)


li = eval(input('\nPlease input a list: '))
item = int(input('\nPlease input search item: '))
result = rec_bi_search(li, item)
print('The index of item is: %d' % li.index(result))
