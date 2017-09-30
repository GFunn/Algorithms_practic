def binary_search(lists, item):
    low = 0
    high = len(lists) - 1

    while low < high:
        mid = int((low + high) / 2)
        guess = lists[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 2))
