def rec_bi_search(lists, item, left=0, right=None):

    if right is None:
        right = len(lists)

    mid = int((left + right) / 2)

    if lists[mid] == item:
        return mid
    if lists[mid] < item:
        return rec_bi_search(lists, item, mid, right)
    else:
        return rec_bi_search(lists, item, left, mid)


li = eval(input('\nPlease input a list: '))
item = int(input('\nPlease input search item: '))
result = rec_bi_search(li, item)
print('The index of item is: %d' % result)
